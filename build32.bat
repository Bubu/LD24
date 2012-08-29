rmdir /s/q build
del Evolution_of_a_Planet.zip
C:\Python32_x86\python.exe setup.py build
copy start32.bat build\start.bat
copy README build\readme.txt
rename build "Evolution_of_a_Planet"
"C:\Program Files\7-Zip\7z" a Evolution_of_a_Planet.zip Evolution_of_a_Planet\start.bat Evolution_of_a_Planet\readme.txt "Evolution_of_a_Planet\exe.win32-3.2"