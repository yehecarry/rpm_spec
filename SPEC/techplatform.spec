Name:           techplatform
Version:        1.0
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
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d/
cp -a * $RPM_BUILD_ROOT/etc/yum.repos.d/
%post


%files
%defattr(-,root,root)
/*

%changelog
