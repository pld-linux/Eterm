Summary:	Terminal for Enlightenment
Summary(pl):	Terminal dla Enlightenmenta
Name:		Eterm
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://www.eterm.org/download/Eterm-0.9.1.tar.gz	
Source1: 	http://www.eterm.org/download/Eterm-bg-0.9.1.tar.gz	
Patch0:		%{name}-features.patch
Patch1:		%{name}-xterm-color-fixes.patch
URL:		http://www.eterm.org/
BuildRequires:	imlib2-devel >= 1.0.3
BuildRequires:  libast-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Eterm is a color vt102 terminal emulator intended as an xterm(1)
replacement for users who want a term program integrated with
Enlightenment, or simply want a little more "eye candy". Eterm uses
Imlib for advanced graphic abilities.

%description -l pl
Eterm jest kolorowym emulatorem terminala vt102 mogacym byæ
zamiennikiem xterm(1) dla u¿ytkowników chc±cych mieæ program
terminalowy zintegrowany z zarz±dc± okienek o nazwie Enlightenment lub
dla tych którzy chc± mieæ trochê bardziej urozmaicony wygl±d tego typu
programu. Eterm u¿ywa biblioteki IMlib do zaawansowanego operowania na
grafice.

%prep
%setup -q -a1
#%patch0 -p1
#%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
%configure \
	--disable-static \
	--enable-shared \
	--disable-stack-trace \
	--without-debugging
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.html

%attr(2755,root,utmp) %{_bindir}/Eterm
%attr(755,root,root) %{_bindir}/Esetroot
%attr(755,root,root) %{_bindir}/Etbg
#%attr(755,root,root) %{_bindir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/*
%{_datadir}/Eterm
