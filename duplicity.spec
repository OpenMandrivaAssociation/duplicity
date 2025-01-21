Summary:	Duplicity backs directories by producing encrypted tar-format volumes and uploading them to a remote or local file server.
Version:	3.0.3.2
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

%patchlist
duplicity-no-Lusrlib.patch

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
