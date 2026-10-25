# Blender Source Tools — SMD/VTA Workflow Edition

[简体中文](README_zh_HANS.md) · **English**

An independently maintained modification of **Blender Source Tools**, focused on faster mesh-only export, controlled shape key export, and easier export configuration for Source engine workflows.

**Target Blender version: 4.0.2.** The bundled upstream metadata identifies the base as **Blender Source Tools 3.2.6**. This edition is maintained by [Kokkorylien](https://github.com/Kokkorylien); it is an unofficial derivative.

## What the original add-on provides

Blender Source Tools provides SMD/VTA and DMX import/export, skeletal animation and flex tools, and QC-related tools for Valve engine asset workflows. This edition retains that foundation. The changes below focus on mesh SMD and shape key VTA export; QC generation, compilation workflows, and the existing vertex animation tools retain their upstream behavior.

## Changes in this edition

### Independent SMD/VTA settings for each exportable

Each mesh or collection exportable has its own output mode:

| Mode | Output and behavior |
| --- | --- |
| SMD + VTA | Export the mesh SMD and, when exportable shape keys exist, the shape key VTA. |
| SMD only | Export the reference mesh and **skip shape key baking and VTA generation**. |
| VTA only | Export the shape key VTA without rewriting the mesh SMD. |

**SMD-only mode removes the expensive per-shape baking work.** It keeps the shape keys in the Blender file and evaluates the reference mesh from the first, base shape. This makes mesh export practical for objects containing hundreds or thousands of shape keys. Normal mesh processing, modifiers, and other export work still take time.

For VTA-only export, the existing mesh SMD must match the geometry and vertex ordering used for the VTA bake. Re-export the SMD when changes affect that correspondence.

### Export a shape key range while keeping the rest

Set **VTA First Shape** and **VTA Last Shape** independently for each exportable. The range includes both endpoints.

For this shape key list:

~~~text
basis, blink, angry, smile_1, smile_2, shape1, shape2, shapeblank, shape3
~~~

Selecting **shape1 → shapeblank** produces:

| VTA frame | Shape |
| --- | --- |
| 0 | basis |
| 1 | shape1 |
| 2 | shape2 |
| 3 | shapeblank |

Frame 0 always uses the object's first shape key, normally Basis. The selected non-base shapes are numbered consecutively from frame 1. Other shape keys remain available in the Blender file and are excluded from this export's shape baking.

Leaving the first or last endpoint blank uses the beginning or end of the available non-base shapes. Invalid or reversed endpoints are reported before export.

For collections containing multiple meshes, their shape key lists may differ. Names are merged in the exporter's object traversal order, preserving the first occurrence of each name. The range applies to that merged list; a mesh without a particular shape contributes its base geometry for that frame. Each mesh supplies its own first shape key for frame 0. Review the displayed range and frame count when configuring a collection.

**Keep the QC flex frame references consistent with the exported VTA.** This edition leaves QC adjustments to the user.

### Confirm large VTA exports before baking

SMD + VTA and VTA-only exports are checked before the expensive bake begins. The confirmation shows shape frame counts and an estimated file size so an accidental export can be cancelled.

The scene-level confirmation settings default to:

| Setting | When confirmation is requested |
| --- | --- |
| Shape frame count: 64 | Any exportable would write more than 64 non-base shape frames. |
| Estimated size: 128 MB | The estimated total VTA size for the operation exceeds 128 MB, using 1 MB = 1,024 × 1,024 bytes. |

These values determine **when Blender asks for confirmation**; they do not limit how much can be exported after confirmation. Set a value to 0 to disable that particular check. The size is a conservative estimate, and the actual file can be smaller. Background exports log a warning and continue without an interactive dialog.

### Optional Skip Shape Normals

Each exportable can enable **Skip Shape Normals**:

- Shape frames reuse the base mesh normals.
- Only vertices whose positions change are written for those frames.
- Changes affecting normals alone are ignored, and per-shape normal calculation is skipped.

VTA still contains the normal columns required by the format. With this option enabled, exported flexes do not update lighting normals to follow their deformed shapes. Leave it disabled when those normal changes matter.

### Easier selection and configuration

The **Selected Exportable** panel follows the object or collection chosen in the scene, including meshes hidden with H or disabled in the viewport.

- Selecting a collection resolves that collection's exportable.
- Selecting a mesh resolves its containing exportable collection or collections. A different collection sharing the mesh's name is not treated as a match.
- Selecting a row in **Exportables** also selects the configuration target, while preserving the scene's selected objects, active object, and active collection.
- Changing the scene selection resumes scene-based target selection.
- Export list refreshes preserve the chosen row by object or collection identity.

The selected panel and export menu provide quick access to the resolved target's SMD/VTA mode and normal setting. The export list also shows each applicable item's mode and Skip Normals flag alongside its shape count.

### Batch export configuration

The **Exportables → Batch Export Settings** controls apply SMD/VTA mode and Skip Shape Normals to the selected exportable targets or to all applicable exportables. Selected targets can come from the scene selection or the independently chosen export list row.

Armature animation items are excluded from these mesh/VTA batch settings. Shape range endpoints remain individual settings.

### Armature animation export from collections

An armature's action or NLA animation exportable remains accessible when the armature is inside an ordinary or nested collection. Moving the armature into the scene's root collection is no longer required.

Select the armature to access its animation exportable. Selecting a collection continues to target that collection's export.

### Simplified Chinese interface and tooltips

This edition adds Simplified Chinese translations for the add-on's interface strings, settings, hover descriptions, and messages. Terminology is adapted to Valve workflows; for example, Source engine is rendered as “起源引擎”.

## Installation and quick start

1. In Blender 4.0.2, disable the existing Blender Source Tools installation if present. Both editions use the module name `io_scene_valvesource`.
2. Open **Edit → Preferences → Add-ons → Install**, choose this edition's installable ZIP, and enable Blender Source Tools.
3. Use a release ZIP containing the `io_scene_valvesource/` folder. GitHub's automatically generated source archive is a repository snapshot and may have a different directory layout.
4. In **Scene Properties → Source Engine Export**, set the export path and choose **SMD** as the export format.
5. Select a collection or mesh, or choose a row in **Exportables**. Configure output mode and normals in **Selected Exportable**; use the **SMD / VTA** panel under Exportables for shape range settings.
6. Export through the scene export button or **File → Export → Source Engine**.

To use the Chinese interface, choose Simplified Chinese in Blender's interface language settings and enable interface/tooltips translation.

**[Download updates from this edition's releases](https://github.com/Kokkorylien/Blender-Source-Tools-SMD-VTA/releases).** The add-on's update button opens that page. Download the installable ZIP and install it manually in Blender; the button does not download or overwrite files automatically.

## Credits, source, and license

- **Original add-on:** Blender Source Tools, by **Tom Edwards**. The bundled metadata credits **Grigory Revzin** for translations. Existing upstream contributors and their notices retain their credit.
- **This edition:** SMD/VTA workflow changes and Simplified Chinese localization maintained by **Kokkorylien**.
- **Base version:** 3.2.6, as recorded by the bundled add-on metadata. See [UPSTREAM.md](UPSTREAM.md) for provenance details and modification records.
- **Upstream links:** [website](http://steamreview.org/BlenderSourceTools/) · [version archives](http://steamreview.org/BlenderSourceTools/archives/) · [news and changelog](https://steamcommunity.com/groups/BlenderSourceTools/announcements).

The add-on and this edition's modifications are distributed under the **GNU General Public License, version 2 or any later version (GPL-2.0-or-later)**, following the existing source headers. See [LICENSE](LICENSE) for the GPL v2 text. Bundled MIT-licensed components retain their notices and permissions; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This project is independently maintained and does not claim endorsement by the upstream authors, Valve, or the Blender project. Report issues specific to this edition in this repository.

