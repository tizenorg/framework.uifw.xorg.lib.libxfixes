
Name:       libXfixes
Summary:    X.Org X11 libXfixes runtime library
Version:    4.0.5
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros)


%description
Xorg X11 libXfixes runtime library


%package devel
Summary:    Development components for the libXfixes library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Xorg X11 libXfixes development package


%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
#%dir %{_mandir}/man3x
%doc %{_mandir}/man3/Xfixes.3*

