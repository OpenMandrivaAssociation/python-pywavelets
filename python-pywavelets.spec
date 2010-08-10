%define pkgname PyWavelets
%define module	pywavelets
%define name 	python-%{module}
%define version 0.2.0
%define release 1

Summary: 	Python module for wavelet transforms
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{pkgname}-%{version}.tar.bz2
License: 	MIT
Group:		Development/Python
Url: 		http://www.pybytes.com/pywavelets/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	pywavelets
Requires:	python-numpy
BuildRequires:	python-cython
BuildRequires:	python-sphinx
%py_requires -d

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
%setup -q -n %{pkgname}-%{version}

%build
PYTHONDONTWRITEBYTECODE= %__python setup.py build
%make -C doc html

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt demo/ doc/build/html


