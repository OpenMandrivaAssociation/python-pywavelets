%define pkgname PyWavelets
%define module	pywavelets
%define smodule pywt

%bcond_with tests

Summary: 	Python module for wavelet transforms
Name: 		python-%{module}
Version: 	1.1.1
Release: 	1
Source0:	https://github.com/PyWavelets/pywt/archive/refs/tags/v%{version}/%{smodule}-%{version}.tar.gz
#Patch0:		setup-lm-0.2.2.patch
License: 	MIT
Group:		Development/Python
Url: 		https://pywavelets.readthedocs.io/
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(cython)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(setuptools)
# for docs
BuildRequires:	python3dist(pygments)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(numpydoc)
BuildRequires:	python3dist(matplotlib)

%if %{with tests}
BuildRequires:	python3-nose
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

%files
%license LICENSE
%doc README.rst
%doc doc/build/html
%doc demo/
%{python3_sitearch}/%{smodule}/
%{python3_sitearch}/%{pkgname}-*.egg-info

#---------------------------------------------------------------------------

%prep
%autosetup -n %{smodule}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix wrong-script-interpreter
find demo -name '*.py' -exec sed -i "s|#!/usr/bin/env python|#!%__python3|" {} \;

%build
%py3_build

%install
%py3_install

# docs
PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitearch}" \
make -C doc PAPER=letter html
find doc/build/html -name '.*' -delete
