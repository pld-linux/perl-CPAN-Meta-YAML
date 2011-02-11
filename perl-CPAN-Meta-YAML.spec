#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta-YAML
%include	/usr/lib/rpm/macros.perl
Summary:	CPAN::Meta::YAML - Read and write a subset of YAML for CPAN Meta files
Name:		perl-CPAN-Meta-YAML
Version:	0.003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	62d0f9726a2b91971b2f3f4ac770de5d
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
%{perl_vendorlib}/CPAN/Meta/*.pm
%{_mandir}/man3/CPAN::Meta::YAML.3pm*
