#include <QApplication>
#include <qWidget>
#include <QLabel>
#include <QLineEdit>
#include <QHBoxLayout>
#include <QGroupBox>

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    QWidget* qwin = new QWidget ;
    QHBoxLayout* layout = new QHBoxLayout;
    //QGroupBox* qg = new QGroupBox ;
    QLabel* label = new QLabel("Hello Qt!");
    QLineEdit* lineedt = new QLineEdit();
    lineedt->setGeometry(30,30,20,20);
    //qwin->addWidget( lineedt );
    layout->addWidget(label);
    layout->addWidget(lineedt);
    qwin->setLayout(layout);
    //label->show();
    //lineedt->show() ;
    //app.setMainWidget( qwin ) ;
    qwin->show();
    return app.exec();
}
