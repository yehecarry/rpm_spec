Name:		mariadb
Version:	10.3.10
Release:	el7
Summary:	mariadb

License:	GPL
Source0:	mariadb-10.3.10.tar.gz
BuildRequires:	gcc,make	
#Requires: libevent >= 2.0.22
AutoReqProv: no

%description
mariadb


%prep
%setup -q



%build
cmake . -DCMAKE_INSTALL_PREFIX=/opt/mariadb_10.3.10 \
 -DMYSQL_DATADIR=/data/mysql \
 -DSYSCONFDIR=/etc \
 -DWITHOUT_TOKUDB=1 \
 -DWITH_INNOBASE_STORAGE_ENGINE=1 \
 -DWITH_ARCHIVE_STPRAGE_ENGINE=1 \
 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
 -DWIYH_READLINE=1 \
 -DWIYH_SSL=system \
 -DVITH_ZLIB=system \
 -DWITH_LOBWRAP=0 \
 -DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
 -DDEFAULT_CHARSET=utf8 \
 -DDEFAULT_COLLATION=utf8_general_ci

make -j8

%install
make install DESTDIR=%{buildroot}
cp  %{_topdir}/SOURCES/file/mysql.sh $RPM_BUILD_ROOT/opt/mariadb_10.3.10/scripts
cp  %{_topdir}/SOURCES/file/my.cnf $RPM_BUILD_ROOT/opt/mariadb_10.3.10/scripts

%files
%defattr (-,root,root)
/*

%pre
groupadd -r mysql
useradd -r -g mysql -s /sbin/nologin -d /opt/mariadb_10.3.10 -M mysql
mkdir -p /data/mysql
chown -R mysql:mysql /data/mysql
mv /etc/my.cnf /etc/my.cnf.back


%post
cd /opt/mariadb_10.3.10/
scripts/mysql_install_db --user=mysql --datadir=/data/mysql
cp /opt/mariadb_10.3.10/support-files/mysql.server  /etc/rc.d/init.d/mariadb
cp /opt/mariadb_10.3.10/scripts/my.cnf /etc/
cp /opt/mariadb_10.3.10/scripts/mysql.sh /etc/profile.d
source /etc/profile.d/mysql.sh
chkconfig --add mariadb
service mariadb start

%changelog
