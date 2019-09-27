Name:		memcached
Version:	1.4.25
Release:	el7
Summary:	memcached

License:	GPL
Source0:	memcached-1.4.25.tar.gz
BuildRequires:	gcc,make	
Requires: libevent >= 2.0.22
AutoReqProv: no

%description
memcached


%prep
%setup -q



%build
./configure --prefix=$RPM_BUILD_ROOT/opt/memcache_1.4.25 --with-libevent=/opt/libevent_2.0.22
make -j8
make install


%files
%defattr (-,root,root)
/*

%pre

%post

%changelog
