Name:           rnote
Version:        0.11.0
Release:        %autorelease
Summary:        Sketch and take handwritten notes.
License:        GPL-3.0
URL:            https://github.com/flxzt/rnote
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Requires:       gtk4 libadwaita glib2 poppler-glib
BuildRequires:  cargo rustc
BuildRequires:  gcc gcc-c++ clang clang-devel python3 make cmake meson git appstream gettext desktop-file-utils shared-mime-info kernel-devel gtk4-devel libadwaita-devel poppler-glib-devel poppler-data alsa-lib-devel


%description
Rnote is an open-source vector-based drawing app for sketching,
handwritten notes and to annotate documents and pictures. It is
targeted at students, teachers and those who own a drawing tablet
and provides features like Pdf and picture import and export, an
infinite canvas and an adaptive UI for big and small screens.

%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README.md
%doc AUTHORS
%license LICENSE

%{_bindir}/rnote

%{_datadir}/applications/com.github.flxzt.rnote.desktop
%{_datadir}/metainfo/com.github.flxzt.rnote.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/rnote.mo
%{_datadir}/rnote/
%{_datadir}/fonts/rnote-fonts/
%{_datadir}/glib-2.0/schemas/com.github.flxzt.rnote.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.flxzt.rnote.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.flxzt.rnote-symbolic.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/application-rnote.svg
%{_datadir}/mime/packages/com.github.flxzt.rnote.xml