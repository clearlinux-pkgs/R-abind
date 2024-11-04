#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v19
# autospec commit: f35655a
#
Name     : R-abind
Version  : 1.4.8
Release  : 56
URL      : https://cran.r-project.org/src/contrib/abind_1.4-8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/abind_1.4-8.tar.gz
Summary  : Combine Multidimensional Arrays
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a generalization of 'cbind' and 'rbind'.  Works with
  vectors, matrices, and higher-dimensional arrays (aka tensors).
  Also provides functions 'adrop', 'asub', and 'afill' for
  manipulating, extracting and replacing data in arrays.

%prep
%setup -q -n abind
pushd ..
cp -a abind buildavx2
popd
pushd ..
cp -a abind buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726181750

%install
export SOURCE_DATE_EPOCH=1726181750
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/abind/DESCRIPTION
/usr/lib64/R/library/abind/INDEX
/usr/lib64/R/library/abind/LICENSE
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
