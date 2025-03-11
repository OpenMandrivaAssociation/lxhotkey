# git snapshot
#global snapshot 1
%if 0%{?snapshot}
	%global commit		09bfd852313635006cae7aab0c2cb2a76eab0b0b
	%global commitdate	20240817
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	A lightweight global keyboard shortcuts configurator
Name:		lxhotkey
Version:	0.1.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/lxhotkey/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(libfm)
BuildRequires:  pkgconfig(libfm-extra)

%description
Lightweight global keyboard shortcuts configurator.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}/gtk.so
%{_libdir}/%{name}/ob.so
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.1.*

#---------------------------------------------------------------------------

%package devel
Summary:	%{name} developement files
Group:		Graphical desktop/Other
Provides:	%{name}-devel = %{version}-%{release}

%description devel
This package contains header files needed when building applications based on
%{name}.

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	-with-gtk=3 \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name}

desktop-file-install \
	--delete-original \
	--remove-key=NotShowIn \
	--add-only-show-in=LXDE \
	--set-icon=preferences-desktop-keyboard \
	%{buildroot}%{_datadir}/applications/%{name}-gtk.desktop

