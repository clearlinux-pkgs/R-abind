#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-abind
Version  : 1.4.5
Release  : 49
URL      : https://cran.r-project.org/src/contrib/abind_1.4-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/abind_1.4-5.tar.gz
Summary  : Combine Multidimensional Arrays
Group    : Development/Tools
License  : LGPL-2.0+
BuildRequires : buildreq-R

%description
This is a generalization of 'cbind' and 'rbind'.  Works with
  vectors, matrices, and higher-dimensional arrays.  Also
  provides functions 'adrop', 'asub', and 'afill' for manipulating,
  extracting and replacing data in arrays.

%prep
%setup -q -c -n abind
cd %{_builddir}/abind

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640964062

%install
export SOURCE_DATE_EPOCH=1640964062
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library abind
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library abind
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library abind
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc abind || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/abind/DESCRIPTION
/usr/lib64/R/library/abind/INDEX
/usr/lib64/R/library/abind/Meta/Rd.rds
/usr/lib64/R/library/abind/Meta/features.rds
/usr/lib64/R/library/abind/Meta/hsearch.rds
/usr/lib64/R/library/abind/Meta/links.rds
/usr/lib64/R/library/abind/Meta/nsInfo.rds
/usr/lib64/R/library/abind/Meta/package.rds
/usr/lib64/R/library/abind/NAMESPACE
/usr/lib64/R/library/abind/R/abind
/usr/lib64/R/library/abind/R/abind.rdb
/usr/lib64/R/library/abind/R/abind.rdx
/usr/lib64/R/library/abind/help/AnIndex
/usr/lib64/R/library/abind/help/abind.rdb
/usr/lib64/R/library/abind/help/abind.rdx
/usr/lib64/R/library/abind/help/aliases.rds
/usr/lib64/R/library/abind/help/paths.rds
/usr/lib64/R/library/abind/html/00Index.html
/usr/lib64/R/library/abind/html/R.css
/usr/lib64/R/library/abind/sccversion.txt
/usr/lib64/R/library/abind/svnversion.txt
/usr/lib64/R/library/abind/tests/abind.R
/usr/lib64/R/library/abind/tests/abind.Rout.save
/usr/lib64/R/library/abind/tests/adrop.R
/usr/lib64/R/library/abind/tests/adrop.Rout.save
/usr/lib64/R/library/abind/tests/afill.R
/usr/lib64/R/library/abind/tests/afill.Rout.save
/usr/lib64/R/library/abind/tests/asub.R
/usr/lib64/R/library/abind/tests/asub.Rout.save
/usr/lib64/R/library/abind/tests/dnns.R
/usr/lib64/R/library/abind/tests/dnns.Rout.save
/usr/lib64/R/library/abind/tests/tmp.txt
