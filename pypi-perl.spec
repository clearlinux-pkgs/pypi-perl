#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-perl
Version  : 1.0.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/cb/2f/d2724ee752dc50c6eb4273ab5c486ce43737866072f15bd089e449003fd2/perl-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/2f/d2724ee752dc50c6eb4273ab5c486ce43737866072f15bd089e449003fd2/perl-1.0.0.tar.gz
Summary  : Perl as a Python package
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-perl-license = %{version}-%{release}
Requires: pypi-perl-python = %{version}-%{release}
Requires: pypi-perl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(pytest_runner)
BuildRequires : pypi(six)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Perl as a Python package
        ========================

%package license
Summary: license components for the pypi-perl package.
Group: Default

%description license
license components for the pypi-perl package.


%package python
Summary: python components for the pypi-perl package.
Group: Default
Requires: pypi-perl-python3 = %{version}-%{release}

%description python
python components for the pypi-perl package.


%package python3
Summary: python3 components for the pypi-perl package.
Group: Default
Requires: python3-core
Provides: pypi(perl)
Requires: pypi(six)

%description python3
python3 components for the pypi-perl package.


%prep
%setup -q -n perl-1.0.0
cd %{_builddir}/perl-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639061292
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-perl
cp %{_builddir}/perl-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-perl/ed162379c94acdde7b07bb868f0676497fdd8462
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-perl/ed162379c94acdde7b07bb868f0676497fdd8462

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*