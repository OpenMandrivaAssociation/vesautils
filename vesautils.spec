%define name vesautils
%define version 0
%define svn 10
%define major 0
%define libname %mklibname vbe %major
%define libnamedev %mklibname -d vbe

Summary: Vesa BIOS extension tools
Name: %{name}
Version: %{version}
Release: %mkrel %svn.9
Source0: %{name}-%{svn}.tar.bz2
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
