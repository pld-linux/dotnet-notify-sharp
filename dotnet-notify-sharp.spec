%include	/usr/lib/rpm/macros.mono

Summary:	notify-sharp is a C# client implementation for Desktop Notifications
Name:		dotnet-notify-sharp
Version:	0.4.0
Release:	3
License:	X11/MIT
Source0:	notify-sharp-%{version}.tar.gz
# Source0-md5:	dc8ea18947afb0801320182c81fc55bd
Patch0:		%{name}-monodir.patch
Group:		Development/Libraries
URL:		http://trac.galago-project.org/wiki/DesktopNotifications
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp
BuildRequires:	dotnet-ndesk-dbus-sharp
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	mono-devel
BuildRequires:	monodoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:	Files required for compilation using notify-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files required for compilation using notify-sharp.

%prep
%setup -q -n notify-sharp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-docs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/*.dll
%{_pkgconfigdir}/notify-sharp.pc
