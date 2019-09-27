Name:		go
Version:	1.10.4
Release:	el7
Summary:	nodejs

License:	GPL
Source0:	go-1.10.4.tar.gz
#BuildRequires:	gcc,make
AutoReqProv: no

%description
go-1.10.4


%prep
%setup -q
rm -rf $RPM_BUILD_ROOT/*



%build


%install
mkdir -p $RPM_BUILD_ROOT/opt/go-1.10.4
cp -a * $RPM_BUILD_ROOT/opt/go-1.10.4



%files
%defattr (-,root,root)
/*

%post
ln -s  /opt/go-1.10.4/bin/* /usr/bin

%changelog
