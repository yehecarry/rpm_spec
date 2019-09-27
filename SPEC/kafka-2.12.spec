Name:		kafka
Version:	2.12
Release:	el7
Summary:	kafka

License:	GPL
Source0:	kafka-2.12.tar.gz
BuildRequires:	gcc,make	
Requires: jdk >= 1.8

%description
kafka


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*



%build
mkdir -p $RPM_BUILD_ROOT/opt/kafka-2.12
cp -a * $RPM_BUILD_ROOT/opt/kafka-2.12




%files
%defattr (-,root,root)
/*

%pre
rm -rf /etc/rc.d/init.d/kafka
%post
cp /opt/kafka-2.12/script/kafka /etc/rc.d/init.d/kafka
chkconfig --add kafka
chkconfig kafka on

%changelog
