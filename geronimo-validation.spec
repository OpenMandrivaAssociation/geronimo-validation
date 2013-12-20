%_javapackages_macros
%global spec_ver 1.0
%global spec_name geronimo-validation_%{spec_ver}_spec

Name:           geronimo-validation
Version:        1.1
Release:        10.0%{?dist}
Summary:        Geronimo implementation of JSR 303
License:        ASL 2.0
# should be http://geronimo.apache.org/
URL:            http://apache.org/
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.1/
# tar caf geronimo-validation_1.0_spec-1.1.tar.xz geronimo-validation_1.0_spec-1.1
Source0:        %{spec_name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  geronimo-parent-poms
BuildRequires:  geronimo-osgi-support

%description
This is the Geronimo implementation of JSR-303, the Bean
Validation API specification.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{version}
%pom_xpath_set "pom:project/pom:parent/pom:groupId" org.apache.geronimo.specs
%pom_xpath_set "pom:project/pom:parent/pom:artifactId" specs
%pom_xpath_set "pom:project/pom:parent/pom:version" 1.4
%pom_xpath_inject "pom:project/pom:parent" "<relativePath>../pom.xml</relativePath>"
%pom_xpath_set "pom:project/pom:packaging" jar

%build
%mvn_file : %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE
