Name:           perl-Crypt-OpenSSL-Random
Version:        0.04
Release:        9.1%{?dist}
Summary:        Perl interface to OpenSSL for Random
License:        GPL+ or Artistic 
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-OpenSSL-Random/
Source0:        http://www.cpan.org/authors/id/I/IR/IROBERTS/Crypt-OpenSSL-Random-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl openssl-devel perl(ExtUtils::MakeMaker)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Crypt::OpenSSL::Random - Routines for accessing the OpenSSL
pseudo-random number generator

%prep
%setup -q -n Crypt-OpenSSL-Random-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes
%doc LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.04-9.1
- Rebuilt for RHEL 6

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.04-9
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.04-6
- rebuild with new openssl

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-5
- rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.04-4
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.04-3
 - Rebuild for deps

* Wed May 23 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.04-2
- Add document file: LICENSE

* Mon May 21 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.04-1
- Update to upstream 0.4 with proper license

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.03-3
- BuildRequire perl(ExtUtils::MakeMaker)

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.03-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.03-1
- Initial version
