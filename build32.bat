rmdir /s/q build
del build.zip
C:\Python32_x86\python.exe setup.py build
copy start32.bat build\start.bat
"C:\Program Files\7-Zip\7z" a build.zip build\start.bat "build\exe.win32-3.2"