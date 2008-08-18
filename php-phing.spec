Summary:	PHP project build system based on Apache Ant
Summary(pl.UTF-8):	System budowania projektów w PHP oparty na narzędziu Apache Ant
Name:		phing
Version:	2.3.0
Release:	0.7
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://phing.tigris.org/files/documents/995/40189/%{name}-%{version}.zip
# Source0-md5:	7a986d9f24a2b8d6c4574d66545ce174
Source1:	%{name}.sh
URL:		http://www.phing.info/
BuildRequires:	sed >= 4.0
Requires:	/usr/bin/php
Requires:	php-common >= 4:5.0.2
Requires:	php-dom
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/%{name}

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

%description -l pl.UTF-8
PHing Is Not GNU make (phing to nie GNU make) to system budowania
projektów oparty na narzędziu Apache Ant. Pozwala robić wszystko to,
co da się zrobić przy użyciu tradycyjnego systemu budowania takiego
jak GNU make i wykorzystuje proste pliki reguł XML oraz rozszerzalne
klasy PHP "zadań", co czyni z niego łatwe w użyciu i elastyczne
środowisko. Możliwości obejmują przekształcenia (np. podstawienia
tokenów, przekształcenia XSLT, przekształcenia szablonów Smarty),
operacje na systemie plików, obsługę interaktywnego budowania,
wywoływanie SQL-a, operacje na CVS-ie, narzędzia do tworzenia pakietów
PEAR i wiele więcej.

%prep
%setup -q
%{__sed} -i -e 's,@DATA-DIR@,%{_appdir}/data,g' classes/phing/Phing.php
find -name '*.php' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}/data/phing/{listener,tasks,types}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/phing
cp -a bin/phing.php $RPM_BUILD_ROOT%{php_data_dir}
cp -a classes/phing/* $RPM_BUILD_ROOT%{_appdir}
cp -a etc $RPM_BUILD_ROOT%{_appdir}/data/phing
mv $RPM_BUILD_ROOT{%{_appdir},%{_appdir}/data/phing}/listener/defaults.properties
mv $RPM_BUILD_ROOT{%{_appdir},%{_appdir}/data/phing}/tasks/defaults.properties
mv $RPM_BUILD_ROOT{%{_appdir},%{_appdir}/data/phing}/types/defaults.properties

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a docs/example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS
%attr(755,root,root) %{_bindir}/phing
%{php_data_dir}/phing.php
%{_appdir}
%{_examplesdir}/%{name}-%{version}
