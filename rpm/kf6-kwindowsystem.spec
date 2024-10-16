%global kf_version 6.6.0

Name:    kf6-kwindowsystem
Version: 6.6.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 1 integration module with classes for windows management

License: LGPLv2+ and MIT
URL:     https://invent.kde.org/frameworks/kwindowsystem

Source0: %{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: kf6-extra-cmake-modules >= %{kf_version}
BuildRequires: kf6-rpm-macros >= %{kf_version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qttools-devel
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6WaylandClient)
BuildRequires: kf6-plasma-wayland-protocols-devel

BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-egl)

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Development Documentation files for %{name}
BuildArch:      noarch
%description    doc


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6 \
    -DKWINDOWSYSTEM_X11=OFF
%cmake_build

%install
%cmake_install

%find_lang_kf6 kwindowsystem6_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kwindowsystem.*
%{_kf6_libdir}/libKF6WindowSystem.so.*
%{_kf6_qmldir}/org/kde/kwindowsystem/
%{_kf6_plugindir}/kwindowsystem/

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/pkgconfig/KF6WindowSystem.pc
%{_kf6_libdir}/cmake/KF6WindowSystem/
%{_qt6_docdir}/KF6WindowSystem.tags

%files doc
%{_qt6_docdir}/KF6WindowSystem.qch

