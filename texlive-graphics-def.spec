%global tl_name graphics-def
%global tl_revision 76719

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Colour and graphics option files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphics-def
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-def.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-def.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle is a combined distribution consisting of dvips.def,
pdftex.def, luatex.def, xetex.def, dvipdfmx.def, and dvisvgm.def driver
option files for the LaTeX graphics and color packages. It is hoped that
by combining their source repositories at
https://github.com/latex3/graphics-def it will be easier to coordinate
updates.

