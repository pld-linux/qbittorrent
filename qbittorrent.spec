#
# Conditional build:
%bcond_without	qsa		# build with bundled QtSingleApplication

%define		qtver	4.5
Summary:	qbittorrent - Qt4-based torrent client
Summary(hu.UTF-8):	qbittorrent - Qt4-alapú torrent kliens
Summary(pl.UTF-8):	qbittorrent - graficzny klient torrenta oparty na Qt4
Name:		qbittorrent
Version:	3.0.10
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/qbittorrent/%{name}-%{version}.tar.gz
# Source0-md5:	f13c9416524fce8297b41caeadb04f1e
Patch0:		lang-hu-2.3.0.patch
Patch1:		cxx.patch
URL:		http://qbittorrent.sourceforge.net/
BuildRequires:	GeoIP-devel
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
%{?with_qsa:BuildRequires:	QtSingleApplication-devel >= 2.6-5}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libtorrent-rasterbar-devel >= 1:0.15.9
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	which
Requires:	desktop-file-utils
Requires:	libtorrent-rasterbar >= 1:0.15.9
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
%patch1 -p1

%if %{with qsa}
%{__rm} -r src/qtsingleapp
%endif

%build
# NOTE: not autoconf based configure
./configure \
	--prefix=%{_prefix} \
	%{?with_qsa:--with-qtsingleapplication=system}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS TODO Changelog
%attr(755,root,root) %{_bindir}/qbittorrent
%{_mandir}/man1/qbittorrent.1*
%{_iconsdir}/hicolor/*/apps/qbittorrent.png
%{_desktopdir}/qBittorrent.desktop
%{_pixmapsdir}/qbittorrent.png
