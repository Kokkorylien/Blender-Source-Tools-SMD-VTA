"""Create the installable Blender ZIP from an explicit public file list."""
import argparse
import ast
import hashlib
from pathlib import Path
import zipfile

SOURCE = Path(__file__).resolve().parents[2]
PYTHON_FILES = (
    "__init__.py", "GUI.py", "datamodel.py", "export_smd.py", "flex.py",
    "import_smd.py", "ordered_set.py", "translations.py", "update.py", "utils.py",
)
PACKAGE_FILES = PYTHON_FILES + (
    "README.md", "README_zh_HANS.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "UPSTREAM.md",
)


def build(destination):
    for name in PYTHON_FILES:
        ast.parse((SOURCE / name).read_text(encoding="utf-8-sig"), filename=name)
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / "io_scene_valvesource.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for name in PACKAGE_FILES:
            entry = zipfile.ZipInfo("io_scene_valvesource/" + name, (2026, 10, 25, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o644 << 16
            package.writestr(entry, (SOURCE / name).read_bytes())
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        for name in PACKAGE_FILES:
            assert package.read("io_scene_valvesource/" + name) == (SOURCE / name).read_bytes()
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".zip.sha256").write_text(
        digest + "  " + archive.name + "\n", encoding="ascii", newline="\n"
    )
    print(f"{archive}: {len(PACKAGE_FILES)} files, {archive.stat().st_size} bytes")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SOURCE / "dist")
    build(parser.parse_args().output)
