# TODO
# - subpackages for tasks with external dependencies, or rather suggests?
%define		pkgname		phing
%define		pearname	%{pkgname}
%define		php_min_version 5.0.2
#%%include	/usr/lib/rpm/macros.php
Summary:	PHP project build system based on Apache Ant
Summary(pl.UTF-8):	System budowania projektów w PHP oparty na narzędziu Apache Ant
Name:		php-%{pkgname}
Version:	2.4.12
Release:	2
License:	LGPL v3
Group:		Development/Languages/PHP
Source0:	http://pear.phing.info/get/phing-%{version}.tgz
# Source0-md5:	6ccb862bc8a97b2c505f64c83c7a1371
Source1:	%{pkgname}.sh
URL:		http://www.phing.info/
BuildRequires:	php-channel(pear.phing.info)
BuildRequires:	php-pear >= 4:1.3.8
BuildRequires:	php-pear-PEAR >= 1:1.8.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	/usr/bin/php
Requires:	php(dom)
Requires:	php(xml)
Requires:	php-channel(pear.phing.info)
Requires:	php-common >= 4:%{php_min_version}
Suggests:	jsl
Suggests:	php-docblox-DocBlox
Suggests:	php-pdepend-PHP_Depend
Suggests:	php-pear-Archive_Tar
Suggests:	php-pear-HTTP_Request2
Suggests:	php-pear-PEAR_PackageFileManager
Suggests:	php-pear-PHP_CodeSniffer
Suggests:	php-pear-PhpDocumentor
Suggests:	php-pear-Services_Amazon_S3
Suggests:	php-pear-VersionControl_Git
Suggests:	php-pear-VersionControl_SVN
Suggests:	php-pecl-xdebug
Suggests:	php-phing-phingdocs
Suggests:	php-phpmd-PHP_PMD
Suggests:	php-phpunit-PHPUnit >= 3.6
Suggests:	php-phpunit-PHP_CodeCoverage
Suggests:	php-phpunit-phpcpd
Provides:	phing = %{version}
Obsoletes:	phing < 2.4.1
Conflicts:	php-phpunit-PHPUnit < 3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{php_data_dir}/%{pkgname}

# exclude optional dependencies
%define		_noautoreq	pear(creole/Creole.php) pear(phing/.*) pear(Smarty.class.php) pear(phpDocumentor/Setup.inc.php) pear(simpletest/.*) pear(Archive/Tar.*) pear(HTTP/Request2.*) pear(PEAR/PackageFileManager.*) pear(PhpDocumentor.*) pear(Services/Amazon/S3.*) pear(VersionControl/Git.*) pear(VersionControl/SVN.*) pear(PHP/CodeSniffer.*)

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

# 2.4.4 release tarball contains .rej and .orig files junk
find '(' -name '*~' -o -name '*.orig' -o -name '*.rej' ')' -print0 | xargs -0 -r -l512 rm -f

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

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc optional-packages.txt
%attr(755,root,root) %{_bindir}/phing
%{php_pear_dir}/.registry/.channel.*/phing.reg
%{php_data_dir}/phing.php
%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/contrib
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
