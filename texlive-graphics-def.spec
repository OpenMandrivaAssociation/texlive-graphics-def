Name:		texlive-graphics-def
Version:	64487
Release:	2
Summary:	Colour and graphics option files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphics-def
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-def.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-def.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle is a combined distribution consisting of dvips.def,
pdftex.def, luatex.def, xetex.def, dvipdfmx.def, and
dvisvgm.def driver option files for the LaTeX graphics and
color packages. It is hoped that by combining their source
repositories at https://github.com/latex3/graphics-def it will
be easier to coordinate updates.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/graphics-def
%doc %{_texmfdistdir}/doc/latex/graphics-def

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
