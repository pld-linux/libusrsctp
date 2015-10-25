#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Userland SCTP stack
Summary(pl.UTF-8):	Stos SCTP w przestrzeni użytkownika
Name:		libusrsctp
Version:	0.9.2.1
%define	snap	20151025
%define	gitref	6071a9a41925c13dd4306bb6434bcce250bdecb2
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries
Source0:	https://github.com/sctplab/usrsctp/archive/%{gitref}/%{name}-%{version}.tar.gz
# Source0-md5:	230c42a5713f43e1f006dcf02cf86cf3
URL:		https://github.com/sctplab/usrsctp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
usrsctp is a userland SCTP stack supporting FreeBSD, Linux, Mac OS X
and Windows.

%description -l pl.UTF-8
Stos SCTP w przestrzeni użytkownika obsługujący FreeBSD, Linuksa, Mac
OS X oraz Windows.

%package devel
Summary:	Header files for usrsctp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki usrsctp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for usrsctp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki usrsctp.

%package static
Summary:	Static usrsctp library
Summary(pl.UTF-8):	Statyczna biblioteka usrsctp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static usrsctp library.

%description static -l pl.UTF-8
Statyczna biblioteka usrsctp.

%prep
%setup -q -n usrsctp-%{gitref}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libusrsctp.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_libdir}/libusrsctp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libusrsctp.so.1

%files devel
%defattr(644,root,root,755)
%doc Manual.md
%attr(755,root,root) %{_libdir}/libusrsctp.so
%{_includedir}/usrsctp.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libusrsctp.a
%endif
