rmdir /s/q build
rmdir /s/q Evolution_of_a_Planet
del Evolution_of_a_Planet_x64.zip
C:\Python32\python.exe setup.py build
copy start.bat build
copy README build\readme.txt
rename build "Evolution_of_a_Planet"
"C:\Program Files\7-Zip\7z" a Evolution_of_a_Planet_x64.zip Evolution_of_a_Planet\start.bat Evolution_of_a_Planet\readme.txt "Evolution_of_a_Planet\exe.win-amd64-3.2"