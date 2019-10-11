#!/bin/bash

echo "you must to be install python3 and install Qt5.13.1 to ~/Qt5.13.1"

# install lib  apt or yum
if [ -f "/usr/bin/apt-get" ];then
    sudo apt-get install libx11-dev libxext-dev libxtst-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev -y
fi
if [ -f "/usr/bin/yum" ];then
    sudo yum install mesa-* freeglut* -y
fi

export QTVER=5.13.1
export QTVERSTR="${QTVER//./}"
export PYVER=$(python3 -c "import sys;print(\"{0}{1}\".format(sys.version_info.major, sys.version_info.minor))")

# install PyQt5
su -c "python3 -m pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com PyQt5==$QTVER"

# install Qt
export INSTALLDIR=~/Qt$QTVER
export PACKAGES=qt.qt5.$QTVERSTR.gcc_64,qt.qt5.$QTVERSTR.qtscript,qt.qt5.$QTVERSTR.qtscript.gcc_64
if [ ! -d "~/Qt$QTVER" ];then
    if [ ! -f "qt-opensource-linux-x64-$QTVER.run" ];then
        wget http://mirrors.ustc.edu.cn/qtproject/archive/qt/5.13/$QTVER/qt-opensource-linux-x64-$QTVER.run
    fi
    ./qt-opensource-linux-x64-$QTVER.run -v --script qtinstaller.js
fi

# build sip
python3 build.py --platform=Linux --arch=x64 --build=sip --sipver=4.19.19 --pyqtver=$QTVER --qmake=$HOME/Qt$QTVER/$QTVER/gcc_64/bin/qmake

# build PyQt5 QtScript
export PATH=~/Qt$QTVER/$QTVER/gcc_64/bin:$PATH
python3 build.py --platform=Linux --arch=x64 --build=PyQt5 --sipver=4.19.19 --pyqtver=$QTVER --qmake=$HOME/Qt$QTVER/$QTVER/gcc_64/bin/qmake

# make whl
python3 mkdist.py --platform=Linux --arch=x64 --version=$QTVER

# test
su -c "python3 test.py --platform=Linux --arch=x64 --version=$QTVER"