#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A pygments lexer for pytest output
Summary(pl.UTF-8):	Lexer pygments do wyjścia pytesta
Name:		python-pygments_pytest
# keep 1.x here for python2 support
Version:	1.3.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pygments-pytest/
Source0:	https://files.pythonhosted.org/packages/source/p/pygments-pytest/pygments_pytest-%{version}.tar.gz
# Source0-md5:	e51a2e259bfd4eb4f93fc4f626e05e17
URL:		https://pypi.org/project/pygments-pytest/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides a pygments lexer called pytest.

%description -l pl.UTF-8
Ta biblioteka udostępnia lexer pygments o nazwie pytest.

%package -n python3-pygments_pytest
Summary:	A pygments lexer for pytest output
Summary(pl.UTF-8):	Lexer pygments do wyjścia pytesta
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pygments_pytest
This library provides a pygments lexer called pytest.

%description -n python3-pygments_pytest -l pl.UTF-8
Ta biblioteka udostępnia lexer pygments o nazwie pytest.

%prep
%setup -q -n pygments_pytest-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/pygments_pytest.py[co]
%{py_sitescriptdir}/pygments_pytest-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pygments_pytest
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/pygments_pytest.py
%{py3_sitescriptdir}/__pycache__/pygments_pytest.cpython-*.py[co]
%{py3_sitescriptdir}/pygments_pytest-%{version}-py*.egg-info
%endif
