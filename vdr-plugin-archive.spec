
%define plugin	archive
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	10

Summary:	VDR plugin: Multimedia-Archive
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://schwatke.net/
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi
Requires(pre):	rpm-helper

%description
Multimedia-Archive plugin for Klaus Schmidinger's Video Disc
Recorder.

%prep
%setup -q -n %plugin-%version
rm scripts/new_entry scripts/sort_archive

%build
%vdr_plugin_build
cd scripts
g++ %optflags -o new_entry new_entry.cc
g++ %optflags -o sort_archive sort_archive.cc

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%plugin
install -m755 scripts/new_entry %{buildroot}%{_vdr_plugin_cfgdir}/%plugin
install -m755 scripts/sort_archive %{buildroot}%{_vdr_plugin_cfgdir}/%plugin
touch %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}/archive

%clean
rm -rf %{buildroot}

%post
%create_ghostfile %{_vdr_plugin_cfgdir}/%{plugin}/archive vdr vdr 644
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%attr(-,vdr,vdr) %dir %{_vdr_plugin_cfgdir}/%{plugin}
%{_vdr_plugin_cfgdir}/%{plugin}/new_entry
%{_vdr_plugin_cfgdir}/%{plugin}/sort_archive
%attr(644,vdr,vdr) %ghost %{_vdr_plugin_cfgdir}/%{plugin}/archive


