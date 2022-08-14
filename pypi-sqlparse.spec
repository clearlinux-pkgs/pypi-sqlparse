#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6DB3F0E3E0B84F81 (albrecht.andi@gmail.com)
#
Name     : pypi-sqlparse
Version  : 0.4.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz.asc
Summary  : A non-validating SQL parser.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sqlparse-bin = %{version}-%{release}
Requires: pypi-sqlparse-license = %{version}-%{release}
Requires: pypi-sqlparse-python = %{version}-%{release}
Requires: pypi-sqlparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
======================================
        
        |buildstatus|_
        |coverage|_
        |docs|_
        
        .. docincludebegin
        
        sqlparse is a non-validating SQL parser for Python.
        It provides support for parsing, splitting and formatting SQL statements.
        
        The module is compatible with Python 3.5+ and released under the terms of the

%package bin
Summary: bin components for the pypi-sqlparse package.
Group: Binaries
Requires: pypi-sqlparse-license = %{version}-%{release}

%description bin
bin components for the pypi-sqlparse package.


%package license
Summary: license components for the pypi-sqlparse package.
Group: Default

%description license
license components for the pypi-sqlparse package.


%package python
Summary: python components for the pypi-sqlparse package.
Group: Default
Requires: pypi-sqlparse-python3 = %{version}-%{release}

%description python
python components for the pypi-sqlparse package.


%package python3
Summary: python3 components for the pypi-sqlparse package.
Group: Default
Requires: python3-core
Provides: pypi(sqlparse)

%description python3
python3 components for the pypi-sqlparse package.


%prep
%setup -q -n sqlparse-0.4.2
cd %{_builddir}/sqlparse-0.4.2
pushd ..
cp -a sqlparse-0.4.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369606
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sqlparse
cp %{_builddir}/sqlparse-0.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sqlparse/c4c4e71afeed48a083c414f8b157f11a3676954a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlformat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sqlparse/c4c4e71afeed48a083c414f8b157f11a3676954a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
