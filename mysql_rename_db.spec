Name:           mysql_rename_db
Version:        $VERSION
Release:        1%{?dist}
Summary:        Clone of postmark for local installations

Group:          Development Tools
License:        none
URL:            https://github.com/SuRaMoN/mysql_rename_db
Source0:        mysql_rename_db-$VERSION.tar.gz

BuildRequires:  make
Requires:       mysql-libs

%description
Easy way to rename mysql databases


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}


%clean
make clean DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}


%files
%defattr(-,root,root,-)
%{_bindir}/mysql_rename_db


%changelog
