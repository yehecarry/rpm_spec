Name:		erlang
Version:	20.3
Release:	v1
Summary:	erlang

License:	GPL
Source0:	erlang-20.3.tar.gz
BuildRequires:	gcc,make	

%description
erlang-20.3


%prep
%setup -q



%build
./configure --without-javac --without-odbc --with-ssl -enable-kernel-pool --prefix=/opt/erlang_20.3
make -j8
make install DESTDIR=%{buildroot}
cp %{_topdir}/SOURCES/file/rebar $RPM_BUILD_ROOT/opt/erlang_20.3/lib/erlang/bin/rebar



%files
%defattr (-,root,root)
/*

%pre
rm -rf /usr/bin/erl
rm -rf /usr/bin/escript
rm -rf /usr/bin/rebar

%post
ln -s /opt/erlang_20.3/lib/erlang/bin/erl /usr/bin/erl
ln -s /opt/erlang_20.3/lib/erlang/bin/escript /usr/bin/escript
ln -s /opt/erlang_20.3/lib/erlang/bin/rebar /usr/bin/rebar

%changelog
