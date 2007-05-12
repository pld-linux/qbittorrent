Summary:	qbittorrent - Qt4-based torrent client
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt4
Name:		qbittorrent
Version:	0.9.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ee5a0ee8677d09569355195f8b2e55a9
Patch0:		%{name}-desktop.patch
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:  curl-devel
BuildRequires:  boost-devel
BuildRequires:  boost-date_time-devel
BuildRequires:  boost-filesystem-devel
BuildRequires:  rb_libtorrent-devel >= 0.12
Requires:	python >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qTorrent - Qt4-based torrent client.

%description -l pl.UTF-8
qTorrent - graficzny klient torrenta oparty na Qt4.

%prep
%setup -q
%patch0 -p0

%build
./configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/{128x128/apps,16x16/apps,192x192/apps,22x22/apps,24x24/apps,32x32/apps,36x36/apps,48x48/apps,64x64/apps,72x72/apps,96x96/apps}

install src/qbittorrent 		$RPM_BUILD_ROOT%{_bindir}
install doc/*  				$RPM_BUILD_ROOT%{_mandir}/man1
install src/Icons/qBittorrent.desktop	$RPM_BUILD_ROOT%{_desktopdir}
install src/menuicons/128x128/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/128x128/apps
install src/menuicons/16x16/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/16x16/apps
install src/menuicons/192x192/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/192x192/apps
install src/menuicons/22x22/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/22x22/apps
install src/menuicons/24x24/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/24x24/apps
install src/menuicons/32x32/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/32x32/apps
install src/menuicons/36x36/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/36x36/apps
install src/menuicons/48x48/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/48x48/apps
install src/menuicons/64x64/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/64x64/apps
install src/menuicons/72x72/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/72x72/apps
install src/menuicons/96x96/apps/*	$RPM_BUILD_ROOT%{_pixmapsdir}/96x96/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_desktopdir}/qBittorrent.desktop
