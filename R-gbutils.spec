#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gbutils
Version  : 0.4.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/gbutils_0.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gbutils_0.4-0.tar.gz
Summary  : Simulation of Real and Complex Numbers and Small Programming
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Rdpack
BuildRequires : R-Rdpack
BuildRequires : buildreq-R

%description
magnitude and arguments. Optionally, the magnitudes and/or arguments may
       be fixed in almost arbitrary ways. Plot density and distribution
       functions with automatic selection of suitable regions.  Small programming

%prep
%setup -q -c -n gbutils
cd %{_builddir}/gbutils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589587355

%install
export SOURCE_DATE_EPOCH=1589587355
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbutils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbutils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gbutils || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gbutils/DESCRIPTION
/usr/lib64/R/library/gbutils/INDEX
/usr/lib64/R/library/gbutils/Meta/Rd.rds
/usr/lib64/R/library/gbutils/Meta/features.rds
/usr/lib64/R/library/gbutils/Meta/hsearch.rds
/usr/lib64/R/library/gbutils/Meta/links.rds
/usr/lib64/R/library/gbutils/Meta/nsInfo.rds
/usr/lib64/R/library/gbutils/Meta/package.rds
/usr/lib64/R/library/gbutils/Meta/vignette.rds
/usr/lib64/R/library/gbutils/NAMESPACE
/usr/lib64/R/library/gbutils/NEWS.md
/usr/lib64/R/library/gbutils/R/gbutils
/usr/lib64/R/library/gbutils/R/gbutils.rdb
/usr/lib64/R/library/gbutils/R/gbutils.rdx
/usr/lib64/R/library/gbutils/REFERENCES.bib
/usr/lib64/R/library/gbutils/doc/Plot_pdf.R
/usr/lib64/R/library/gbutils/doc/Plot_pdf.Rnw
/usr/lib64/R/library/gbutils/doc/Plot_pdf.pdf
/usr/lib64/R/library/gbutils/doc/index.html
/usr/lib64/R/library/gbutils/help/AnIndex
/usr/lib64/R/library/gbutils/help/aliases.rds
/usr/lib64/R/library/gbutils/help/gbutils.rdb
/usr/lib64/R/library/gbutils/help/gbutils.rdx
/usr/lib64/R/library/gbutils/help/paths.rds
/usr/lib64/R/library/gbutils/html/00Index.html
/usr/lib64/R/library/gbutils/html/R.css
