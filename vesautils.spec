%define svn	12
%define major	0
%define libname	%mklibname vbe %{major}
%define devname	%mklibname -d vbe

Summary:	Vesa BIOS extension tools
Name:		vesautils
Version:	0.1
Release:	0.%{svn}.1
License:	GPLv2
Group:		System/Configuration/Hardware
Url:		http://www.mplayerhq.hu/vesautils/index.html
Source0:	%{name}-%{svn}.tar.xz
Patch0:		vesautils-10-makefile.patch
Patch1:		vesautils-10-get-edid-path.patch
ExclusiveArch:	%ix86
BuildRequires:	liblrmi-devel

%description
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.

%package -n %{libname}
Summary:	Vesa BIOS extension tools
Group:		System/Libraries

%description -n %{libname}
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.

%package -n %{devname}
Summary:	Vesa BIOS extension tools
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libvbe-devel = %{version}-%{release}

%description -n %{devname}
This is a collection of utilities and a library for handling the VESA
BIOS Extension (aka VBE) with the help of LRMI under Linux and BSD.

%prep
%setup -qn %{name}
%apply_patches

%build
make
cd libvbe
make

%install
install -d %{buildroot}%{_bindir}
install -m 755 dosint get-edid vbemodeinfo %{buildroot}%{_bindir}
cd libvbe
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}
%makeinstall LIBDIR=%{buildroot}%{_libdir} INCDIR=%{buildroot}%{_includedir}

%files
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libvbe.so.%{major}*

%files -n %{devname}
%{_libdir}/libvbe.so
%{_includedir}/vbe.h

