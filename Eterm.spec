Summary:	Terminal for Enlightenment
Summary(es):	Terminal para Enlightenment
Summary(pl):	Terminal dla Enlightenmenta
Summary(pt_BR):	Eterm versão %{version}
Name:		Eterm
Version:	0.9.2
Release:	10
License:	GPL
Group:		X11/Applications
Source0:	http://www.eterm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	e8c82cf52b25fdd51d16ff76b993ba68
Source1:	http://www.eterm.org/download/%{name}-bg-%{version}.tar.gz
# Source1-md5:	fb465e84f24de348e31bb9fd4d430071
Source2:	%{name}.desktop
Source3:	Escreen.desktop
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-twin.patch
Patch2:		%{name}-keys-theme.patch
URL:		http://www.eterm.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	imlib2-devel >= 1.0.3
BuildRequires:	libast-devel >= 0.5
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	screen
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
Summary:	Sets root pixmap
Summary(pl):	Aplikacja ustawiaj±ca t³o nadrzêdnego okna
Group:		X11/Window Managers/Tools
 
%description -n Esetroot
This program enables non-Enlightenment users to use pseudotransparency.

%description -n Esetroot -l pl
Program ten umo¿liwia u¿ytkownikom zarz±dców okien innych ni¿ Enlightenment
korzystanie z pseudo-przezroczysto¶ci.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2	-p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-shared \
	--enable-escreen \
	--enable-etwin \
	--enable-profile \
	--disable-stack-trace \
	--without-debugging \
	--enable-trans \
	--enable-multi-charset \
	--enable-auto-encoding \
%ifarch athlon
	--enable-mmx
%else
	--disable-mmx
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/*

%files -n Esetroot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Esetroot
%attr(755,root,root) %{_bindir}/kEsetroot
 
