Name:           kibana
Version:        6.6.1
Release:        1%{?dist}
Summary:        this is kibana-6.6.1
 
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
mkdir -p $RPM_BUILD_ROOT/opt/kibana-6.6.1
cp -a * $RPM_BUILD_ROOT/opt/kibana-6.6.1


%files
%defattr(-,root,root)
/*

%post
cp /opt/kibana-6.6.1/script/kibana /etc/init.d/kibana
chmod a+x /etc/init.d/kibana
chkconfig kibana on
ulimit -n 65536


%changelog
