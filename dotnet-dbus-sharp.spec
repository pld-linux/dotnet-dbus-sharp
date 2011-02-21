#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET library for using D-BUS message bus
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS
Name:		dotnet-dbus-sharp
Version:	0.7.0
Release:	1
Epoch:		1
License:	AFL v2.1 or GPL v2+
Group:		Libraries
Source0:	dbus-sharp-%{version}.tar.gz
# Source0-md5:	1964fc341dcbaeda859c53cee295d042
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS.

%description -l pl.UTF-8
Biblioteka .NET do używania D-BUS.

%package devel
Summary:	Development .NET library for using D-BUS
Summary(pl.UTF-8):	Programistyczna biblioteka .NET do używania D-BUS
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development .NET library for using D-BUS.

%description devel -l pl.UTF-8
Programistyczna biblioteka .NET do używania D-BUS.

%prep
%setup -q -n dbus-sharp-%{version}

%build
%{__libtoolize}
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
%doc AUTHORS README
%{_prefix}/lib/mono/gac/dbus-sharp
%{_prefix}/lib/mono/dbus-sharp-1.0

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/dbus-sharp-*.pc
