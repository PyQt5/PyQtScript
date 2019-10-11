set PLATFORM=x86
set SIPVER=4.19.19
set PYQTVER=5.13.1
set QTDIR="D:\soft\Qt\Qt5.13.1\5.13.1\msvc2017"

python build.py --platform=Windows --arch=%PLATFORM% --build=sip --sipver=%SIPVER% --pyqtver=%PYQTVER% --qmake=%QTDIR%\bin\qmake.exe
python build.py --platform=Windows --arch=%PLATFORM% --build=PyQt5 --sipver=%SIPVER% --pyqtver=%PYQTVER% --qmake=%QTDIR%\bin\qmake.exe

:: python35 --tags=cp35
python mkdist.py --platform=Windows --arch=%PLATFORM% --version=%PYQTVER% --tags=cp35
python test.py --platform=Windows --arch=%PLATFORM% --version=%PYQTVER% --tags=cp35