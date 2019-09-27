Name:           ssr
Version:        1.0
Release:        1%{?dist}
Summary:        this is ssr1.0
 
License:        GPL
URL:            http://www.yehe.info
Source0:        %{name}-%{version}.tar.gz

Requires:       rpm epel-release


%description


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*

%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/ssr
cp -a * $RPM_BUILD_ROOT/opt/ssr


%files
%defattr(-,root,root)
/*

%post
cp /opt/ssr/etc/shadowsocks.json /etc/shadowsocks.json
cp /opt/ssr/etc/ssr /etc/init.d/ssr
chmod a+x /etc/init.d/ssr
systemctl enable ssr
systemctl start ssr

%changelog
