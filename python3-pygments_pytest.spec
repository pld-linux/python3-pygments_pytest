Summary:	A pygments lexer for pytest output
Summary(pl.UTF-8):	Lexer pygments do wyjścia pytesta
Name:		python3-pygments_pytest
Version:	2.2.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pygments-pytest/
Source0:	https://files.pythonhosted.org/packages/source/p/pygments-pytest/pygments_pytest-%{version}.tar.gz
# Source0-md5:	387a512e52a3cfbbd612f6f23e760594
URL:		https://pypi.org/project/pygments-pytest/
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a pygments lexer called pytest.

%description -l pl.UTF-8
Ta biblioteka udostępnia lexer pygments o nazwie pytest.

%prep
%setup -q -n pygments_pytest-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pygments_pytest.py
%{py3_sitescriptdir}/__pycache__/pygments_pytest.cpython-*.py[co]
%{py3_sitescriptdir}/pygments_pytest-%{version}-py*.egg-info
