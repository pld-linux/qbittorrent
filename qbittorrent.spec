# Conditional build
%bcond_without	gui	# do not build gui frontend

%define		qtver	6.5.0
%define		rasterbar_ver	2:2.0.10
Summary:	qbittorrent - Qt-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt
Name:		qbittorrent
Version:	5.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.xz
# Source0-md5:	776ed6a661f8217700bbf292afca5650
URL:		https://www.qbittorrent.org/
BuildRequires:	GeoIP-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
%if %{with gui}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
%endif
BuildRequires:	boost-devel >= 1.76
BuildRequires:	cmake >= 3.16
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
%if %{with gui}
Requires:	Qt6Widgets >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
%endif
Requires:	libtorrent-rasterbar >= %{rasterbar_ver}
Requires:	python3 >= 1:3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qTorrent - Qt-based torrent client.

%description -l hu.UTF-8
qBittorrent - Qt-alapú torrent kliens

%description -l pl.UTF-8
qTorrent - graficzny klient torrenta oparty na Qt.

%package nox
Summary:	A Headless Bittorrent Client
Group:		Applications/Networking

%description nox
A Headless Bittorrent Client with a Web UI allowing users to remotely
control the client.

%prep
%setup -q

%build
%if %{with gui}
%cmake -B build
%{__make} -C build
%endif

%cmake -B build-nox -D GUI=OFF
%{__make} -C build-nox

%install
rm -rf $RPM_BUILD_ROOT
%if %{with gui}
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build-nox install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%if %{with gui}
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
%endif

%files nox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qbittorrent-nox
%{_datadir}/metainfo/org.qbittorrent.qBittorrent-nox.metainfo.xml
%{_mandir}/man1/qbittorrent-nox.1*
%lang(ru) %{_mandir}/ru/man1/qbittorrent-nox.1*
