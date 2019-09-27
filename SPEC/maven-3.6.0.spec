Name:           maven
Version:        3.6.0
Release:        1%{?dist}
Summary:        this is maven-3.6.0
 
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
mkdir -p $RPM_BUILD_ROOT/opt/maven-3.6.0
cp -a * $RPM_BUILD_ROOT/opt/maven-3.6.0


%files
%defattr(-,root,root)
/*

%post
cat << EOF >> /etc/profile
export MAVEN_HOME=/opt/maven-3.6.0
export PATH=\$PATH:\$MAVEN_HOME/bin
EOF
source /etc/profile


%changelog
