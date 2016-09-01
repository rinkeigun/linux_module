#include <QApplication>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QGridLayout>
#include <QGroupBox>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>



int main(int argc, char** argv)
{
    int i, j, k, l;
    int Y, y, X, x, width=20, height=20 ;

	QApplication app(argc, argv);
    QWidget* window = new QWidget;
    QGroupBox* gBox = new QGroupBox;
    //QGroupBox* gBox = new QGroupBox；

    QPushButton* buttonB = new QPushButton("一時停止");
    QPushButton* buttonC = new QPushButton("終了");

    QGridLayout* s33layout[3][3];

    QHBoxLayout* controllayout = new QHBoxLayout;
    QGridLayout* s99layout = new QGridLayout;
    QHBoxLayout* inputlayout = new QHBoxLayout;
    QVBoxLayout* toplayout = new QVBoxLayout;
    QLabel *timer = new QLabel("Timer");

    QLineEdit *s33lineEdt[3][3] ;

    QLineEdit *inputlineEdt[9] ;

    // 1. 画面の上層部
    controllayout->addWidget(timer);
    controllayout->addWidget(buttonB);
    controllayout->addWidget(buttonC);


    // ２．９x９表示部分
    for(i=0; i<3; i++)
    {
        for(j=0; j<3; j++)
        {
            s33layout[i][j]=new QGridLayout;
            for(k=0;k<3;k++)
            {
                for(l=0;l<3;l++)
                {
                    s33lineEdt[k][l] = new QLineEdit;
                    s33lineEdt[k][l]->setGeometry(10,10,200,200);
                    s33layout[i][j]->addWidget(s33lineEdt[k][l], k, l, 0);
                }
            }
            s99layout->addLayout(s33layout[i][j], i, j, 0);
        }
    }

    // ３．入力部分
    for(i=0; i<9; i++)
    {
        Y = 10 ;
        X = i*width ;
        inputlineEdt[i]=new QLineEdit();
        inputlineEdt[i]->setGeometry(X, Y, width, height);
        inputlayout->addWidget(inputlineEdt[i]);
    }

    gBox->setLayout( inputlayout);

    toplayout->addLayout(controllayout);
    toplayout->addLayout(s99layout);
    //toplayout->addWidget(s99layout);
    //toplayout->addLayout(inputlayout);
    //toplayout->addLayout(gBox);
    toplayout->addWidget(gBox);

    // 全体レイアウト
    window->setLayout(toplayout);
    window->setGeometry(0,0,300,300);
	window->show();	
	return app.exec();
}
