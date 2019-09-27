Name:		tsung
Version:	1.7.0
Release:	server
Summary:	tsung

License:	GPL
Source0:	tsung-1.7.0.tar.gz
BuildRequires:	gcc,make
#AutoReqProv: no
Requires: erlang >= 20.0 gnuplot >= 4.6.2 perl >= 5.0.0 openssh-askpass >= 7.4 ansible >= 2.4.0 
%description


%prep
%setup -q



%build
./configure --prefix=/opt/tsung-1.7.0
make -j8

%install
make install DESTDIR=%{buildroot}
cp -rp %{_topdir}/SOURCES/file/tsung %{buildroot}/opt/tsung-1.7.0/tsung


%files
%defattr (-,root,root)
/*

%pre

%post
ln -s /opt/tsung-1.7.0/bin/* /usr/bin/
ln -s /opt/otp_20.0/lib/erlang/bin/erl /usr/local/bin/
mv /opt/tsung-1.7.0/tsung /etc/ansible/roles
cp -rf /etc/ansible/roles/tsung/ansible.cfg /etc/ansible/ansible.cfg

%changelog
