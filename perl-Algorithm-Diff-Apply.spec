%define module Algorithm-Diff-Apply

Name:      perl-%{module}
Summary:   Apply one or more Algorithm::Diff diffs
Version:   0.2.3
Release:   %mkrel 4
License:   Artistic
Group:     Development/Perl
URL:       http://search.cpan.org/dist/%{module}
Source:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{module}-%version.tar.bz2
Buildroot: %_tmppath/%name-%version
Buildarch: noarch
BuildRequires: perl(Algorithm::Diff)
%if %{mdkversion} < 1010
Buildrequires: perl-devel
%endif

%description
This module contains subroutines for applying diffs generated by
Algorithm::Diff to a target array in the hope of regenerating a new array
incorporating all the changes described in the diffs into a new merged array.

%prep
%setup -q -n %{module}-%version 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make 
%make test

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/*


