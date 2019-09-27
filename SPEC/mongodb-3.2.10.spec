Name:           mongodb
Version:        3.2.10
Release:        1%{?dist}
Summary:        this is mongodb3.2.10
 
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
mkdir -p $RPM_BUILD_ROOT/opt/mongodb-3.2.10
cp -a * $RPM_BUILD_ROOT/opt/mongodb-3.2.10


%files
%defattr(-,root,root)
/*

%post
ln -s /opt/mongodb-3.2.10/script/mongodb.service /lib/systemd/system
systemctl enable mongodb
systemctl restart mongodb
ln -s /opt/mongodb-3.2.10/bin/* /usr/bin/

%changelog
