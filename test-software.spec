Summary: A dummy application
Name: test-software
Version: 1.0
Release: 1
Copyright: GPL
Group: System/Base
Source0: test-software-1.0.zip
URL: https://github.com/jstuart/build-test-package
Distribution: Red Hat
Vendor: James
Packager: James Stuart <james@stuart.name>
Arch: noarch

%description
This is a dummy application

%prep
%setup

%install
install -m 0755 -d %{buildroot}/opt/test-software
install -m 0644 *.jar %{buildroot}/opt/test-software

%files
/opt/test-software