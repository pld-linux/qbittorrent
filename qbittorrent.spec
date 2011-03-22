Summary:	qbittorrent - Qt4-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt4-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt4
Name:		qbittorrent
Version:	2.7.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.gz
# Source0-md5:	98e4048fc832dc2f9a840336fb679a34
Patch0:		lang-hu-2.3.0.patch
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	GeoIP-devel
BuildRequires:	QtCore-devel >= 4.4.0
BuildRequires:	QtDBus-devel >= 4.4.0
BuildRequires:	QtGui-devel >= 4.4.0
BuildRequires:	QtNetwork-devel >= 4.4.0
BuildRequires:	QtXml-devel >= 4.4.0
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	libtorrent-rasterbar-devel >= 1:0.15.5
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.4.0
BuildRequires:	qt4-qmake >= 4.4.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
Requires:	libtorrent-rasterbar >= 1:0.15.5
Requires:	python >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qTorrent - Qt4-based torrent client.

%description -l hu.UTF-8
qBittorrent - Qt4-alapú torrent kliens

%description -l pl.UTF-8
qTorrent - graficzny klient torrenta oparty na Qt4.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{128x128/apps,16x16/apps,192x192/apps,22x22/apps,24x24/apps,32x32/apps,36x36/apps,48x48/apps,64x64/apps,72x72/apps,96x96/apps}

install src/qbittorrent 		$RPM_BUILD_ROOT%{_bindir}
install doc/*  				$RPM_BUILD_ROOT%{_mandir}/man1
install src/Icons/qBittorrent.desktop	$RPM_BUILD_ROOT%{_desktopdir}
install src/menuicons/16x16/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps
install src/menuicons/22x22/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps
install src/menuicons/24x24/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/apps
install src/menuicons/32x32/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps
install src/menuicons/36x36/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/36x36/apps
install src/menuicons/48x48/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps
install src/menuicons/64x64/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps
install src/menuicons/72x72/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/72x72/apps
install src/menuicons/96x96/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/96x96/apps
install src/menuicons/128x128/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps
install src/menuicons/192x192/apps/*	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/192x192/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{_iconsdir}/hicolor/*/apps/*
%{_desktopdir}/qBittorrent.desktop
