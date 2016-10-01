import QtQuick 2.0

Item {
    property int buttonW: 20
    Rectangle{
        id:inputgroup
        //x:0
        //y:210
        //width:450
        //height:20

        Text{
               id:inputtext0
                x:0
                y:0
                text: "0"
        }
        Text{
                id:inputtext1
                x:20
                y:0

                text: "0"
        }
        Text{
                id:inputtext2
                x:40
                y:0

                text: "0"
        }
        Text{
                id:inputtext3
                x:60
                y:0

                text: "0"
        }
        Text{
                id:inputtext4
                x:80
                y:0

                text: "0"
        }
        Text{
                id:inputtext5
                x:100
                y:0

                text: "0"
        }
        Text{
                id:inputtext6
                x:120
                y:0

                text: "0"
        }
        Text{
                id:inputtext7
                x:140
                y:0

                text: "0"
        }
        Text{
                id:inputButton8
                x:160
                y:0

                text: "0"
        }


        ButtonInput{
            id:inputButton9
            x:inputButton8.x + buttonW
            y:0


            Text{
                id:inputtext9
                anchors.fill: parent
                text:"9"
            }

            MouseArea{
                anchors.fill: parent
                onClicked: {
                    //s99_00text.text = inputtext9.text.toString()
                    if(inputtextname) inputtextname.text = "9"
                    else console.debug( "未定義")
                }
            }
        }

    }
}
