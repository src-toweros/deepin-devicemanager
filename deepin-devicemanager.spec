Name:           deepin-devicemanager
Version:        5.5.9.36
Release:        1
Summary:        Device Manager is a handy tool for viewing hardware information and managing the devices
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-devicemanager
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires:  dtkcore-devel
BuildRequires: dtkwidget-devel
BuildRequires: systemd-devel
BuildRequires: libicu-devel
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: cups-devel
BuildRequires: pkgconfig(dframeworkdbus)


Requires: smartmontools
Requires: dmidecode
Requires: xorg-x11-server-utils
Requires: hwinfo
Requires: cups
Requires: upower
Requires: deepin-shortcut-viewer
Requires: lshw
Requires: util-linux

%description
%{summary}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")

mkdir build && pushd build
%cmake ../ -DCMAKE_BUILD_TYPE=Release -DAPP_VERSION=%{version} -DVERSION=%{version}
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-authenticateProxy
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/*.policy

%changelog
* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.5.9.36-1
- Update 5.5.9.36

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.5.4.4-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.4.4-1
- Package init

