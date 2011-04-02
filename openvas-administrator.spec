Summary: 	Provide a unified access for various administrative tasks
Name:		openvas-administrator
Version:	1.1.1
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Patch0:		openvas-administrator-1.1.1-build.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0

%description
The mission of OpenVAS Administrator is to provide a unified access
for various administrative tasks such as creating and configuring
scan user accounts. 

The Administrator can be used in two ways: As a command line tool for
direct changes on the respective system and as a remote service.

%prep
%setup -q -n %name-%version
%patch0 -p0

sed -i -e 's#-Werror##' CMakeLists.txt

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/openvasad_log.conf
%{_sbindir}/openvasad
%{_mandir}/man8/openvasad.8.xz
%{_datadir}/openvas/openvasad
