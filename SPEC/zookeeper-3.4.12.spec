Name:		zookeeper
Version:	3.4.12
Release:	el7
Summary:	zookeeper

License:	GPL
Source0:	zookeeper-3.4.12.tar.gz
BuildRequires:	gcc,make	
Requires: jdk >= 1.8

%description
zookeeper


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*



%build
mkdir -p $RPM_BUILD_ROOT/opt/zookeeper-3.4.12
cp -a * $RPM_BUILD_ROOT/opt/zookeeper-3.4.12




%files
%defattr (-,root,root)
/*

%pre
rm -rf /etc/rc.d/init.d/zookeeper

%post
cat << EOF >> /etc/profile
export ZOOKEEPER_HOME=/opt/zookeeper-3.4.12
export PATH=\$ZOOKEEPER_HOME/bin:\$PATH
export PATH
EOF
source /etc/profile

cp /opt/zookeeper-3.4.12/src/packages/rpm/init.d/zookeeper /etc/rc.d/init.d/zookeeper
chkconfig --add zookeeper
chkconfig zookeeper on

%changelog
