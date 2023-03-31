%global pypi_name mypy_extensions

Name:           python-%{pypi_name}
Version:        0.4.3
Release:        2
Summary:        Experimental type system extensions for programs checked with the mypy typechecker
Group:          Development/Python
License:        MIT
URL:            http://www.mypy-lang.org/
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}
%{?python_provide:%python_provide python3-mypy-extensions}

%description
Mypy Extensions The "mypy_extensions" module defines experimental extensions to
the standard "typing" module that are supported by the mypy typechecker.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
