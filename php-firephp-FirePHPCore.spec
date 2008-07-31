Summary:	Firebug Extension for AJAX Development
Name:		php-firephp
Version:	0.1.1
Release:	0.2
License:	New BSD License
Group:		Development/Languages/PHP
URL:		http://www.firephp.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	php-common >= 4:5.0
Source0:	http://www.firephp.org/DownloadRelease/FirePHPLibrary-FirePHPCore-%{version}
# Source0-md5:	f11b9e4d9cfbc204699aeeb81547e193
Patch0:		php-firephp.patch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FirePHP enables you to print to your Firebug Console using a simple
PHP function call.

%prep
%setup -qc
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a demo/*.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a lib/FirePHPCore/*.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{php_data_dir}/FirePHP.class.php
%{php_data_dir}/fb.php

%{_examplesdir}/%{name}-%{version}
