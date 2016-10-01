import QtQuick 2.5
import QtQuick.Controls 1.4

ApplicationWindow {
    id:mainw
    visible: true
    width: 350; height: 480

    title: qsTr("数独")


    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: console.log("Open action triggered");
            }
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
    }

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



    // control AREA Strat
    Rectangle {
        id:controlgroup
        x:0; y:0
        width:mainw.width; height:base_h
        color:"red"
        border.width: 1
        property bool timerflag: false
        property date starttime:new Date()
        property var totaltime

        Rectangle {
             id: timer
             x:0
             y:0

             color: "grey"
             width: parent.width*0.33
             height: base_h

             Text{
                 id: timertext
                 x:0
                 text: "timer"
             }
             Timer {
                 id:timerf
                 interval: 500; running: true; repeat: true
                 property date tmpdate
                 property int tmpvalue


                 //onTriggered: timertext.text = (new Date()-controlgroup.starttime).toLocaleString(Qt.locale(),"hh:mm:ss")
                 onTriggered: {
                     timerf.tmpvalue = (new Date()-controlgroup.starttime)/1000
                     timertext.text = (timer.tmpvalue / 3600).toString()
                     //timertext.text = ((new Date()-controlgroup.starttime/*+timerf.tmpdate*/)/1000).toLocaleString(Qt.locale(),"hh:mm:ss")


                    //timertext.text = controlgroup.starttime.toLocaleString(Qt.locale(),"hh:mm:ss")
                    //stoptext.text = new Date().toLocaleString(Qt.locale(),"hh:mm:ss")
                 }

             }


             QtObject {
                 property var locale: Qt.locale()
                 property string dateTimeString: "Tue 2013-09-17 10:56:06"

                 Component.onCompleted: {
                     print(Date().fromLocaleString(locale, dateTimeString, "ddd yyyy-MM-dd hh:mm:ss"));
                 }
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
                 //text: "一時停止"
                 text:"開始"
             }
             MouseArea{
                anchors.fill: parent
                onClicked: {
                    if( timerflag==false)
                    {
                        timerflag = true;
                        stoptext.text = "一時停止"
                        timerf.running = false
                    }
                    else if (timerflag==true)
                    {
                        timerflag = false;
                        stoptext.text = "開始"
                        timerf.running =true
                    }
                }
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


    Item {
        anchors.fill: parent
        focus: true
        Keys.onPressed: {
            if (event.key == Qt.Key_Left) {
                console.log("move left");
                event.accepted = true;
            }
        }
    }
}
