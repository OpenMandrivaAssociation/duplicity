Summary:	Duplicity backs directories by producing encrypted tar-format volumes and uploading them to a remote or local file server.
Version:	3.0.4.1
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
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pytest-runner)


Requires:	gnupg2

Requires:	%{name}-backend = %{EVRD}

%patchlist
duplicity-no-Lusrlib.patch
duplicity-relax-atom-dep.patch

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

D="$(pwd)"
cd %{buildroot}%{python_sitearch}/duplicity/backends
for i in *; do
	if echo $i |grep -q 'backend.py$' && [ "$i" != "_testbackend.py" ]; then
		BACKEND="$(echo ${i/backend.py/} |sed -e 's,_$,,')"
		case $BACKEND in
		gio)
			EXTRA_DEPS="Requires: python%{pyver}dist(pygobject)"
			;;
		rsync)
			EXTRA_DEPS="Requires: rsync"
			;;
		ssh*)
			EXTRA_DEPS="Requires: openssh-clients"
			;;
		ncftp)
			EXTRA_DEPS="Requires: ncftp"
			;;
		lftp)
			EXTRA_DEPS="Requires: lftp"
			;;
		*)
			EXTRA_DEPS=""
			;;
		esac
		sed -e 's,^@,%%,g' >%{specpartsdir}/${BACKEND}.specpart <<EOF
@package backend-${BACKEND}
Summary: ${BACKEND} backend for the duplicity backup tool
Group:	Archiving/Backup
Provides: %{name}-backend = %{EVRD}
$EXTRA_DEPS

@description backend-${BACKEND}
${BACKEND} backend for the duplicity backup tool

@files backend-${BACKEND}
%{python_sitearch}/duplicity/backends/$i
EOF
	else
		echo %{python_sitearch}/duplicity/backends/$i >>$D/backends-core.files
	fi
done


%files -f %{name}.lang -f backends-core.files
%doc CHANGELOG.md README.md
%{_mandir}/man1/%{name}*
%{_bindir}/duplicity
%dir %{python_sitearch}/duplicity
%{python_sitearch}/duplicity/*.so
%{python_sitearch}/duplicity/*.py
%{python_sitearch}/duplicity/*.c
%{python_sitearch}/duplicity/__pycache__
%{python_sitearch}/duplicity-%{version}.dist-info
%dir %{python_sitearch}/duplicity/backends
