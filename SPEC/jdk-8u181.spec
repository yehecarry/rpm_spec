Name:		jdk
Version:	1.8.0
Release:	el7
Summary:	jdk

License:	GPL
Source0:	jdk-1.8.0.tar.gz

Requires:       rpm
AutoReqProv: no

%description
jdk


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*



%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/jdk_1.8.0
cp -a * $RPM_BUILD_ROOT/opt/jdk_1.8.0


%files
%defattr (-,root,root)
/*

%pre

%post
cat << EOF >> /etc/profile
JAVA_HOME=/opt/jdk_1.8.0
JRE_HOME=/opt/jdk_1.8.0/jre
PATH=\$PATH:\$JAVA_HOME/bin:\$JRE_HOME/bin
CLASSPATH=.:\$JAVA_HOME/lib/dt.jar:\$JAVA_HOME/lib/tools.jar:\$JRE_HOME/lib
export JAVA_HOME JRE_HOME PATH CLASSPATH
EOF
source /etc/profile

%changelog
