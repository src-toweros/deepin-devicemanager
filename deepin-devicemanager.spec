%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif
Name:           deepin-devicemanager
Version:        5.5.4.4
Release:        2
Summary:        Device Manager is a handy tool for viewing hardware information and managing the devices.
License:        GPLv3+
URL:            https://uos-packages.deepin.com/uos/pool/main/d/deepin-devicemanager/
Source0:        %{name}-%{version}.orig.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  cups-devel

%description
Device Manager is a handy tool for viewing hardware information and managing the devices.


%prep
%autosetup

%build
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd


%files
%{_bindir}/deepin-devicemanager
%{_bindir}/deepin-devicemanager-authenticateProxy
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/deepin-devicemanager.svg
%{_datadir}/polkit-1/actions/com.deepin.pkexec.deepin-devicemanager-authenticateProxy.policy
%license LICENSE
%doc README.md

%changelog
* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.5.4.4-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.5.4.4-1
- Package init
