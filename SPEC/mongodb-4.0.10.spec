Name:           mongodb
Version:        4.0.10
Release:        1%{?dist}
Summary:        this is mongodb4.0.10
 
License:        GPL
URL:            http://www.yehe.info
Source0:        %{name}-%{version}.tar.gz

Requires:       rpm


%description


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*

%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/mongodb-4.0.10
cp -a * $RPM_BUILD_ROOT/opt/mongodb-4.0.10


%files
%defattr(-,root,root)
/*

%post
ln -s /opt/mongodb-4.0.10/script/mongodb-4.0.10.service /lib/systemd/system
systemctl enable mongodb-4.0.10
systemctl restart mongodb-4.0.10
ln -s /opt/mongodb-4.0.10/bin/mongod /usr/bin/
ln -s /opt/mongodb-4.0.10/bin/mongo /usr/bin/
ln -s /opt/mongodb-4.0.10/bin/mongos /usr/bin/
ln -s /opt/mongodb-4.0.10/bin/mongodump /usr/bin/
ln -s /opt/mongodb-4.0.10/bin/mongorestore /usr/bin/
%preun
systemctl stop  mongodb-4.0.10
%postun
rm -rf /lib/systemd/system/mongodb-4.0.10.service
rm -rf /usr/bin/mongod
rm -rf /usr/bin/mongo
rm -rf /usr/bin/mongos
rm -rf /usr/bin/mongodump
rm -rf /usr/bin/mongorestore
%changelog
