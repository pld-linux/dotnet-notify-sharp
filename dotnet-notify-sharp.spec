Name:		dotnet-notify-sharp
Summary:	notify-sharp is a C# client implementation for Desktop Notifications
Version:	0.4.0
Release:	0
License:	X11/MIT
URL:		http://trac.galago-project.org/wiki/DesktopNotifications
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	gtk+2-devel
BuildRequires:	mono-devel
BuildRequires:	monodoc
BuildRequires:	dotnet-ndesk-dbus-sharp
BuildRequires:	dotnet-ndesk-dbus-glib-sharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	notify-sharp-%{version}.tar.gz
# Source0-md5:	dc8ea18947afb0801320182c81fc55bd
Group:		Development/Libraries

%package devel
Summary:	Files required for compilation using notify-sharp
Group:	Development/Libraries

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%description devel
Files required for compilation using notify-sharp.

%prep
%setup -q -n notify-sharp-%{version}

%build
%configure \
	--disable-docs \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/%_lib/pkgconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/*

%files devel
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/*
%{_pkgconfigdir}/notify-sharp.pc
