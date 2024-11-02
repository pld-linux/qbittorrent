%define		qtver	6.5.0
%define		rasterbar_ver	2:2.0.10
Summary:	qbittorrent - Qt-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt
Name:		qbittorrent
Version:	5.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.xz
# Source0-md5:	2f2cf3ada13a3ee761b74051302809a6
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	GeoIP-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	boost-devel >= 1.76
BuildRequires:	cmake >= 3.16
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libtorrent-rasterbar-devel >= %{rasterbar_ver}
BuildRequires:	openssl-devel >= 3.0.2
BuildRequires:	pkgconfig >= 1:0.23
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	qt6-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xz
BuildRequires:	zlib >= 1.2.11
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6Sql >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
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
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/metainfo/org.qbittorrent.qBittorrent.metainfo.xml
%{_mandir}/man1/qbittorrent.1*
%lang(ru) %{_mandir}/ru/man1/qbittorrent.1*
%{_desktopdir}/org.qbittorrent.qBittorrent.desktop
%{_iconsdir}/hicolor/*x*/apps/qbittorrent.png
%{_iconsdir}/hicolor/*x*/status/qbittorrent-tray.png
%{_iconsdir}/hicolor/scalable/apps/qbittorrent.svg
%{_iconsdir}/hicolor/scalable/status/qbittorrent-tray*.svg
