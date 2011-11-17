Summary: 	Provide a unified access for various administrative tasks
Name:		openvas-administrator
Version:	1.1.2
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://www.openvas.org
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The mission of OpenVAS Administrator is to provide a unified access
for various administrative tasks such as creating and configuring
scan user accounts. 

The Administrator can be used in two ways: As a command line tool for
direct changes on the respective system and as a remote service.

%prep
%setup -q -n %name-%version

sed -i -e 's#-Werror##' CMakeLists.txt

%build
%cmake
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/openvasad_log.conf
%{_sbindir}/openvasad
%{_mandir}/man8/openvasad.8.*
%{_datadir}/openvas/openvasad
