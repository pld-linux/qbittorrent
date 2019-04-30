#
# Conditional build:
%bcond_with	qsa		# system QtSingleApplication

%define		qtver	5.7
%define		rasterbar_ver	2:1.1.10
Summary:	qbittorrent - Qt-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt
Name:		qbittorrent
Version:	4.1.5
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.xz
# Source0-md5:	4650cc8bcf5149de2785b07a5ade7d2c
URL:		http://qbittorrent.sourceforge.net/
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
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtorrent-rasterbar-devel >= %{rasterbar_ver}
# not ready yet
BuildRequires:	libtorrent-rasterbar-devel < 2:1.2.0
BuildRequires:	pkgconfig >= 1:0.23
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
BuildRequires:	zlib >= 1.2.5.2
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

%if %{with qsa}
%{__rm} -r src/app/qtsingleapplication
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
%{_datadir}/appdata/qbittorrent.appdata.xml
%{_mandir}/man1/qbittorrent.1*
%{_iconsdir}/hicolor/*x*/apps/qbittorrent.png
%{_iconsdir}/hicolor/*x*/status/qbittorrent-tray.png
%{_iconsdir}/hicolor/scalable/status/qbittorrent-tray*.svg
%{_desktopdir}/qbittorrent.desktop
%{_pixmapsdir}/qbittorrent.png
