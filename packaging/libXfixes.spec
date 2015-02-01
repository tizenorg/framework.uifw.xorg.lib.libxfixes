Summary: X Fixes library
Name: libXfixes
Version: 5.0
Release: 2
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(fixesproto) pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X Fixes library.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: libxfixes-devel
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
libXfixes development package

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
#%{_mandir}/man3/Xfixes.3*
