Name:		erlang
Version:	21.1
Release:	v1
Summary:	erlang

License:	GPL
Source0:	erlang-21.1.tar.gz
BuildRequires:	gcc,make

%description
erlang-21.1


%prep
%setup -q



%build
./configure --without-javac --without-odbc --with-ssl -enable-kernel-pool --prefix=/opt/erlang_21.1
make -j8
make install DESTDIR=%{buildroot}



%files
%defattr (-,root,root)
/*

%pre
rm -rf /usr/bin/erl
rm -rf /usr/bin/escript


%post
ln -s  /opt/erlang_21.1/lib/erlang/bin/erl /usr/bin/erl
ln -s  /opt/erlang_21.1/lib/erlang/bin/escript /usr/bin/escript

%changelog
