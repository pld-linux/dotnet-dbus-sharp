#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET library for using D-BUS message bus
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS
Name:		dotnet-dbus-sharp
Version:	0.63
Release:	1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	dbus-mono-%{version}.tar.bz2
# Source0-md5:	d87d155d643ae19ab48851c3820dbeb5
Patch0:		dbus-mint.patch
Patch1:		dbus-monodir.patch
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	rpmbuild(macros) >= 1.268
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
Requires:	%{name} = %{version}-%{release}

%description devel
Development .NET library for using D-BUS.

%description devel -l pl.UTF-8
Programistyczna biblioteka .NET do używania D-BUS.

%prep
%setup -qn dbus-mono-%{version}
%patch0 -p0
%patch1 -p1

# don't build dotnet-gtk-sharp based examples
# (depends on old gtk-sharp)
sed -i -e 's/example//' mono/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%{_prefix}/lib/mono/gac/dbus-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/dbus-sharp
%{_pkgconfigdir}/dbus-sharp.pc
