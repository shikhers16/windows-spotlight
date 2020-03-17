# -*- mode: python -*-

block_cipher = None


added_files = [
         ( 'files/history.json', './files'),
         ( 'files/user.json', './files'),
         ( 'files/wallpaper.jpeg', './files'),
         ('icons/camera.png', './icons'),
         ('icons/heart.png', './icons'),
         ('icons/broken-heart.png', './icons'),
         ('icons/arrow-left.png', './icons'),
         ('icons/arrow-right.png', './icons'),
         ('icons/bing.png', './icons'),
         ('icons/author.png', './icons'),
         ]

a = Analysis(['app.py'],
             pathex=['S:\\Shikher-Srivastava\\Fun\\Code\\spotlight'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Windows Spotlight',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='S:\\Shikher-Srivastava\\Fun\\Code\\windows-spotlight\\windows-spotlight\\spotlight.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Windows Spotlight')
