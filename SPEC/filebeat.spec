Name:           filebeat
Version:        6.6.1
Release:        1%{?dist}
Summary:        this is filebeat-6.6.1
 
License:        GPL
URL:            http://www.yehe.info
Source0:        %{name}-%{version}.tar.gz
#Requires: jdk >= 1.8
AutoReqProv: no


%description


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*

%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/filebeat-6.6.1
cp -a * $RPM_BUILD_ROOT/opt/filebeat-6.6.1


%files
%defattr(-,root,root)
/*

%post
cp /opt/filebeat-6.6.1/script/filebeat /etc/init.d/filebeat
chmod a+x /etc/init.d/filebeat
chkconfig filebeat on
ulimit -n 65536


%changelog
