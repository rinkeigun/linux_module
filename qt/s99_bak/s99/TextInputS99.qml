import QtQuick 2.0

Item {
    Rectangle{
        color:s99BaseColor
        width:base_w
        height:base_h

        TextInput{
            id:s99_00text
            x:0
            y:0
            inputMask:"9"
            maximumLength:1
            text: "0"
            MouseArea{
                anchors.fill: parent
                onClicked: {

                    inputtextname = s99_00text;
                    //文字入力はどうする？
                    //s99_00text.activeFocus ;
                }
            }
        }
    }
}
