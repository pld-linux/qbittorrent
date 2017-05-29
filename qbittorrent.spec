#
# Conditional build:
%bcond_with	qsa		# build with bundled QtSingleApplication

%define		qtver	5.7
%define		rasterbar_ver	2:1.0.11
Summary:	qbittorrent - Qt-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt
Name:		qbittorrent
Version:	3.3.11
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.xz
# Source0-md5:	c0b23cc43bb99cf2bf51a2e4d4f6d926
Patch1:		qmake.patch
URL:		http://qbittorrent.sourceforge.net/
BuildConflicts:	libtorrent-rasterbar >= 2:1.1
BuildRequires:	GeoIP-devel
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
%{?with_qsa:BuildRequires:	Qt5SingleApplication-devel >= 2.6.1-4}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtorrent-rasterbar-devel >= %{rasterbar_ver}
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libtorrent-rasterbar >= %{rasterbar_ver}
Requires:	python >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qTorrent - Qt-based torrent client.

%description -l hu.UTF-8
qBittorrent - Qt-alapú torrent kliens

%description -l pl.UTF-8
qTorrent - graficzny klient torrenta oparty na Qt.

%prep
%setup -q
%patch1 -p1

%if %{with qsa}
#%{__rm} -r src/qtsingleapp
%endif

%build
%{__aclocal}
%{__autoconf}
%configure \
	--verbose \
	--prefix=%{_prefix} \
	--with-boost-libdir=%{_libdir} \
	%{?with_qsa:--with-qtsingleapplication=system}

%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS TODO Changelog
%attr(755,root,root) %{_bindir}/qbittorrent
%{_datadir}/appdata/qBittorrent.appdata.xml
%{_mandir}/man1/qbittorrent.1*
%{_iconsdir}/hicolor/*/apps/qbittorrent.png
%{_iconsdir}/hicolor/*x*/status/qbittorrent-tray.png
%{_desktopdir}/qBittorrent.desktop
%{_pixmapsdir}/qbittorrent.png
