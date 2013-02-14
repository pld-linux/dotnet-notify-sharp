%define		rel		1
%define		subver	20100411
%include	/usr/lib/rpm/macros.mono
Summary:	notify-sharp is a C# client implementation for Desktop Notifications
Name:		dotnet-notify-sharp
Version:	0.4.0
Release:	4.%{subver}.%{rel}
License:	X11/MIT
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/notify-sharp/notify-sharp-%{subver}.tar.bz2/add5e8884a3add412843037453a05ea6/notify-sharp-%{subver}.tar.bz2
# Source0-md5:	add5e8884a3add412843037453a05ea6
Patch0:		%{name}-monodir.patch
Group:		Development/Libraries
URL:		http://www.ndesk.org/NotifySharp
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.1
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
%setup -q -n notify-sharp-%{subver}
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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/gac/notify-sharp/*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/notify-sharp
%{_prefix}/lib/mono/notify-sharp/*.dll
%{_pkgconfigdir}/notify-sharp.pc
