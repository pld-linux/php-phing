# TODO
# - subpackages for tasks with external dependencies
#%%include	/usr/lib/rpm/macros.php
%define		pkgname	phing
%define		_pearname	%{pkgname}
Summary:	PHP project build system based on Apache Ant
Summary(pl.UTF-8):	System budowania projektów w PHP oparty na narzędziu Apache Ant
Name:		php-%{pkgname}
Version:	2.4.1
Release:	2
License:	LGPL v3
Group:		Development/Languages/PHP
Source0:	http://pear.phing.info/get/phing-%{version}.tgz
# Source0-md5:	3cb7be9bc033dfe713d4ae4c62235d60
Source1:	%{pkgname}.sh
URL:		http://www.phing.info/
BuildRequires:	php-channel(pear.phing.info)
BuildRequires:	php-pear-PEAR >= 1:1.8.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.564
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	/usr/bin/php
Requires:	php-PHPUnit >= 3.4
Requires:	php-common >= 4:5.0.2
Requires:	php-dom
Requires:	php-xml
Provides:	phing = %{version}
Obsoletes:	phing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/%{pkgname}

%define		_noautopear pear(creole/Creole.php) pear(phing/.*) pear(Smarty.class.php) pear(phpDocumentor/Setup.inc.php) pear(simpletest/.*)

# these are all optional:
#Wed Mar 10 15:52:25 2010 php-pear-Archive_Tar-1.3.2-1.noarch
#Wed Mar 10 15:52:25 2010 php-pear-Console_Getopt-1.2.3-3.noarch
#Wed Mar 10 15:52:26 2010 php-pear-Structures_Graph-1.0.2-1.noarch
#Wed Mar 10 15:52:57 2010 php-pear-1.2-2.noarch
#Wed Mar 10 15:52:57 2010 php-pear-PEAR-1.7.2-10.noarch
#Wed Mar 10 15:52:57 2010 php-pear-PEAR-core-1.7.2-10.noarch
#Wed Mar 10 22:07:22 2010 php-pear-VersionControl_SVN-0.3.1-3.noarch
#Wed Mar 10 22:07:22 2010 php-pear-XML_Parser-1.3.2-1.noarch
#Wed Mar 10 22:07:23 2010 php-pear-Mail-1.1.14-3.noarch
#Wed Mar 10 22:07:23 2010 php-pear-PEAR_PackageFileManager-1.6.3-1.noarch
#Wed Mar 10 22:07:24 2010 php-pear-Benchmark-1.2.7-1.noarch
#Wed Mar 10 22:07:24 2010 php-pear-Log-1.11.3-1.noarch
#Wed Mar 10 22:07:25 2010 php-PHPUnit-3.3.14-2.noarch

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

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
%pear_package_setup -d data_dir=%{_appdir}/data

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir},%{_appdir}}
%pear_package_install

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/phing

# cleanup the mess pear install made
mv $RPM_BUILD_ROOT{%{php_pear_dir}/%{pkgname}/*,%{_appdir}}
mv $RPM_BUILD_ROOT{%{php_pear_dir}/phing.php,%{php_data_dir}/phing.php}
cp -a ./%{php_data_dir}/* $RPM_BUILD_ROOT%{php_data_dir}

#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
#cp -a docs/example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc optional-packages.txt
%attr(755,root,root) %{_bindir}/phing
%{php_pear_dir}/.registry/.channel.*/phing.reg
%{php_data_dir}/phing.php
%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/filters
%{_appdir}/input
%{_appdir}/listener
%{_appdir}/mappers
%{_appdir}/parser
%{_appdir}/system
%{_appdir}/tasks
%{_appdir}/types
%{_appdir}/util

%dir %{_appdir}/lib
%{_appdir}/lib/Capsule.php

%{_appdir}/data

#%{_examplesdir}/%{name}-%{version}
