Summary:	Terminal for Enlightenment
Summary(pl):	Terminal dla Enlightenmenta
Name:		Eterm
Version:	0.8.9
Release:	1
Copyright:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source:		ftp://ftp.enlightenment.org/pub/Eterm/%{name}-%{version}.tar.gz
Requires:	imlib >= 1.9.2
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Eterm is a color vt102 terminal emulator intended as an xterm(1) replacement
for users who want a term program integrated with Enlightenment, or simply
want a little more "eye candy". Eterm uses Imlib for advanced graphic
abilities.

%description -l pl
Eterm jest kolorowym emulatorem terminala vt102 mogacym byæ zamiennikiem
xterm(1) dla u¿ytkowników chc±cych mieæ program terminalowy zintegrowany z
zarz±dc± okienek o nazwie Enlightenment lub dla tych któzrzy ch± mieæ 
trochê bardziej urozmaicony wygl±d tego typu programu. Eterm uzywa
biblioteki IMlib do zaawansowanego operowania na grafice.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6 \
	--with-imlib=/usr/X11R6 \
	--disable-static \
	--enable-shared \
	--disable-stack-trace \
	--without-debugging
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,lib,man}

make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/* \
	doc/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html.gz

%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/libEterm.so.0.8.9
%attr(755,root,root) /usr/X11R6/lib/libmej.so.0.8.9
/usr/X11R6/lib/libEterm.so.0
/usr/X11R6/lib/libmej.so.0
/usr/X11R6/man/man1/*

/usr/X11R6/share/Eterm

%changelog
* Sat Jun 05 1999 Jan Rêkorajski <baggins@pld.org.pl>
  [0.8.9-1]
- update to 0.8.9
	--disable-static
	--enable-shared
	--disable-stack-trace

* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.8.8-2d]
- added gzipping documentation
- cosmetic changes

* Wed Feb  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.8.8-1d]
- changed pl translation,
- added --without-debugging to ./configure parametrs,
- updated Requires for imlib (= 1.9.2),
- added patch for proper installing with using $DESTDIR,
- added Grou(pl).

* Thu Aug 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.8-3d]
- updated to Eterm-DR-0.8+PL2,
- added default background themes,
- minor modifications of spec file.

* Thu Jul 09 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.8-2d]
- first try at an RPM,
- build against glibc-2.1,
- added a utmp.c patch,
- translation modified for pl,
- added %changelog,
- changed prefix to /usr/X11R6.
