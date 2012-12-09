%define svn 12
%define major 0
%define libname %mklibname vbe %major
%define libnamedev %mklibname -d vbe

Summary: Vesa BIOS extension tools
Name: vesautils
Version: 0.1
Release: %mkrel -c %svn 1
Source0: %{name}-%{svn}.tar.xz
Patch: vesautils-10-makefile.patch
Patch1: vesautils-10-get-edid-path.patch
License: GPL
Group: System/Configuration/Hardware
Url: http://www.mplayerhq.hu/vesautils/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: liblrmi-devel
ExclusiveArch: %ix86

%description
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.

%package -n %libname
Group:System/Libraries
Summary: Vesa BIOS extension tools

%description -n %libname
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.

%package -n %libnamedev
Group:Development/C
Summary: Vesa BIOS extension tools
Requires: %libname = %version
Provides: libvbe-devel = %version-%release
Obsoletes: %mklibname -d vbe 0

%description -n %libnamedev
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.


%prep
%setup -q -n %name
%patch -p0
%patch1 -p1

%build
make
cd libvbe
make

%install
rm -rf %buildroot
install -d %buildroot%_bindir
install -m 755 dosint get-edid vbemodeinfo %buildroot%_bindir
cd libvbe
mkdir -p %buildroot%_libdir %buildroot%_includedir
%makeinstall LIBDIR=%buildroot%_libdir INCDIR=%buildroot%_includedir

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README
%_bindir/*

%files -n %libname
%defattr(-,root,root)
%_libdir/libvbe.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/libvbe.so
%attr(644,root,root) %_includedir/vbe.h


%changelog
* Wed Oct 19 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.1-0.12.1mdv2012.0
+ Revision: 705427
- newer svn snapshot
  cleaned up spec
  changed version to 0.1, bascally the release was being the version

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0-10.9
+ Revision: 670765
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0-10.8mdv2011.0
+ Revision: 608123
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0-10.7mdv2010.1
+ Revision: 524308
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0-10.6mdv2010.0
+ Revision: 427492
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 0-10.5mdv2009.0
+ Revision: 217196
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0-10.5mdv2008.1
+ Revision: 179678
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 03 2007 Götz Waschk <waschk@mandriva.org> 0-10.4mdv2008.0
+ Revision: 58498
- fix devel name

* Sun Jun 24 2007 Götz Waschk <waschk@mandriva.org> 0-10.3mdv2008.0
+ Revision: 43637
- Import vesautils



* Sun Jun 24 2007 Götz Waschk <waschk@mandriva.org> 0-10.3mdv2008.0
- fix path in get-edid (bug #31565)

* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 0-10.3mdv2007.0
- clean buildroot

* Sun Apr 23 2006 Götz Waschk <waschk@mandriva.org> 0-10.2mdk
- remove vbetool (already in the vbetool package

* Tue Apr  4 2006 Götz Waschk <waschk@mandriva.org> 0-10.1mdk
- this is for x86 only

* Mon Apr  3 2006 Götz Waschk <waschk@mandriva.org> 0-0.10.1mdk
- initial package
