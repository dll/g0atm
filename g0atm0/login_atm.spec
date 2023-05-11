# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['./g0atm0/customer.py'],
    pathex=['./venv/Lib/site-packages','./g0atm0/customer.py','./g0atm0/dbutil.py','./g0atm0/pgini.py'],
    binaries=[],
    datas=[('./g0atm0/pg.env','./g0atm0/pg.env')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='login_atm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
