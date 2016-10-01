import QtQuick 2.5
import QtQuick.Window 2.2

Window {
    id:mainw
    // 各値の初期化
    // s99のセルが選択されるときに記録する値
    property var inputtextname:;

    //セルの基本位置
    property int base_x:20
    property int base_y:20

    //セルの基本サイズ
    property int base_w:20
    property int base_h:20


    //s99 color
    property color s99BaseColor:"gray"
    property color s99ActiveColor:"red"

    //

    visible: true
    width: 350
    height: 480

    title: qsTr("数独")


    // control AREA Strat
    Rectangle {
        id:controlgroup
        x:0; y:0
        width:mainw.width; height:base_h
        color:"red"
        border.width: 1

        Rectangle {
             id: timer
             x:0
             y:0

             color: "grey"
             width: parent.width*0.3
             height: base_h

             Text{
                 id: timertext
                 x:0
                 text: "timer"
             }
        }
        Rectangle {
             id: stop
             x:timer.width
             y:0

             color: "grey"
             width: parent.width*0.3
             height: base_h

             Text{
                 id: stoptext
                 text: "一時停止"
             }
        }
        Rectangle {
             id: end
             x:stop.x + stop.width; y:0
             color: "grey"
             width: parent.width*0.3
             height: base_h

             Text{
                 id: endtext
                 text: "終了"
             }
              MouseArea{
                 anchors.fill: parent
                 onClicked: {
                     Qt.quit();
                 }
             }
        }
    }
    // control AREA End
    /*
    Rectangle {
        width: 100
        height: 100

        gradient: Gradient {
            GradientStop { position: 0.0; color: "yellow" }
            GradientStop { position: 1.0; color: "green" }
        }
    }
    */

    // S99 AREA Start
    RectangleS99
    {
        id:s99group
        x:0
        y:controlgroup.y + controlgroup.height
        width:controlgroup.width; height:160
        border.width:1
    }

    /*
    Rectangle{
        //id:s99group
        //x:0
        //y:controlgroup.y + controlgroup.height
        //width:controlgroup.width; height:160


        Rectangle{
            color:s99BaseColor

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

            TextInput{
                id:s99_10text
                x:20
                y:0
                text: "0"
            }

            TextInput{
                id:s99_20text
                x:40
                y:0
                text: "0"
            }

            TextInput{
                id:s99_30text
                x:60
                y:0
                text: "0"
            }

            TextInput{
                id:s99_40text
                x:80
                y:0
                text: "0"
            }

            TextInput{
                id:s99_50text
                x:100
                y:0
                text: "0"
            }

            TextInput{
                id:s99_60text
                x:120
                y:0
                text: "0"
            }

            TextInput{
                id:s99_70text
                x:140
                y:0
                text: "0"
            }

            TextInput{
                id:s99_80text
                x:160
                y:0
                text: "0"
            }

            TextInput{
                id:s99_01text
                x:0
                y:20
                text: "0"
            }

            TextInput{
                id:s99_11text
                x:20
                y:20
                text: "0"
            }

            TextInput{
                id:s99_21text
                x:40
                y:20
                text: "0"
            }

            TextInput{
                id:s99_31text
                x:60
                y:20
                text: "0"
            }

            TextInput{
                id:s99_41text
                x:80
                y:20
                text: "0"
            }

            TextInput{
                id:s99_51text
                x:100
                y:20
                text: "0"
            }

            TextInput{
                id:s99_61text
                x:120
                y:20
                text: "0"
            }

            TextInput{
                id:s99_71text
                x:140
                y:20
                text: "0"
            }

            TextInput{
                id:s99_81text
                x:160
                y:20
                text: "0"
            }

            TextInput{
                id:s99_02text
                x:0
                y:40
                text: "0"
            }

            TextInput{
                id:s99_12text
                x:20
                y:40
                text: "0"
            }

            TextInput{
                id:s99_22text
                x:40
                y:40
                text: "0"
            }

            TextInput{
                id:s99_32text
                x:60
                y:40
                text: "0"
            }

            TextInput{
                id:s99_42text
                x:80
                y:40
                text: "0"
            }

            TextInput{
                id:s99_52text
                x:100
                y:40
                text: "0"
            }

            TextInput{
                id:s99_62text
                x:120
                y:40
                text: "0"
            }

            TextInput{
                id:s99_72text
                x:140
                y:40
                text: "0"
            }

            TextInput{
                id:s99_82text
                x:160
                y:40
                text: "0"
            }

            TextInput{
                id:s99_03text
                x:0
                y:60
                text: "0"
            }

            TextInput{
                id:s99_13text
                x:20
                y:60
                text: "0"
            }

            TextInput{
                id:s99_23text
                x:40
                y:60
                text: "0"
            }

            TextInput{
                id:s99_33text
                x:60
                y:60
                text: "0"
            }

            TextInput{
                id:s99_43text
                x:80
                y:60
                text: "0"
            }

            TextInput{
                id:s99_53text
                x:100
                y:60
                text: "0"
            }

            TextInput{
                id:s99_63text
                x:120
                y:60
                text: "0"
            }

            TextInput{
                id:s99_73text
                x:140
                y:60
                text: "0"
            }

            TextInput{
                id:s99_83text
                x:160
                y:60
                text: "0"
            }

            TextInput{
                id:s99_04text
                x:0
                y:80
                text: "0"
            }

            TextInput{
                id:s99_14text
                x:20
                y:80
                text: "0"
            }

            TextInput{
                id:s99_24text
                x:40
                y:80
                text: "0"
            }

            TextInput{
                id:s99_34text
                x:60
                y:80
                text: "0"
            }

            TextInput{
                id:s99_44text
                x:80
                y:80
                text: "0"
            }

            TextInput{
                id:s99_54text
                x:100
                y:80
                text: "0"
            }

            TextInput{
                id:s99_64text
                x:120
                y:80
                text: "0"
            }

            TextInput{
                id:s99_74text
                x:140
                y:80
                text: "0"
            }

            TextInput{
                id:s99_84text
                x:160
                y:80
                text: "0"
            }

            TextInput{
                id:s99_05text
                x:0
                y:100
                text: "0"
            }

            TextInput{
                id:s99_15text
                x:20
                y:100
                text: "0"
            }

            TextInput{
                id:s99_25text
                x:40
                y:100
                text: "0"
            }

            TextInput{
                id:s99_35text
                x:60
                y:100
                text: "0"
            }

            TextInput{
                id:s99_45text
                x:80
                y:100
                text: "0"
            }

            TextInput{
                id:s99_55text
                x:100
                y:100
                text: "0"
            }

            TextInput{
                id:s99_65text
                x:120
                y:100
                text: "0"
            }

            TextInput{
                id:s99_75text
                x:140
                y:100
                text: "0"
            }

            TextInput{
                id:s99_85text
                x:160
                y:100
                text: "0"
            }

            TextInput{
                id:s99_06text
                x:0
                y:120
                text: "0"
            }

            TextInput{
                id:s99_16text
                x:20
                y:120
                text: "0"
            }

            TextInput{
                id:s99_26text
                x:40
                y:120
                text: "0"
            }

            TextInput{
                id:s99_36text
                x:60
                y:120
                text: "0"
            }

            TextInput{
                id:s99_46text
                x:80
                y:120
                text: "0"
            }

            TextInput{
                id:s99_56text
                x:100
                y:120
                text: "0"
            }

            TextInput{
                id:s99_66text
                x:120
                y:120
                text: "0"
            }


            TextInput{
                id:s99_76text
                x:140
                y:120
                text: "0"
            }


            TextInput{
                id:s99_86text
                x:160
                y:120
                text: "0"
            }

            TextInput{
                id:s99_07text
                x:0
                y:140
                text: "0"
            }

            TextInput{
                id:s99_17text
                x:20
                y:140
                text: "0"
            }

            TextInput{
                id:s99_27text
                x:40
                y:140
                text: "0"
            }

            TextInput{
                id:s99_37text
                x:60
                y:140
                text: "0"
            }

            TextInput{
                id:s99_47text
                x:80
                y:140
                text: "0"
            }

            TextInput{
                id:s99_57text
                x:100
                y:140
                text: "0"
            }


            TextInput{
                id:s99_67text
                x:120
                y:140
                text: "0"
            }


            TextInput{
                id:s99_77text
                x:140
                y:140
                text: "0"
            }


            TextInput{
                id:s99_87text
                x:160
                y:140
                text: "0"
            }


            TextInput{
                id:s99_08text
                x:0
                y:160
                text: "0"
            }


            TextInput{
                id:s99_18text
                x:20
                y:160
                text: "0"
            }


            TextInput{
                id:s99_28text
                x:40
                y:160
                text: "0"
            }


            TextInput{
                id:s99_38text
                x:60
                y:160
                text: "0"
            }


            TextInput{
                id:s99_48text
                x:80
                y:160
                text: "0"
            }


            TextInput{
                id:s99_58text
                x:100
                y:160
                text: "0"
            }


            TextInput{
                id:s99_68text
                x:120
                y:160
                text: "0"
            }


            TextInput{
                id:s99_78text
                x:140
                y:160
                text: "0"
            }


            TextInput{
                id:s99_88text
                x:160
                y:160
                text: "0"
            }

    }
*/
    // S99 AREA End
    // Input AREA Start
    RectangleInput
    {
        y:s99group.y + s99group.height
        width:s99group.width; height:20
    }


    // Input AREA End


}
