%define upstream_name    Algorithm-Diff-Apply
%define upstream_version 0.2.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	13

Summary:	Apply one or more Algorithm::Diff diffs
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)

BuildArch:	noarch

%description
This module contains subroutines for applying diffs generated by
Algorithm::Diff to a target array in the hope of regenerating a new array
incorporating all the changes described in the diffs into a new merged array.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make 
%make test

%install
%makeinstall_std

%files 
%{_mandir}/*/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.2.3-12mdv2011.0
+ Revision: 653385
- rebuild for updated spec-helper

* Wed Feb 10 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.2.3-11mdv2011.0
+ Revision: 503914
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.3-10mdv2010.0
+ Revision: 430256
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-9mdv2009.0
+ Revision: 255264
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-7mdv2008.1
+ Revision: 151811
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.3-5mdv2008.0
+ Revision: 85918
- rebuild


* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.3-4mdk
- Fix BuildRequires Using perl Policies
	- Source URL
	- BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.3-3mdk
- Buildrequires fix

* Thu Apr 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.3-2mdk
- spec cleanup

* Thu Apr 28 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.3-1mdk
- initial build

