%define name 	tabatha
%define version 0.6
%define release %mkrel 3

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

