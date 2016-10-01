import QtQuick 2.2

Rectangle{


            width:20
            height:20
            anchors.fill: parent
            mouseArea.onClicked: {
                Qt.quit();
            }
            Text{
                text:ok
            }


}
