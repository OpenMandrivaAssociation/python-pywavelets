%define pkgname PyWavelets
%define module	pywavelets
%define name 	python-%{module}
%define version 0.1.6
%define release 1

Summary: 	Python module for wavelet transforms
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
Source0: 	%{pkgname}-%{version}.tar.bz2
License: 	MIT
Group:		Development/Python
Url: 		http://www.pybytes.com/pywavelets/
Obsoletes:	pywavelets
Requires:	python-numpy
Requires:	python >= 2.4
BuildRequires:	python-devel >= 2.4

%description
PyWavelets is a Python module for calculating the Simple and Inverse
Discrete Wavelet Transform, as well as Wavelet Packets and the Stationary
Wavelet Transform.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__python setup.py build

%install
rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES
%__chmod -R a+rx *.txt doc/ demo/

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc CHANGES.txt README.txt demo/ doc/


