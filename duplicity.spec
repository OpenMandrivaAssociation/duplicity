Summary:	Untrusted/encrypted backup using rsync algorithm
Version:	0.6.18
Name:		duplicity
Release:	1
License:	GPLv2
Group:		Archiving/Backup
URL:		http://www.nongnu.org/duplicity/
Source0:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz
Source1:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz.sig
# (misc) patch was sent upstream : https://bugs.launchpad.net/duplicity/+bug/518629
Patch0:		patch-64bits.patch
Requires:	gnupg
BuildRequires:	python-devel
BuildRequires:	librsync-devel

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

%setup -q
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --prefix=%{buildroot}%{_prefix}

rm -Rf %{buildroot}%{_datadir}/doc/duplicity-%{version}

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG COPYING README tarfile-LICENSE
%{_bindir}/rdiffdir
%{_bindir}/duplicity
%{_mandir}/man1/*
%{py_platsitedir}/duplicity
%{py_platsitedir}/*.egg-info
