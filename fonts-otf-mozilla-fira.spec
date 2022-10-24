%define fname mozilla-fira

Name: fonts-otf-%fname
Version: 4.301
Release: alt1

Summary: Fira Font Family
License: OFL-1.1-no-RFN
Group: System/Fonts/True type

Url: https://github.com/bBoxType/FiraSans
Source0: %name-%version.tar
Source1: LICENSE

BuildArch: noarch
BuildRequires: rpm-build-fonts >= 0.4
Requires(pre,postun): fontconfig >= 2.4.2

%description
Set of Fira family fonts (ex Mozilla Fira)
Fira Sans 4.3 + Fira Code 3.2 + Fira Mono 3.2

%prep
%setup
cp -a %SOURCE1 .

%install
%otf_fonts_install %fname

%files -f %fname.files
%doc LICENSE

%changelog
* Mon Oct 24 2022 Ivan G <lordvivec@mail.ru> 4.301-alt1
- Fira Sans 4.3(update) + Fira Code 3.2(new) + Fira Mono 3.2(update)

* Thu Apr 04 2019 Michael Shigorin <mike@altlinux.org> 2:3.111-alt2
- revert to 3.111: 4.202 got buggy Cyrillic Capital Letter SHCH
  + NB: should rather be upgraded to Carrois Fira though!

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1:4.202-alt1
- 4.202 (upstream tag, yay!)

* Sun Aug 31 2014 Michael Shigorin <mike@altlinux.org> 1:3.111-alt1
- 3.111 (wish upstream used tags though)

* Thu Jun 05 2014 Michael Shigorin <mike@altlinux.org> 1:3.108-alt1
- 3.108 built from upstream git
  + fixes https://github.com/mozilla/Fira/issues/39
- reworked build appropriately

* Fri May 30 2014 Michael Shigorin <mike@altlinux.org> 20130925-alt1
- built for ALT Linux (description from fedora spec)

