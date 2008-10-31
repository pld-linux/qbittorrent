# TODO: - fix build problem (under working - uzsolt)
Summary:	qbittorrent - Qt4-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt4-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt4
Name:		qbittorrent
Version:	1.2.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qbittorrent/%{name}-%{version}.tar.gz
# Source0-md5:	497dd5629d608e52cd5184dfb22c1701
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	boost-asio
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	curl-devel
BuildRequires:	libtorrent-rasterbar-devel >= 0.13.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
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

%build
./configure \
	--prefix=%{_prefix}
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
%{_mandir}/man1/*
%{_iconsdir}/hicolor/*/apps/*
%{_desktopdir}/qBittorrent.desktop
