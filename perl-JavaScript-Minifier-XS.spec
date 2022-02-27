#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	JavaScript
%define		pnam	Minifier-XS
Summary:	JavaScript::Minifier::XS - XS based JavaScript minifier
Name:		perl-JavaScript-Minifier-XS
Version:	0.11
Release:	8
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JavaScript/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd8544287ecd1b651367295485f4a5b0
URL:		http://search.cpan.org/dist/JavaScript-Minifier-XS/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript::Minifier::XS is a JavaScript "minifier"; its designed to
remove un-necessary whitespace and comments from JavaScript files,
which also not breaking the JavaScript.

JavaScript::Minifier::XS is similar in function to
JavaScript::Minifier, but is substantially faster as its written in XS
and not just pure Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	config=optimize='%{rpmcflags}' \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/JavaScript/Minifier
%{perl_vendorarch}/JavaScript/Minifier/*.pm
%dir %{perl_vendorarch}/auto/JavaScript/Minifier
%dir %{perl_vendorarch}/auto/JavaScript/Minifier/XS
%{perl_vendorarch}/auto/JavaScript/Minifier/XS/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/JavaScript/Minifier/XS/*.so
%{_mandir}/man3/*
