Summary:	Terminal for Enlightenment
Summary(pl):	Terminal dla Enlightenmenta
Name:		Eterm
Version:	0.8.9
Release:	2
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source:		ftp://ftp.enlightenment.org/pub/Eterm/%{name}-%{version}.tar.gz
Patch0:		Eterm-utempter.patch
Patch1:		Eterm-features.patch
Requires:	imlib >= 1.9.2
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Eterm is a color vt102 terminal emulator intended as an xterm(1) replacement
for users who want a term program integrated with Enlightenment, or simply
want a little more "eye candy". Eterm uses Imlib for advanced graphic
abilities.

%description -l pl
Eterm jest kolorowym emulatorem terminala vt102 mogacym byæ zamiennikiem
xterm(1) dla u¿ytkowników chc±cych mieæ program terminalowy zintegrowany z
zarz±dc± okienek o nazwie Enlightenment lub dla tych którzy chc± mieæ 
trochê bardziej urozmaicony wygl±d tego typu programu. Eterm u¿ywa
biblioteki IMlib do zaawansowanego operowania na grafice.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s -lutempter" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--disable-static \
	--enable-shared \
	--disable-stack-trace \
	--without-debugging
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

make install \
	DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libEterm.so.0.8.9
%attr(755,root,root) %{_libdir}/libmej.so.0.8.9
%{_libdir}/libEterm.so.0
%{_libdir}/libmej.so.0
%{_mandir}/man1/*
%{_datadir}/Eterm
