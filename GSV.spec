from importlib.util import find_spec
from pathlib import Path


project_dir = Path(SPECPATH)
src_dir = project_dir / "src"
hooks_dir = project_dir / "hooks"

flet_cli_spec = find_spec("flet_cli.cli")

if flet_cli_spec is None or flet_cli_spec.origin is None:
    raise RuntimeError(
        "Не удалось найти flet-cli"
    )

flet_cli_dir = Path(
    flet_cli_spec.origin
).parent

flet_hooks_dir = (
    flet_cli_dir
    / "__pyinstaller"
)


a =  Analysis(
    [
        str(
            src_dir
            / "main.py"
        )
    ],
    pathex=[
        str(src_dir)
    ],
    binaries=[],
    datas=[
        (
            str(
                src_dir
                / "assets"
            ),
            "assets"
        )
    ],
    hiddenimports=[
        "flet_desktop",
        "flet_desktop.version",
    ],
    hookspath=[
        str(hooks_dir),
        str(flet_hooks_dir),
    ],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "pygments",
    ],
    noarchive=False,
)

pyz = PYZ(
    a.pure
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="Game Settings Vault",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    icon=str(
        src_dir
        / "assets"
        / "icon.ico"
    ),
)