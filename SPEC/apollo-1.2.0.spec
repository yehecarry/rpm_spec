Name:           apollo
Version:        1.2.0
Release:        1%{?dist}
Summary:        this is apollo-1.2.0
 
License:        GPL
URL:            http://www.yehe.info
Source0:        %{name}-%{version}.tar.gz
Requires: jdk >= 1.8 maven >= 3.6.0
AutoReqProv: no


%description


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*

%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/apollo-1.2.0
cp -a * $RPM_BUILD_ROOT/opt/apollo-1.2.0


%files
%defattr(-,root,root)
/*

%post
cp /opt/apollo-1.2.0/script/apollo /etc/init.d/apollo
chmod a+x /etc/init.d/apollo
chkconfig apollo on


%changelog
