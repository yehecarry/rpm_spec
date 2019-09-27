Name:		tsung
Version:	1.7.0
Release:	v1
Summary:	tsung

License:	GPL
Source0:	tsung-1.7.0.tar.gz
BuildRequires:	gcc,make
#AutoReqProv: no
Requires: otp-src = 20.0 gnuplot >= 4.6.2 perl >= 5.0.0 openssh-askpass >= 7.4
%description


%prep
%setup -q



%build
./configure --prefix=/opt/tsung-1.7.9
make -j8

%install
make install DESTDIR=%{buildroot}
#mkdir -p $RPM_BUILD_ROOT/opt/tsung-1.7.9
#cp -rp /opt/tsung-1.7.9/* $RPM_BUILD_ROOT/opt/tsung-1.7.9


%files
%defattr (-,root,root)
/*

%pre

%post
ln -s /opt/tsung-1.7.9/bin/* /usr/bin/
ln -s /opt/otp_20.0/lib/erlang/bin/erl /usr/local/bin/

%changelog
