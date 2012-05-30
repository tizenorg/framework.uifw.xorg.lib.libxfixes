Name:       libxfixes
Summary:    X.Org X11 libXfixes runtime library
Version:    4.0.5
Release:    2.6
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Source1001: packaging/libxfixes.manifest 
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
cp %{SOURCE1001} .
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
autoreconf -vfi
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%manifest libxfixes.manifest
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0


%files devel
%manifest libxfixes.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
#%dir %{_mandir}/man3x
%doc %{_mandir}/man3/Xfixes.3*

%changelog
* Fri May 13 2011 Li Peng <peng.li@intel.com> - 5.0
- libXfixes 5.0
* Sat Feb 27 2010 Anas Nashif <anas.nashif@intel.com> - 4.0.4
- Updated with latest spectacle
- Include YAML file in source rpm
* Fri Dec 11 2009 Li Peng <peng.li@intel.com> 4.0.4
- libXfixes 4.0.4
* Thu Dec 18 2008 Arjan van de Ven <arjan@linux.intel.com> 4.0.3
- Fix buildrequires
* Tue Dec 16 2008 Anas Nashif <anas.nashif@intel.com> 4.0.3
- Update spec file using latest spec-builder
* Tue Dec 16 2008 Anas Nashif <anas.nashif@intel.com> 4.0.3
- Update spec file using latest spec-builder
* Thu Dec 11 2008 Arjan van de Ven <arjan@linux.intel.com> 4.0.3
- Clean up specfile
