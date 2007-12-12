%define name 	tabatha
%define version 0.6
%define release 1mdk

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
(cd $RPM_BUILD_ROOT
mkdir -p ./%{_menudir}
cat > ./%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/tabatha"\
title="Tabatha"\
longtitle="Quick-configure menu"\
needs="x11"\
icon="configuration_section.png"\
section="System/Configuration/Other"
EOF
)

%post
%update_menus

%postun
%update_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README 
%_bindir/%name
%_sbindir/%name
%_datadir/%name
%_menudir/%name

