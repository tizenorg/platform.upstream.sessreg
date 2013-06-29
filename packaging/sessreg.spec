Name:           sessreg
Version:        1.0.7
Release:        1
License:        MIT
Summary:        Utility to manage utmp/wtmp entries for X sessions
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	sessreg.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
BuildRequires:  pkgconfig(xproto)

%description
Sessreg is a simple program for managing utmp/wtmp entries for X sessions.
It was originally written for use with xdm, but may also be used with
other display managers such as gdm or kdm.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING
%{_bindir}/sessreg
%{_mandir}/man1/sessreg.1%{?ext_man}

%changelog
