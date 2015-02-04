Summary: A dummy application
Name: test-software
Version: 1.0
Release: 1
License: GPL
Group: System/Base
Source0: test-software-1.0.zip
URL: https://github.com/jstuart/build-test-package
Distribution: Red Hat
Vendor: James
Packager: James Stuart <james@stuart.name>
BuildArch: noarch

%description
This is a dummy application

%prep
%setup -q

%build
# Nothing

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}/opt/test-software
install -m 0644 *.jar %{buildroot}/opt/test-software

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/test-software

%changelog
* Wed Feb 04 2015 James Stuart <james@stuart.name> 1.0-1
- Initial release