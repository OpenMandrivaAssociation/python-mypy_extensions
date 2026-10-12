%global pypi_name mypy_extensions

Name:		python-%{pypi_name}
Version:	1.1.0
Release:	1
Summary:	Type system extensions for the mypy type checker
Group:		Development/Python
License:	MIT
URL:		https://www.mypy-lang.org/
Source0:	https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)

%description
The mypy_extensions module defines extensions to the Python standard
library typing module that are supported by the mypy type checker and
the mypyc compiler.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{py_sitedir}/%{pypi_name}.py
%{py_sitedir}/__pycache__/%{pypi_name}*
%{py_sitedir}/%{pypi_name}-%{version}.dist-info
