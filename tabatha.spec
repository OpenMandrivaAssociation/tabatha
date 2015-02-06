%define name 	tabatha
%define version 0.6
%define release 6

Summary: 	Push-button menu for system commands
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://groundstate.ca/tabatha/
License: 	GPL
Group: 		System/Configuration/Other
Source: 	%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildArch:	noarch
Requires:	usermode-consoleonly

%description
Tabatha is a GTK2 popup menu for tablet PCs, handhelds, and other frequently
changed desktops. It can be called with a single keypress, and allows system
configurations (power, X display, networking, etc.) to be changed with a
single button push. New buttons are easily configured through a simple XML
file, with no programming necessary.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%_bindir,%_sbindir,%_datadir}
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/tabatha
Name=Tabatha
Comment=Quick-configure menu
Icon=configuration_section
Categories=Settings;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README 
%_bindir/%name
%_sbindir/%name
%_datadir/%name
%{_datadir}/applications/mandriva-%name.desktop



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6-5mdv2010.0
+ Revision: 434265
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6-4mdv2009.0
+ Revision: 261342
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6-3mdv2009.0
+ Revision: 254070
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.6-1mdv2008.1
+ Revision: 135455
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import tabatha


* Mon Aug 16 2004 Austin Acton <austin@mandrake.org> 0.6-1mdk
- initial package
