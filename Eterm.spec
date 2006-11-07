#
# Conditional build:
%bcond_with	mmx		# use MMX instructions
%bcond_with	sse2		# use SSE2 instructions
#
%ifarch athlon pentium3 pentium4
%define		with_mmx	1
%endif
%ifarch %{x8664}
%define		with_sse2	1
%endif
Summary:	Terminal for Enlightenment
Summary(es):	Terminal para Enlightenment
Summary(pl):	Terminal dla Enlightenmenta
Summary(pt_BR):	Eterm versão %{version}
Name:		Eterm
Version:	0.9.4
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	b8869ee9c9b9516231af9eefa595cee3
Source1:	http://www.eterm.org/download/%{name}-bg-%{version}.tar.gz
# Source1-md5:	e8c6567b13d7fb760bded56c1d1a181d
Source2:	%{name}.desktop
Source3:	Escreen.desktop
Source4:	gnome-eterm.png
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-keys-theme.patch
URL:		http://www.eterm.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	imlib2-devel >= 1.0.3
BuildRequires:	libast-devel >= 0.6
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	screen
BuildRequires:	sed >= 4.0
BuildRequires:	twin-devel
BuildRequires:	utempter-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eterm is a color vt102 terminal emulator intended as an xterm(1)
replacement for users who want a term program integrated with
Enlightenment, or simply want a little more "eye candy". Eterm uses
Imlib for advanced graphic abilities.

%description -l es
Eterm es un emulador de terminal vt102 con soporte para colores,
desarrollado como un sustituto para el emulador xterm, para los
usuarios que deseen un emulador de terminal integrado con la
iluminación, o simplemente deseen algo más agradable visualmente. El
emulador Eterm usa Imlib para trabajar con gráficos.

%description -l pl
Eterm jest kolorowym emulatorem terminala vt102 mog±cym byæ
zamiennikiem xterm(1) dla u¿ytkowników chc±cych mieæ program
terminalowy zintegrowany z zarz±dc± okienek o nazwie Enlightenment lub
dla tych którzy chc± mieæ trochê bardziej urozmaicony wygl±d tego typu
programu. Eterm u¿ywa biblioteki IMlib do zaawansowanego operowania na
grafice.

%description -l pt_BR
O Eterm -- versão %{version} -- é um emulador de terminal vt102 com
suporte a cores, desenvolvido para ser um substituto para o xterm,
para os usuários que queiram um emulador de terminal integrado com o
Enlightenment, ou simplesmente queiram algo mais agradável para os
olhos. O Eterm usa a Imlib para trabalhar com gráficos.

%package -n Esetroot
Summary:	Utility to set root pixmap
Summary(pl):	Aplikacja ustawiaj±ca t³o nadrzêdnego okna
Group:		X11/Window Managers/Tools
 
%description -n Esetroot
This program enables non-Enlightenment users to use
pseudotransparency.

%description -n Esetroot -l pl
Program ten umo¿liwia korzystanie z pseudoprzezroczysto¶ci
u¿ytkownikom zarz±dców okien innych ni¿ Enlightenment.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
find themes/ -name "*.cfg*" -exec \
	sed -i 's/<Eterm-0\.9\..>/<Eterm-%{version}>/' "{}" ";"

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--enable-shared		\
	--enable-escreen	\
	--enable-etwin		\
	--enable-escreen-fx	\
	--enable-profile	\
	--enable-trans		\
%if %{with mmx}
	--enable-mmx		\
%else
	--disable-mmx		\
%endif
%if %{with sse2}
	--enable-sse2		\
%else
	--disable-sse2		\
%endif
	--enable-utmp		\
	--enable-auto-encoding	\
	--enable-multi-charset	\
	--disable-stack-trace	\
	--enable-name-reporting-escapes \
	--without-debugging
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.html ReleaseNotes* ChangeLog
%attr(755,root,root) %{_bindir}/Eterm
%attr(755,root,root) %{_bindir}/Etbg
%attr(755,root,root) %{_bindir}/Etcolors
%attr(755,root,root) %{_bindir}/Ettable
%attr(755,root,root) %{_bindir}/Etbg_update_list
%attr(755,root,root) %{_bindir}/Etsearch
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man1/*
%{_datadir}/Eterm
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files -n Esetroot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Esetroot
%attr(755,root,root) %{_bindir}/kEsetroot
 
