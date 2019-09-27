Name:		python
Version:	3.6.3
Release:	el7
Summary:	python

License:	GPL
Source0:	python-3.6.3.tar.gz
BuildRequires:	gcc,make	
AutoReqProv: no
%description
python


%prep
%setup -q



%build
./configure --prefix=/opt/python_3.6.3
make -j8
make install DESTDIR=%{buildroot}



%files
%defattr (-,root,root)
/*

%pre

%post
ln -s  /opt/python_3.6.3/bin/python3 /usr/bin/python3
ln -s  /opt/python_3.6.3/bin/pip3 /usr/bin/pip3

%postun
rm -rf /usr/bin/python3
rm -rf /usr/bin/pip3

%changelog
