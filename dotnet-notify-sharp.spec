Summary:	C# client implementation for Desktop Notifications
Summary(pl.UTF-8):	Implementacja C# klienta usługi Desktop Notifications
Name:		dotnet-notify-sharp
Version:	0.4.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://www.meebey.net/projects/notify-sharp/downloads/notify-sharp-%{version}.tar.gz
# Source0-md5:	46fcb7a6b9b1cd0241366b8234e31e37
Patch0:		%{name}-monodir.patch
Patch1:		notify-sharp-dbus.patch
URL:		https://www.meebey.net/projects/notify-sharp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel >= 1:0.7
BuildRequires:	dotnet-dbus-sharp-glib-devel >= 0.5
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.1
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	mono-devel >= 1.1.13
BuildRequires:	mono-monodoc >= 1.1.18
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.015
Requires:	dotnet-dbus-sharp >= 1:0.7
Requires:	dotnet-dbus-sharp-glib >= 0.5
Requires:	dotnet-gtk-sharp2 >= 2.10.1
Requires:	mono >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no native code
%define		_enable_debug_packages	0

%description
notify-sharp (Notify#) is a C# client implementation for Desktop
Notifications, i.e. notification-daemon. It is inspired by the
libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%description -l pl.UTF-8
notify-sharp (Notify#) to implementacja w C# klienta usługi Desktop
Notifications (powiadomień w środowisku graficznym), tj. usługi
notification-daemon. Jest zainspirowana API biblioteki libnotify.

Desktop Notifications to usługa zapewniająca standardową metodę
wykonywania pasywnych powiadomień poprzez wyskakujące okienka na
pulpicie Linuksa. Jest zaprojektowana w celu powiadamiania użytkownika
o jakimś zdarzeniu bez przerywania pracy oknem dialogowym, które
trzeba zamknąć. Pasywne wyskakujące okienka mogą znikać automatycznie
po krótkim okresie czasu.

%package devel
Summary:	Development files for notify-sharp library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki notify-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.10.1
Requires:	mono-devel >= 1.1.13

%description devel
Development files for notify-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki notify-sharp.

%prep
%setup -q -n notify-sharp-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	GMCS=/usr/bin/mcs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/0.4.0.0__*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/notify-sharp.dll
%{_prefix}/lib/monodoc/sources/notify-sharp-docs.*
%{_pkgconfigdir}/notify-sharp.pc
