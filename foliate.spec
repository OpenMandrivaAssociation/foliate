Name:           foliate
Version:        2.0.0
Release:        1
Summary:        A simple and modern GTK eBook reader
Group:          Office/Utilities
License:        GPLv3
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gjs
BuildRequires: ninja
BuildRequires: meson
BuildRequires: gettext
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(webkit2gtk-4.0)

Requires: gjs
Requires: webkit2
# Needed for mobipocket (.mobi) and Kindle File Format (.azw, .azw3)
Requires: python
# Optional for text-to-speech
Recommends: espeak
Recommends: gspell-i18n

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep
%setup -q
2to3 --write --nobackups --no-diffs src/assets/KindleUnpack/mobiml2xhtml.py
sed -i -e '1s/python$/python3/' src/assets/KindleUnpack/*.py
%autopatch -p1

%build
%meson
%ninja -C build

%install
%ninja -C build install

pushd %{buildroot}%{_bindir}
ln -s com.github.johnfactotum.Foliate foliate
popd

%find_lang com.github.johnfactotum.Foliate

%files -f com.github.johnfactotum.Foliate.lang
%doc README.md COPYING
%{_bindir}/foliate
%{_bindir}/com.github.johnfactotum.Foliate
%{_datadir}/applications/com.github.johnfactotum.Foliate.desktop
%{_datadir}/foliate/com.github.johnfactotum.Foliate.data.gresource
%{_datadir}/foliate/com.github.johnfactotum.Foliate.src.gresource
%{_datadir}/glib-2.0/schemas/com.github.johnfactotum.Foliate.gschema.xml
%{_datadir}/foliate/assets/*
%{_iconsdir}/hicolor/*/apps/com.github.johnfactotum.Foliate*.svg
%{_datadir}/metainfo/com.github.johnfactotum.Foliate.appdata.xml
