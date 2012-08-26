rmdir /s/q build
del build.zip
C:\Python32\python.exe setup.py build
copy start.bat build
"C:\Program Files\7-Zip\7z" a build.zip build\start.bat "build\exe.win-amd64-3.2"