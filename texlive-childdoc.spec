%global tl_name childdoc
%global tl_revision 74758

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.1
Release:	%{tl_revision}.1
Summary:	Directly compile \included child documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/childdoc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/childdoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/childdoc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/childdoc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX2e package enables the direct compilation of document sections
included by \include to individual files.

