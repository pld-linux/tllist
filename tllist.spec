Summary:	A C header file only implementation of a typed linked list
Name:		tllist
Version:	1.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://codeberg.org/dnkl/tllist/archive/%{version}.tar.gz
# Source0-md5:	5a778c92b33b654564094c8a40dce848
URL:		https://codeberg.org/dnkl/tllist
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
tllist is a Typed Linked List C header file only library implemented
using pre-processor macros.

%package devel
Summary:	A C header file only implementation of a typed linked list
Group:		Development/Libraries

%description devel
tllist is a Typed Linked List C header file only library implemented
using pre-processor macros.

%prep
%setup -q -n %{name}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc README.md
%{_includedir}/tllist.h
%{_pkgconfigdir}/tllist.pc
