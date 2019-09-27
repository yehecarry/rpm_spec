Name:           elasticsearch
Version:        6.6.1
Release:        1%{?dist}
Summary:        this is elasticsearch-6.6.1
 
License:        GPL
URL:            http://www.yehe.info
Source0:        %{name}-%{version}.tar.gz
Requires: jdk >= 1.8
AutoReqProv: no


%description


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*

%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/elasticsearch-6.6.1
cp -a * $RPM_BUILD_ROOT/opt/elasticsearch-6.6.1


%files
%defattr(-,root,root)
/*

%post
cp /opt/elasticsearch-6.6.1/script/elasticsearch /etc/init.d/elasticsearch
chmod a+x /etc/init.d/elasticsearch
chkconfig elasticsearch on
ulimit -n 65536

id elastic >> /dev/null
if [ $? != 0 ];then
adduser elastic
chmod -R 777 /opt/elasticsearch-6.6.1/
fi

grep "* hard nofile 65536" /etc/security/limits.conf >> /dev/null
if [ $? != 0 ];then
echo "* soft noproc 65536" >> /etc/security/limits.conf
echo "* hard noproc 65536" >> /etc/security/limits.conf
echo "* soft nofile 65536" >> /etc/security/limits.conf
echo "* hard nofile 65536" >> /etc/security/limits.conf
fi

grep "vm.max_map_count=262144" /etc/sysctl.conf >> /dev/null
if [ $? != 0 ];then
echo "vm.max_map_count=262144" >> /etc/sysctl.conf
sysctl -p
fi


%changelog
