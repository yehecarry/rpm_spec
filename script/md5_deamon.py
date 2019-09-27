# !/usr/bin/env python
# encoding: utf-8
# description: 一个守护进程的简单包装类, 具备常用的start|stop|restart|status功能, 使用方便
#             需要改造为守护进程的程序只需要重写基类的run函数就可以了
# date: 2015-10-29
# usage: 启动: python daemon_class.py start
#       关闭: python daemon_class.py stop
#       状态: python daemon_class.py status
#       重启: python daemon_class.py restart
#       查看: ps -axj | grep daemon_class

import atexit, os, sys, time, signal


class CDaemon:
    '''
    a generic daemon class.
    usage: subclass the CDaemon class and override the run() method
    stderr  表示错误日志文件绝对路径, 收集启动过程中的错误日志
    verbose 表示将启动运行过程中的异常错误信息打印到终端,便于调试,建议非调试模式下关闭, 默认为1, 表示开启
    save_path 表示守护进程pid文件的绝对路径
    '''

    def __init__(self, save_path, stdin=os.devnull, stdout=os.devnull, stderr=os.devnull, home_dir='.', umask=int("022"),
                 verbose=1):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = save_path  # pid文件绝对路径
        self.home_dir = home_dir
        self.verbose = verbose  # 调试开关
        self.umask = umask
        self.daemon_alive = True

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

        os.chdir(self.home_dir)
        os.setsid()
        os.umask(int(self.umask))

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()

        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        if self.stderr:
            se = open(self.stderr, 'a+')
        else:
            se = so

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        def sig_handler(signum, frame):
            self.daemon_alive = False

        signal.signal(signal.SIGTERM, sig_handler)
        signal.signal(signal.SIGINT, sig_handler)

        if self.verbose >= 1:
            print('daemon process started ...')

        atexit.register(self.del_pid)
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write('%s\n' % pid)

    def get_pid(self):
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        except SystemExit:
            pid = None
        return pid

    def del_pid(self):
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)

    def start(self, *args, **kwargs):
        if self.verbose >= 1:
            print('ready to starting ......')
        # check for a pid file to see if the daemon already runs
        pid = self.get_pid()
        if pid:
            msg = 'pid file %s already exists, is it already running?\n'
            sys.stderr.write(msg % self.pidfile)
            sys.exit(1)
        # start the daemon
        self.daemonize()
        self.run(*args, **kwargs)

    def stop(self):
        if self.verbose >= 1:
            print('stopping ...')
        pid = self.get_pid()
        if not pid:
            msg = 'pid file [%s] does not exist. Not running?\n' % self.pidfile
            sys.stderr.write(msg)
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)
            return
        # try to kill the daemon process
        try:
            i = 0
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
                i = i + 1
                if i % 10 == 0:
                    os.kill(pid, signal.SIGHUP)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)
            if self.verbose >= 1:
                print('Stopped!')

    def restart(self, *args, **kwargs):
        self.stop()
        self.start(*args, **kwargs)

    def is_running(self):
        pid = self.get_pid()
        # print(pid)
        return pid and os.path.exists('/proc/%d' % pid)

    def run(self, *args, **kwargs):
        'NOTE: override the method in subclass'
        print('base class run()')


class ClientDaemon(CDaemon):
    def __init__(self, name, save_path, stdin=os.devnull, stdout=os.devnull, stderr=os.devnull, home_dir='.', umask=int("022"), verbose=1):
        CDaemon.__init__(self, save_path, stdin, stdout, stderr, home_dir, umask, verbose)
        self.name = name  # 派生守护进程类的名称

    def set_md5(self):
        output = os.popen('find /usr/share/nginx/html/ -type f | grep -v .md5$')
        file_list = output.read().split('\n')
        for file in file_list:
            if file != "" and not os.path.exists("%s.md5" % file):
                os.popen('md5sum %s > %s.md5' % (file, file))

    def set_all_md5(self):
        os.popen('md5sum `find /usr/share/nginx/html/ -type f | grep -v .md5$` > /usr/share/nginx/all.md5')



    def run(self, output_fn, **kwargs):
        dir_size = os.popen("du -s /usr/share/nginx/html/ | awk '{print $1}'")
        dir_size = dir_size.read()
        fd = open(output_fn, 'w')
        while True:
            dir_size_check = os.popen("du -s /usr/share/nginx/html/ | awk '{print $1}'")
            dir_size_check = dir_size_check.read()
            if dir_size != dir_size_check:
                #生成改变后的md5码
                output = os.popen('find /usr/share/nginx/html/ -type f | grep -v .md5$')
                file_list = output.read().split('\n')
                for file in file_list:
                    if file != "" and not os.path.exists("%s.md5" % file):
                        os.popen('md5sum %s > %s.md5' % (file, file))
                #生成改变后md5码列表
                os.popen('md5sum `find /usr/share/nginx/html/ -type f | grep -v .md5$` > /usr/share/nginx/all.md5')
                line = time.ctime()
                dir_size = dir_size_check
                fd.write("%s  Someone uploaded the file. dir size is %s" % (line,dir_size_check))
                fd.flush()
                #生成链接文件
                cfg_path = "/usr/share/nginx/html/techplatform/sdks/"
                dirs_path = ["bi/android", "bi/ios", "bi/unity", "pay/android", "pay/ios", "pay/unity", "gcfg/android", "gcfg/ios", "gcfg/unity"]
                time.sleep(3)
                for dir_path in dirs_path:
                    file_path = "%s%s" % (cfg_path, dir_path)
                    ctime = os.popen("date '+%m/%d/%Y'")
                    ctime = ctime.read().strip('\n')
                    file_name = os.popen("find %s -type f -exec ls -lrt {} \; |awk '{print $9}' | grep -v latest | grep ^/ | egrep '.zip$|.unitypackage$|.jar$' | tail -n 1 " % file_path)
                    file_name = file_name.read().strip('\n')
		    #写file_path 的时候不要多写一个/
                    if file_path == "/usr/share/nginx/html/techplatform/sdks/bi/android":
                        os.system('rm -rf /usr/share/nginx/html/techplatform/sdks/bi/android/FTDSDK-latest.zip')
                        os.system('ln -s %s /usr/share/nginx/html/techplatform/sdks/bi/android/FTDSDK-latest.zip' % file_name)
                    elif file_path == "/usr/share/nginx/html/techplatform/sdks/bi/ios":
                        os.system('rm -rf /usr/share/nginx/html/techplatform/sdks/bi/ios/with_appsflyer_latest.zip')
                        os.system('ln -s %s /usr/share/nginx/html/techplatform/sdks/bi/ios/with_appsflyer_latest.zip' % file_name)
                    elif file_path == "/usr/share/nginx/html/techplatform/sdks/bi/unity":
                        os.system('rm -rf /usr/share/nginx/html/techplatform/sdks/bi/unity/FTDSdk_latest.unitypackage')
                        os.system('ln -s %s /usr/share/nginx/html/techplatform/sdks/bi/unity/FTDSdk_latest.unitypackage' % file_name)
                    elif file_path == "/usr/share/nginx/html/techplatform/sdks/gcfg/android":
                        os.system('rm -rf /usr/share/nginx/html/techplatform/sdks/gcfg/android/FTGcfgSdk_latest.jar')
                        os.system('ln -s %s /usr/share/nginx/html/techplatform/sdks/gcfg/android/FTGcfgSdk_latest.jar' % file_name)
                    elif file_path == "/usr/share/nginx/html/techplatform/sdks/pay/android":
                        os.system('rm -rf /usr/share/nginx/html/techplatform/sdks/pay/android/FTPSdk_latest.jar')
                        os.system('ln -s %s /usr/share/nginx/html/techplatform/sdks/pay/android/FTPSdk_latest.jar' % file_name)
            time.sleep(5)


if __name__ == '__main__':
    help_msg = 'Usage: python %s <start|stop|restart|status>' % sys.argv[0]
    if len(sys.argv) != 2:
        print(help_msg)
        sys.exit(1)
    p_name = 'md5check'  # 守护进程名称
    pid_fn = '/tmp/daemon_class.pid'  # 守护进程pid文件的绝对路径
    log_fn = '/var/log/daemon_class.log'  # 守护进程日志文件的绝对路径
    err_fn = '/var/log/daemon_class.err.log'  # 守护进程启动过程中的错误日志,内部出错能从这里看到
    cD = ClientDaemon(p_name, pid_fn, stderr=err_fn, verbose=1)

    if sys.argv[1] == 'start':
        cD.start(log_fn)
    elif sys.argv[1] == 'stop':
        cD.stop()
    elif sys.argv[1] == 'restart':
        cD.restart(log_fn)
    elif sys.argv[1] == 'status':
        alive = cD.is_running()
        if alive:
            print('process [%s] is running ......' % cD.get_pid())
        else:
            print( 'daemon process [%s] stopped' % cD.name)
    else:
        print('invalid argument!')

