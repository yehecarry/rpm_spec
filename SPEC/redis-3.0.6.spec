Name:		redis
Version:	3.0.6
Release:	el7
Summary:	redis

License:	GPL
Source0:	redis-3.0.6.tar.gz
BuildRequires:	gcc,make	

%description
redis


%prep
%setup -q



%build
make -j8
mkdir -p $RPM_BUILD_ROOT/opt/redis3.0.6/etc
cp %{_topdir}/SOURCES/file/redis.conf $RPM_BUILD_ROOT/opt/redis3.0.6/etc/redis.conf
cp %{_topdir}/SOURCES/file/redis.service $RPM_BUILD_ROOT/opt/redis3.0.6/etc/redis.service
cp %{_topdir}/SOURCES/file/sentinel.conf $RPM_BUILD_ROOT/opt/redis3.0.6/etc/sentinel.conf
cp %{_topdir}/SOURCES/file/redis-sentinel.service $RPM_BUILD_ROOT/opt/redis3.0.6/etc/redis-sentinel.service
make PREFIX=$RPM_BUILD_ROOT/opt/redis3.0.6 install



%files
%defattr (-,root,root)
/*

%pre

%post
ln -s /opt/redis3.0.6/bin/redis-benchmark /usr/bin/redis-benchmark
ln -s /opt/redis3.0.6/bin/redis-cli /usr/bin/redis-cli
ln -s /opt/redis3.0.6/bin/redis-server /usr/bin/redis-server
cp /opt/redis3.0.6/etc/redis.service /lib/systemd/system
cp /opt/redis3.0.6/etc/redis-sentinel.service  /lib/systemd/system
mkdir -p /opt/redis3.0.6/logs/
systemctl enable redis
systemctl restart redis

%changelog
