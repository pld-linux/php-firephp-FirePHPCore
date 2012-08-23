%include	/usr/lib/rpm/macros.php
%define		_pearname	FirePHPCore
%define		php_min_version 5.2.0
Summary:	Firebug Extension for AJAX Development
Name:		php-firephp-%{_pearname}
Version:	0.3.2
Release:	3
License:	New BSD License
Group:		Development/Languages/PHP
URL:		http://www.firephp.org/
BuildRequires:	php-channel(pear.firephp.org)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= %{php_min_version}
Source0:	http://pear.firephp.org/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2850c4a9a976337e14c29c4f4d48b483
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-channel(pear.firephp.org)
Requires:	php-pear >= 4:1.2-2
Obsoletes:	php-firephp < 0.3.2
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
%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}/*.php4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/.registry/.channel.pear.firephp.org/firephpcore.reg
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/%{_pearname}/FirePHP.class.php
%{php_pear_dir}/%{_pearname}/fb.php
