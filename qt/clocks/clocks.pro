TEMPLATE     = app

QT          += qml quick

SOURCES     += main.cpp
RESOURCES   += clocks.qrc
TRANSLATIONS += i18n/clocks_en.ts \
                i18n/clocks_ja.ts \
                i18n/clocks_zh.ts \
                i18n/clocks_ko.ts

lupdate_only{
SOURCES = clocks.qml
}

#target.path  = $$[QT_INSTALL_EXAMPLES]/quick/demos/clocks
#target.path  = %{CurrentProject:Path}
target.path  = C:\Users\USER\Desktop\clocks
INSTALLS    += target

OTHER_FILES  += \
                clocks.qml \
                content/Clock.qml \
                content/*.png

message( $$TEMPLATE )
message( $$QT )
message( $$RESOURCES )
message( $$target.path )
message( $$INSTALLS )
message( $$OTHER_FILES )
