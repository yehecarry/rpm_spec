Name:		libevent
Version:	2.0.22
Release:	el7
Summary:	libevent

License:	GPL
Source0:	libevent-2.0.22.tar.gz
BuildRequires:	gcc,make	
#Requires: libevent >= 2.0.22
AutoReqProv: no

%description


%prep
%setup -q



%build
./configure --prefix=/opt/libevent_2.0.22
#./configure --prefix=$RPM_BUILD_ROOT/opt/libevent-2.0.22
make -j8
#mkdir -p $RPM_BUILD_ROOT/opt/python-3.6.3
make install DESTDIR=%{buildroot}


%files
%defattr (-,root,root)
/*

%pre

%post

%changelog
