Summary:	MIME library for GNUstep
Summary(pl):	Biblioteka MIME dla ¶rodowiska GNUstep
Name:		gsweb
Version:	0
%define cvs 20041118
Release:	0.%{cvs}.1
License:	LGPL
Group:		Libraries
Source0:	%{name}-cvs-%{cvs}.tar.gz
# Source0-md5:	525a9f986756db876ac0f5c1d19c17f9
URL:		http://www.gnustepweb.org
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
#%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*
#%dir %{_prefix}/System/Library/Frameworks/*.framework
#%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions
#%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/*
#%dir %{_prefix}/System/Library/Frameworks/*.framework/Versions/*/Resources
#%{_prefix}/System/Library/Frameworks/*.framework/Versions/*/Resources/*.bundle
#%{_prefix}/System/Library/Frameworks/*.framework/Versions/*/Resources/*.plist
#%{_prefix}/System/Library/Frameworks/*.framework/Versions/*/%{gscpu}/%{gsos}/%{libcombo}/*.so.*

%files devel
%defattr(644,root,root,755)
#%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
#%{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/*
#%{_prefix}/System/Tools/%{gscpu}/%{gsos}/%{libcombo}/*
#%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/*.so
#%{_prefix}/System/Library/Frameworks/*.framework/Headers
#%{_prefix}/System/Library/Frameworks/*.framework/Versions/*/Headers/*
