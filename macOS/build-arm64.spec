# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['Notepad==.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tkinter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Notepad==',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # This flag is equivalent to --windowed
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='arm64',
    codesign_identity=None,
    entitlements_file=None,
    icon=['Notepad.icns'],  # Icon for the executable
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Notepad==',
)
app = BUNDLE(
    coll,
    name='Notepad==.app',
    icon='Notepad.icns',  # Icon for the application bundle
    bundle_identifier=None,
)