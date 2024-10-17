Name:		pyrit
Version:	0.4.0
Release:	1
# OpenSSL exception
License:	GPLv3
Group:		Monitoring
Summary:	A GPGPU-driven WPA/WPA2-PSK key cracker
URL:		https://code.google.com/p/pyrit/
Source0:	http://pyrit.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	python-devel, openssl-devel, zlib-devel, libpcap-devel
# Scapy and python-sqlalchemy are needed for full testing
BuildRequires:	scapy, python-sqlalchemy
Requires:	scapy, python-sqlalchemy
Provides:	python-pyrit = %{version}-%{release}

%description
Pyrit exploits the computational power of many-core and GPGPU-platforms to
create massive databases, pre-computing part of the WPA/WPA2-PSK authentication
phase in a space-time trade-off. It is a powerful attack against one of the 
world's most used security-protocols.
Please note that this package only provides CPU support, GPUGPU support requires
CUDA or OpenCL, which have no Free Software implementations at this time.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}
chmod 755 %{buildroot}%{python_sitearch}/cpyrit/*.so

%files
%doc CHANGELOG COPYING PKG-INFO README
%{_bindir}/%{name}
%{python_sitearch}/cpyrit/
%{python_sitearch}/%{name}-%{version}-*.egg-info
%{python_sitearch}/%{name}_cli.*
