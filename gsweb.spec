Summary:	WebObjects 4.x compatible library
Summary(pl):	Biblioteka kompatybilna z WebObjects 4.x
Name:		gsweb
Version:	0
%define cvs 20041118
Release:	0.%{cvs}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	525a9f986756db876ac0f5c1d19c17f9
URL:		http://www.gnustepweb.org/
BuildRequires:	gnustep-db2-devel
BuildRequires:	gsantlr-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
GNUstepWeb is a library which was designed to be compatible with
WebObjects 4.x (developed by NeXT (now Apple) Inc.).

This library is a logic extension of the GNUstep project. It should
help Objective-C, OpenStep and WebObjects to become standards.

%description -l pl
GNUstepWeb to biblioteka zaprojektowana by byæ kompatybiln± z
WebObjects 4.x (stworzon± przez NeXT (teraz Apple) Inc.).

Ta biblioteka jest logicznym rozszerzeniem projektu GNUstep. Powinna
pomóc Objective-C, OpenStepowi i WebObjects w staniu siê standardami.

%package devel
Summary:	Header files for gsweb library
Summary(pl):	Pliki nag³ówkowe biblioteki gsweb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gsweb library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gsweb.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%configure
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System \
	INSTALL_ROOT_DIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*
%dir %{_prefix}/System/Library/Frameworks/*.framework
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/?
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources
%{_prefix}/System/Library/Frameworks/*.framework/Versions/Current
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/*.plist
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/%{gscpu}/%{gsos}/%{libcombo}/*.so.*
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/*.gswc
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/WebServer
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/WebServer/*.png
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/WebServer/*.mng
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/*.wo
%lang(fr) %{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/French.lproj
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/DTDs
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/DTDs/*.ent
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Resources/DTDs/*.dtd
%dir %{_prefix}/System/Library/Libraries/Resources/DTDs
%{_prefix}/System/Library/Libraries/Resources/DTDs/*.ent
%{_prefix}/System/Library/Libraries/Resources/DTDs/*.dtd

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
%{_prefix}/System/Makefiles/Auxiliary/*.make
%{_prefix}/System/Library/Frameworks/*.framework/Headers
%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Headers
%{_prefix}/System/Library/Frameworks/*.framework/Versions/?/Headers/*
