QT += widgets

HEADERS       = mainwindow.h
SOURCES       = mainwindow.cpp \
                main.cpp

TRANSLATIONS += i18n/menus_en.ts \
                i18n/menus_zh.ts \
                i18n/menus_ja.ts \
                i18n/menus_ko.ts

# install
target.path = $$[QT_INSTALL_EXAMPLES]/widgets/mainwindows/menus
INSTALLS += target


RESOURCES += \
    menus.qrc
