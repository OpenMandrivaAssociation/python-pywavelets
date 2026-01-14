%define module pywt
%define oname pywavelets

%bcond tests 0
# doc html build requires myst-nb which is unpackaged
%bcond docs 0

Summary: 	Python module for wavelet transforms
Name: 		python-pywavelets
Version: 	1.9.0
Release: 	1
Source0:	https://github.com/PyWavelets/pywt/archive/refs/tags/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch0:		setup-lm-0.2.2.patch
License: 	MIT
Group:		Development/Python
URL: 		https://pywavelets.readthedocs.io/
BuildSystem:	python
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	make
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# for docs
%if %{with docs}
BuildRequires:	python%{pyver}dist(pygments)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(numpydoc)
BuildRequires:	python%{pyver}dist(matplotlib)
# Currenty unpackaged, doc build requires myst-nb
#BuildRequires:	python%%{pyver}dist(myst_nb)
%endif
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
PyWavelets is a Python wavelet transform module that includes:

* 1D and 2D Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
* 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
* 1D and 2D Wavelet Packet decomposition and reconstruction
* Computing Approximations of wavelet and scaling functions
* Over seventy built-in wavelet filters and support for custom wavelets
* Single and double precision calculations
* Results compatibility with Matlab Wavelet Toolbox (tm)


%prep
%autosetup -n %{module}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix wrong-script-interpreter
find demo -name '*.py' -exec sed -i "s|#!/usr/bin/env python|#!%{__python}|" {} \;
sed -i '1{/env python/d}' pywt/tests/*.py util/create_dat.py
chmod -x util/create_dat.py

# These are unpackaged deps and apparently not needed
sed -i -e '/jupyterlite_sphinx/d' -e '/sphinx_togglebutton/d' doc/source/conf.py
sed -i -e '/jupyterlite-pyodide-kernel/d' -e '/jupyterlite-sphinx/d' -e '/sphinx-togglebutton/d' -e '/docutils/s/<.*//' util/readthedocs/requirements.txt

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export LDFLAGS="%{ldflags} -lpython%{pyver}"
%py_build

%install
%py_install
# doc build requires the package to be installed in the buildroot
%if %{with docs}
# make html docs
PYTHONPATH="%{buildroot}%{python_sitearch}" make -C doc html
find -name '.buildinfo' -delete
%endif

%files
%license LICENSE
%doc README.rst
%doc demo/
%{python_sitearch}/%{module}/
%{python_sitearch}/%{oname}-%{version}.dist-info
%if %{with docs}
%doc doc/build/html
%endif
