Name:          forever
Version:       0.10.1
Release:       1%{?dist}
Summary:       A simple CLI tool for ensuring that a given script runs continuously (i.e. forever).
Packager:      Laurent Eschenauer <laurent.eschenauer@comodit.com>
Group:         Development/Libraries
License:       MIT License
URL:           https://github.com/nodejitsu/forever
Source0:       %{url}/tarball/v%{version}
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-tmp
Provides:      forever
Requires:      nodejs
BuildRequires: nodejs
BuildRequires: npm

%description
A simple CLI tool for ensuring that a given script runs continuously (i.e. forever)

%prep
%setup -c -q -n %{name}-%{version}

%build
cd nodejitsu-forever*
npm install

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_prefix}/lib/node_modules/forever
%{__cp} -r nodejitsu-forever*/* $RPM_BUILD_ROOT%{_prefix}/lib/node_modules/forever/

%post
ln -sf %{_prefix}/lib/node_modules/forever/bin/forever %{_bindir}/forever
ln -sf %{_prefix}/lib/node_modules/forever/bin/foreverd %{_bindir}/foreverd

%postun
rm -f %{_bindir}/forever
rm -f %{_bindir}/foreverd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,-)
%{_prefix}/lib/node_modules/forever/*
%defattr(755,root,root,-)
%{_prefix}/lib/node_modules/forever/bin/*

%changelog
* Thu Oct 01 2012 Laurent Eschenauer <laurent.eschenauer@comodit.com> - 0.10.1
- Initial release.

