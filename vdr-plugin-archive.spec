%define plugin	archive

Summary:	VDR plugin: Multimedia-Archive
Name:		vdr-plugin-%plugin
Version:	0.0.2
Release:	22
Group:		Video
License:	GPL
URL:		http://schwatke.net/
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		archive-includes.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires(pre):	rpm-helper

%description
Multimedia-Archive plugin for Klaus Schmidinger's Video Disc
Recorder.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
rm scripts/new_entry scripts/sort_archive
%vdr_plugin_prep

%build
%vdr_plugin_build
cd scripts
g++ %optflags -o new_entry new_entry.cc
g++ %optflags -o sort_archive sort_archive.cc

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/%plugin
install -m755 scripts/new_entry %{buildroot}%{vdr_plugin_cfgdir}/%plugin
install -m755 scripts/sort_archive %{buildroot}%{vdr_plugin_cfgdir}/%plugin
touch %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}/archive

%post
%create_ghostfile %{vdr_plugin_cfgdir}/%{plugin}/archive vdr vdr 644

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{vdr_plugin_cfgdir}/%{plugin}
%{vdr_plugin_cfgdir}/%{plugin}/new_entry
%{vdr_plugin_cfgdir}/%{plugin}/sort_archive
%attr(644,vdr,vdr) %ghost %{vdr_plugin_cfgdir}/%{plugin}/archive




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-19mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- add more missing includes (includes.patch)

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-18mdv2009.1
+ Revision: 359403
- add missing includes (includes.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-17mdv2009.0
+ Revision: 197896
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-16mdv2009.0
+ Revision: 197627
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-15mdv2008.1
+ Revision: 145015
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-14mdv2008.1
+ Revision: 144971
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-13mdv2008.1
+ Revision: 103056
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-12mdv2008.0
+ Revision: 49965
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-11mdv2008.0
+ Revision: 42052
- rebuild for new vdr

* Tue May 15 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-10mdv2008.0
+ Revision: 27091
- rebuild

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2008.0
+ Revision: 22696
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2007.0
+ Revision: 90887
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2007.1
+ Revision: 73944
- rebuild for new vdr
- Import vdr-plugin-archive

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- use _ prefix for system path macros

* Sun Jun 11 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

