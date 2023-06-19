#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : libyami
Version  : 1.3.2
Release  : 14
URL      : https://github.com/intel/libyami/archive/1.3.2/libyami-1.3.2.tar.gz
Source0  : https://github.com/intel/libyami/archive/1.3.2/libyami-1.3.2.tar.gz
Summary  : Intel open source media infrastructure base on libva.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: libyami-lib = %{version}-%{release}
Requires: libyami-license = %{version}-%{release}
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(x11)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Yet Another Media Infrastructure.
It is YUMMY to your video experience on Linux like platform.
Yami is core building block for media solution. it parses video stream
and decodes them leverage hardware acceleration.

%package dev
Summary: dev components for the libyami package.
Group: Development
Requires: libyami-lib = %{version}-%{release}
Provides: libyami-devel = %{version}-%{release}
Requires: libyami = %{version}-%{release}

%description dev
dev components for the libyami package.


%package lib
Summary: lib components for the libyami package.
Group: Libraries
Requires: libyami-license = %{version}-%{release}

%description lib
lib components for the libyami package.


%package license
Summary: license components for the libyami package.
Group: Default

%description license
license components for the libyami package.


%prep
%setup -q -n libyami-1.3.2
cd %{_builddir}/libyami-1.3.2
pushd ..
cp -a libyami-1.3.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687213128
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static --enable-vp9dec \
--enable-vp9enc \
--enable-h265enc \
--enable-h265dec \
--enable-jpegenc \
--enable-vp8enc \
--enable-dmabuf
make  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static --enable-vp9dec \
--enable-vp9enc \
--enable-h265enc \
--enable-h265dec \
--enable-jpegenc \
--enable-vp8enc \
--enable-dmabuf
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1687213128
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libyami
cp %{_builddir}/libyami-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/libyami/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/libyami-%{version}/codecparsers/dboolhuff.LICENSE %{buildroot}/usr/share/package-licenses/libyami/4dbe7c1f3a1833a88333a7c282119323e9ef44fa || :
cp %{_builddir}/libyami-%{version}/codecparsers/vp9quant.LICENSE %{buildroot}/usr/share/package-licenses/libyami/e9e216e41252f23ea09d1377ed8b9061db7db903 || :
cp %{_builddir}/libyami-%{version}/gtestsrc/gtest/LICENSE %{buildroot}/usr/share/package-licenses/libyami/5a2314153eadadc69258a9429104cd11804ea304 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libyami/VideoCommonDefs.h
/usr/include/libyami/VideoDecoderCapi.h
/usr/include/libyami/VideoDecoderDefs.h
/usr/include/libyami/VideoDecoderHost.h
/usr/include/libyami/VideoDecoderInterface.h
/usr/include/libyami/VideoEncoderCapi.h
/usr/include/libyami/VideoEncoderDefs.h
/usr/include/libyami/VideoEncoderHost.h
/usr/include/libyami/VideoEncoderInterface.h
/usr/include/libyami/VideoPostProcessDefs.h
/usr/include/libyami/VideoPostProcessHost.h
/usr/include/libyami/VideoPostProcessInterface.h
/usr/include/libyami/Yami.h
/usr/include/libyami/YamiC.h
/usr/include/libyami/YamiVersion.h
/usr/lib64/libyami.so
/usr/lib64/pkgconfig/libyami.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libyami.so.1.3.1
/usr/lib64/libyami.so.1
/usr/lib64/libyami.so.1.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libyami/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/libyami/4dbe7c1f3a1833a88333a7c282119323e9ef44fa
/usr/share/package-licenses/libyami/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/libyami/e9e216e41252f23ea09d1377ed8b9061db7db903
