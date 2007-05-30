Summary:	PHP project build system based on Apache Ant
Name:		phing
Version:	2.2.0
Release:	0.2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://phing.tigris.org/files/documents/995/33811/%{name}-%{version}.tar.gz
# Source0-md5:	db69fb31b4224501f3508fd6d8c45b10
URL:		http://phing.info/
Requires:	/usr/bin/phing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
PHing Is Not GNU make; it's a project build system based on Apache
Ant. You can do anything with it that you could do with a traditional
build system like GNU make, and its use of simple XML build files and
extensible PHP "task" classes make it an easy-to-use and highly
flexible build framework. Features include file transformations (e.g.
token replacement, XSLT transformation, Smarty template
transformations), file system operations, interactive build support,
SQL execution, CVS operations, tools for creating PEAR packages, and
much more.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir}/bin,%{_bindir}}
cp -a classes $RPM_BUILD_ROOT%{_appdir}
install bin/phing $RPM_BUILD_ROOT%{_appdir}/bin
cp -a bin/phing.php $RPM_BUILD_ROOT%{_appdir}/bin
ln -s %{_appdir}/bin/phing $RPM_BUILD_ROOT%{_bindir}/phing

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README TODO
%attr(755,root,root) %{_bindir}/phing
%dir %{_appdir}
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/phing
%{_appdir}/bin/phing.php
%{_appdir}/classes
