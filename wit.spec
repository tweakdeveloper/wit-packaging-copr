%global forgeurl https://github.com/Wiimm/wiimms-iso-tools
%global commit e58ce7463bc8829c46bcba52e8232f550e49c17c
%global debug_package %{nil}

%forgemeta

Name:           wit
Version:        v3.04a
Release:        1%{?dist}
Summary:        Wiimms ISO Tool

License:        GPLv2+
URL:            https://wit.wiimm.de/

Source: %{forgesource}

Patch0: wit-v3.04a-makefile-no-sudo.patch
Patch1: wit-v3.04a-load-titles.patch

BuildRequires: gcc, gcc-c++, ncurses-devel 
#Requires:       

%description
Wiimms ISO Tools is a set of command line tools to manipulate Wii and GameCube 
ISO images and WBFS containers.

%prep
%forgesetup
%patch0 -p1
%patch1 -p1

%build
make INSTALL_PATH=%{?buildroot}/usr -C project %{?_smp_mflags} all
make INSTALL_PATH=%{?buildroot}/usr -C project doc

%install
make INSTALL_PATH=%{?buildroot}/usr -C project install

%files
%{_bindir}/wdf
%{_bindir}/wdf-cat
%{_bindir}/wdf-dump
%{_bindir}/wit
%{_bindir}/wwt
%{_datadir}/wit/load-titles.sh
%{_datadir}/wit/magic.txt
%{_datadir}/wit/system-menu.txt
%{_datadir}/wit/titles-de.txt
%{_datadir}/wit/titles-es.txt
%{_datadir}/wit/titles-fr.txt
%{_datadir}/wit/titles-it.txt
%{_datadir}/wit/titles-ja.txt
%{_datadir}/wit/titles-ko.txt
%{_datadir}/wit/titles-nl.txt
%{_datadir}/wit/titles-pt.txt
%{_datadir}/wit/titles-ru.txt
%{_datadir}/wit/titles-zhcn.txt
%{_datadir}/wit/titles-zhtw.txt
%{_datadir}/wit/titles.txt

%doc project/doc/*
%license project/gpl-2.0.txt

%changelog
* Tue Oct 05 2021 Nolan <tweakdeveloper@gmail.com> - v3.04a
- Initial version of package
