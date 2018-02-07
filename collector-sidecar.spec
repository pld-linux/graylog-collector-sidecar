# TODO:
# - build from source: https://github.com/Graylog2/collector-sidecar#compile

Summary:	Manage log collectors through Graylog
Name:		collector-sidecar
Version:	0.1.4
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/Graylog2/collector-sidecar/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8728b5e9310210e91f9a1f5c46160d8d
URL:		https://github.com/Graylog2/collector-sidecar
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Graylog Collector Sidecar is a supervisor process for 3rd party
log collectors like NXLog. The Sidecar program is able to fetch
configurations from a Graylog server and render them as a valid
configuration file for various log collectors. You can think of it
like a centralized configuration management system for your log
collectors.

%prep
%setup -qc
%ifarch %{ix86}
mv %{name}/%{version}/linux/386/graylog-collector-sidecar .
%endif
%ifarch %{x8664}
mv %{name}/%{version}/linux/amd64/graylog-collector-sidecar .
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p graylog-collector-sidecar $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/graylog-collector-sidecar
