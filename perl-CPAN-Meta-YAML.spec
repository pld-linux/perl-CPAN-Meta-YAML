#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta-YAML
%include	/usr/lib/rpm/macros.perl
Summary:	CPAN::Meta::YAML - read and write a subset of YAML for CPAN Meta files
Summary(pl.UTF-8):	CPAN::Meta::YAML - odczyt i zapis podzbioru YAML-a dla plików CPAN Meta
Name:		perl-CPAN-Meta-YAML
Version:	0.008
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06211d8492f23c68aadb83670451284d
URL:		http://search.cpan.org/dist/CPAN-Meta-YAML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like META.yml and MYMETA.yml.
It should not be used for any other general YAML parsing or generation
task.

%description -l pl.UTF-8
Ten moduł jest implementacją podzbioru specyfikacji YAML-a
przeznaczoną do odczytu i zapisu plików metadanych CPAN, takich jak
META.yml i MYMETA.yml. Nie powinien być używany do przetwarzania i
generowania YAML-a w innych celach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/CPAN
%dir %{perl_vendorlib}/CPAN/Meta
%{perl_vendorlib}/CPAN/Meta/YAML.pm
%{_mandir}/man3/CPAN::Meta::YAML.3pm*
