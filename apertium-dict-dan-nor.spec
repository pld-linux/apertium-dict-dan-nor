Summary:	Danish-Norwegian language pair for Apertium
Summary(pl.UTF-8):	Para języków duński-norweski dla Apertium
%define	lpair	dan-nor
Name:		apertium-dict-%{lpair}
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	9d2e25d448c91f88b20cbd8923e707a9
Patch0:		%{name}-versions.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	apertium-lex-tools
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox-devel >= 3.2.0
BuildRequires:	vislcg3 >= 0.9.7.5129
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Danish and Norwegian (both Nynorsk and Bokmaal), morphological
analysis or part-of-speech tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między duńskim a noweskim (zarówno nynorsk, jak i bokmaal), a także
analizy morfologicznej lub oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/nno-dan.mode
%{_datadir}/apertium/modes/nob-dan.mode
