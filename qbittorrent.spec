%define		qtver	5.15.2
%define		rasterbar_ver	2:2.0.9
Summary:	qbittorrent - Qt-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt
Name:		qbittorrent
Version:	4.6.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.xz
# Source0-md5:	ffc528cbdf1ab4ff40a51753e5e9b030
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	GeoIP-devel
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	boost-devel >= 1.71
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtorrent-rasterbar-devel >= %{rasterbar_ver}
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pkgconfig >= 1:0.23
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
BuildRequires:	zlib >= 1.2.11
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libtorrent-rasterbar >= %{rasterbar_ver}
Requires:	python3 >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qTorrent - Qt-based torrent client.

%description -l hu.UTF-8
qBittorrent - Qt-alapú torrent kliens

%description -l pl.UTF-8
qTorrent - graficzny klient torrenta oparty na Qt.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure \
	--verbose \
	--prefix=%{_prefix} \
	--with-boost-libdir=%{_libdir}

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
%doc AUTHORS Changelog
%attr(755,root,root) %{_bindir}/qbittorrent
%{_datadir}/metainfo/org.qbittorrent.qBittorrent.appdata.xml
%{_mandir}/man1/qbittorrent.1*
%{_desktopdir}/org.qbittorrent.qBittorrent.desktop
%{_iconsdir}/hicolor/*x*/apps/qbittorrent.png
%{_iconsdir}/hicolor/*x*/status/qbittorrent-tray.png
%{_iconsdir}/hicolor/scalable/apps/qbittorrent.svg
%{_iconsdir}/hicolor/scalable/status/qbittorrent-tray*.svg
