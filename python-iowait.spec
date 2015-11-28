%define 	module	iowait
Summary:	Platform-independent module for I/O completion events
Name:		python-%{module}
Version:	0.1
Release:	2
License:	LGPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/i/iowait/iowait-%{version}.tar.gz
# Source0-md5:	f928f3c54cfa2c054e889abe936cd775
URL:		https://launchpad.net/python-iowait
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Different operating systems provide different ways to wait for I/O
completion events: there's select(), poll(), epoll() and kqueue(). For
cross-platform applications it can be a pain to support all this
system functions, especially because each one provides a different
interface.

IOWait solves this problem by providing a unified interface and using
always the best and faster function available in the platform. Its
only limitation is that, on Windows, it only works for sockets.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/iowait.py[co]
%{py_sitescriptdir}/iowait-%{version}-py*.egg-info
