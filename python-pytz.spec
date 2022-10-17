# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pytz
Epoch: 100
Version: 2022.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: World timezone definitions, modern and historical
License: MIT
URL: https://github.com/stub42/pytz/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4 or
higher. It also solves the issue of ambiguous times at the end of
daylight saving time, which you can read more about in the Python
Library Reference (datetime.tzinfo).

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pytz
Summary: World timezone definitions, modern and historical
Requires: python3
Provides: python3-pytz = %{epoch}:%{version}-%{release}
Provides: python3dist(pytz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pytz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pytz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pytz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pytz) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pytz
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4 or
higher. It also solves the issue of ambiguous times at the end of
daylight saving time, which you can read more about in the Python
Library Reference (datetime.tzinfo).

%files -n python%{python3_version_nodots}-pytz
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pytz
Summary: World timezone definitions, modern and historical
Requires: python3
Provides: python3-pytz = %{epoch}:%{version}-%{release}
Provides: python3dist(pytz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pytz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pytz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pytz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pytz) = %{epoch}:%{version}-%{release}

%description -n python3-pytz
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4 or
higher. It also solves the issue of ambiguous times at the end of
daylight saving time, which you can read more about in the Python
Library Reference (datetime.tzinfo).

%files -n python3-pytz
%license LICENSE.txt
%{python3_sitelib}/*
%endif

%changelog
