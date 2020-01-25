
%define		module	dbus-sharp

Summary:	D-Bus for .NET - C# library implementing D-Bus
Summary(pl.UTF-8):	D-Bus dla .NET - biblioteka C# implementująca D-Bus
Name:		dotnet-dbus-sharp
Version:	0.7.0
Release:	3
Epoch:		1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/mono/dbus-sharp/downloads
Source0:	http://github.com/downloads/mono/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	1964fc341dcbaeda859c53cee295d042
Patch0:		dbus-monodir.patch
URL:		http://mono.github.com/dbus-sharp/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
Requires:	mono >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbus-sharp is a fork of ndesk-dbus, which is a C# implementation of
D-Bus. It's often referred to as "managed D-Bus" to avoid confusion
with other existing bindings (which wrap libdbus).

%description -l pl.UTF-8
dbus-sharp to odgałęzienie ndesk-dbus, czyli implementacji D-Bus w
języku C#. Często jest nazywane "zarządzanym D-Bus" w odróżnieniu od
innych istniejących wiązań, obudowujących bibliotekę libdbus.

%package devel
Summary:	Development files for dbus-sharp library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki dbus-sharp
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mono-devel >= 1.1.13

%description devel
Development files for dbus-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki dbus-sharp.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_prefix}/lib/mono/gac/dbus-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/dbus-sharp-1.0
%{_pkgconfigdir}/dbus-sharp-1.0.pc
