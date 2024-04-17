%global debug_package %{nil}

Name:           foliate
Version:        3.1.1
Release:        1
Summary:        A simple and modern GTK eBook reader
Group:          Office/Utilities
License:        GPLv3
URL:            https://johnfactotum.github.io/foliate/
# Foliate devs need to unserstand that internal submodules, should be released together with the main project as example in tarball.
Source0:	foliate-3.1.1.tar.xz
#Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
# Needed submodule
#Source1:        https://github.com/johnfactotum/foliate-js/archive/foliate-js-f75fbba096e8fc1c775ea1c162fe1d3322cd5121.tar.gz
Patch0:		fix-typelib.patch

BuildRequires:  appstream-util
BuildRequires:	gjs
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:  pkgconfig(gtk4)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(webkitgtk-6.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	xdg-dbus-proxy
BuildRequires:  locales-extra-charsets

Requires: gjs
Requires: typelib(WebKit) = 6.0
Requires: %{_lib}webkit2gtk-gir6.0
Requires: %{_lib}adwaita-gir1
Requires: xdg-dbus-proxy
# Needed for mobipocket (.mobi) and Kindle File Format (.azw, .azw3)
Requires: python
Requires: iso-codes
# Optional for text-to-speech
Recommends: espeak
Recommends: gspell-i18n
Recommends: noto-coloremoji-fonts

Provides:       bundled(%{name}-js)

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep
	
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

#pushd %{buildroot}%{_bindir}
#ln -s com.github.johnfactotum.Foliate foliate
#popd

%find_lang com.github.johnfactotum.Foliate

%files -f com.github.johnfactotum.Foliate.lang
%doc README.md COPYING
%{_bindir}/foliate
#{_bindir}/com.github.johnfactotum.Foliate
%{_datadir}/applications/com.github.johnfactotum.Foliate.desktop
%{_datadir}/com.github.johnfactotum.Foliate/*
%{_datadir}/glib-2.0/schemas/com.github.johnfactotum.Foliate.gschema.xml
%{_iconsdir}/hicolor/*/apps/com.github.johnfactotum.Foliate*.svg
%{_datadir}/metainfo/com.github.johnfactotum.Foliate.metainfo.xml
