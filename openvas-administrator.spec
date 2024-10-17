Summary: 	Provide a unified access for various administrative tasks
Name:		openvas-administrator
Version:	1.1.2
Release:	3
Source0:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
source1:	.abf.yml
Group:		System/Configuration/Networking
Url:		https://www.openvas.org
License:	GPLv2+
BuildRequires:	cmake
BuildRequires:	openvas-devel
buildrequires:	xmltoman

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
export LDFLAGS="-lglib-2.0"
%cmake
%make

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/openvasad_log.conf
%{_sbindir}/openvasad
%{_mandir}/man8/openvasad.8.*
%attr(644,root,root) %{_datadir}/openvas/openvasad/global_schema_formats/*/*


%changelog
* Thu Sep 08 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 699042
- backport fixes

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 1.1.1-1
+ Revision: 649815
- import openvas-administrator

