Name:		node	
Version:	v8.11.2
Release:	el7
Summary:	nodejs

License:	GPL
Source0:	node-v8.11.2.tar.gz
BuildRequires:	gcc,make	

%description
nodejs


%prep
%setup -q



%build
#./configure --prefix=$RPM_BUILD_ROOT/opt/nodejs-v8.11.2
./configure --prefix=/opt/nodejs_v8.11.2
make -j8

%install
#mkdir -p $RPM_BUILD_ROOT/opt/nodejs-v8.11.2
make install DESTDIR=%{buildroot}



%files
%defattr (-,root,root)
/*

%post
ln -s  /opt/nodejs_v8.11.2/bin/* /usr/bin

%changelog
