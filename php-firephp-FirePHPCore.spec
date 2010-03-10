%include	/usr/lib/rpm/macros.php
%define		_pearname	FirePHPCore
%define		php_min_version 5.2.0
Summary:	Firebug Extension for AJAX Development
Name:		php-firephp
Version:	0.3.1
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
URL:		http://www.firephp.org/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:%{php_min_version}
Source0:	http://pear.firephp.org/get/FirePHPCore-%{version}.tgz
# Source0-md5:	08acc816fc843eea32f825479824662c
Requires:	php-mbstring
Requires:	php-pcre
Requires:	php-pear >= 4:1.2-2
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FirePHP enables you to print to your Firebug Console using a simple
PHP function call.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# Good bye php4
rm -f $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}/*.php4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/.registry/.channel.pear.firephp.org/firephpcore.reg
%{php_pear_dir}/%{_pearname}/FirePHP.class.php
%{php_pear_dir}/%{_pearname}/fb.php
