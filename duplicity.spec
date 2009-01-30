
Version: 0.5.06
Summary: Untrusted/encrypted backup using rsync algorithm
Name: duplicity
Release: %mkrel 1
URL: http://www.nongnu.org/duplicity/
Source: http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz
Patch0: patch-64bits.patch
License: GPLv2
Group: Archiving/Backup
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: librsync, python, gnupg
BuildRequires: python-devel, librsync-devel

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server.  In theory many remote backends are possible;
right now local, ssh/scp, ftp, and rsync backends are written.
Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup.  Currently duplicity supports deleted files, full
unix permissions, directories, symbolic links, fifos, etc., but not
hard links.

%prep
%setup -q
%patch0 -p0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --prefix=$RPM_BUILD_ROOT/usr
%find_lang %{name}
mv $RPM_BUILD_ROOT/%{_datadir}/doc/duplicity-0.5.06 $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGELOG COPYING README
%{_bindir}/rdiffdir
%{_bindir}/duplicity
%{_mandir}/man1/*
%{_libdir}/
