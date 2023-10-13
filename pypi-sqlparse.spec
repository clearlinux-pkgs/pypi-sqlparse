#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
# Source0 file verified with key 0x6DB3F0E3E0B84F81 (albrecht.andi@gmail.com)
#
Name     : pypi-sqlparse
Version  : 0.4.4
Release  : 13
URL      : https://files.pythonhosted.org/packages/65/16/10f170ec641ed852611b6c9441b23d10b5702ab5288371feab3d36de2574/sqlparse-0.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/16/10f170ec641ed852611b6c9441b23d10b5702ab5288371feab3d36de2574/sqlparse-0.4.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/65/16/10f170ec641ed852611b6c9441b23d10b5702ab5288371feab3d36de2574/sqlparse-0.4.4.tar.gz.asc
Summary  : A non-validating SQL parser.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-sqlparse-bin = %{version}-%{release}
Requires: pypi-sqlparse-license = %{version}-%{release}
Requires: pypi-sqlparse-python = %{version}-%{release}
Requires: pypi-sqlparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
python-sqlparse - Parse SQL statements
======================================
|buildstatus|_
|coverage|_
|docs|_
|packageversion|_

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
%setup -q -n sqlparse-0.4.4
cd %{_builddir}/sqlparse-0.4.4
pushd ..
cp -a sqlparse-0.4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681833104
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sqlparse
cp %{_builddir}/sqlparse-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sqlparse/c4c4e71afeed48a083c414f8b157f11a3676954a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
