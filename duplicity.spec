Summary:	Duplicity backs directories by producing encrypted tar-format volumes and uploading them to a remote or local file server.
Version:	3.0.0
Name:		duplicity
Release:	1
License:	GPLv2
Group:		Archiving/Backup
URL:		https://www.nongnu.org/duplicity/
Source0:  https://gitlab.com/duplicity/duplicity/-/archive/rel.%{version}/duplicity-rel.%{version}.tar.bz2
# Looks like sources below are not updated anymore or updated but with delay. So let's use gitlab archives.
#Source0:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz
#Source1:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz.sig

BuildRequires:  gettext
BuildRequires:	%{_lib}rsync-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(wheel)
#BuildRequires:	python3dist(setuptools-scm)
BuildRequires:  python-setuptools_scm
BuildRequires:	python3dist(pytest-runner)


Requires:	gnupg2
Requires:	ncftp
Requires:	openssh-clients
Requires:	python3dist(boto)
Requires:	python3dist(lockfile)
Requires:	rsync
Requires:	python3dist(pygobject)
Requires:	python3dist(paramiko)
Requires:	python3dist(pexpect)
Requires: python3dist(fasteners)


%description
Duplicity incrementally backs up files and directory by encrypting tar-format
volumes with GnuPG and uploading them to a remote (or local) file server. In
theory many remote backends are possible; right now local, ssh/scp, ftp, and
rsync backends are written. Because duplicity uses librsync, the incremental
archives are space efficient and only record the parts of files that have
changed since the last backup.  Currently duplicity supports deleted files,
full unix permissions, directories, symbolic links, fifos, etc., but not hard
links.

%prep
%autosetup -n %{name}-rel.%{version} -p1

%build
%py_build

%install
%py_install

#handle docs in files section
rm -Rf %{buildroot}%{_docdir}

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%{_mandir}/man1/%{name}*
%{_bindir}/duplicity
%{python_sitearch}/duplicity/
%{python_sitearch}/duplicity-%{version}.dist-info

%changelog
* Wed Jun 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.19-1
+ Revision: 805384
- version update 0.6.19

* Fri Mar 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.18-1
+ Revision: 781769
- version update 0.6.18

* Mon Nov 28 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.6.17-1
+ Revision: 734952
- version update

* Fri Oct 07 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6.15-1
+ Revision: 703460
- New version: 0.6.15

* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.6.12-1
+ Revision: 645167
- update to new version 0.6.12

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.6.08b-2mdv2011.0
+ Revision: 592382
- rebuild for python 2.7

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Update to release 0.6.08b.

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 0.6.07-1mdv2010.1
+ Revision: 513072
- update to new version 0.6.07

  + Michael Scherer <misc@mandriva.org>
    - clean old check on unsupported versions

* Fri Nov 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.06-1mdv2010.1
+ Revision: 465924
- update to new version 0.6.06

* Sat Aug 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.05-1mdv2010.0
+ Revision: 422302
- update to new version 0.6.05

* Wed Aug 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.04-1mdv2010.0
+ Revision: 415724
- update to new version 0.6.04

* Fri Jul 31 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.03-1mdv2010.0
+ Revision: 405214
- update to new version 0.6.03

* Sat Jul 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.01-1mdv2010.0
+ Revision: 392364
- update to new version 0.6.01

* Tue Jun 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.00-1mdv2010.0
+ Revision: 384470
- update to new version 0.6.00

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.18-1mdv2010.0
+ Revision: 378386
- update to new version 0.5.18

* Tue May 05 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.17-1mdv2010.0
+ Revision: 372223
- update to new version 0.5.17

* Mon Mar 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.12-1mdv2009.1
+ Revision: 355821
- update to new version 0.5.12

* Sat Mar 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.11-1mdv2009.1
+ Revision: 355055
- update to new version 0.5.11

* Sat Feb 14 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.08-1mdv2009.1
+ Revision: 340252
- 0.5.08
- fixed the spec file

* Fri Jan 30 2009 Jérôme Soyer <saispo@mandriva.org> 0.5.06-1mdv2009.1
+ Revision: 335634
- import duplicity

