//#include "addressbook.h"
//#include "ui_AddressBook.h"//Qtデザイナーで作成したui用
//#include <QtWidgets>

#include <QGridLayout>

class QLineEdit;
class QTextEdit;
class AddressBook : public QWidget
{
    Q_OBJECT
public:
    AddressBook(QWidget *parent = 0);
private:
    QLineEdit *nameLine;//名前を入力するUI要素
    QTextEdit *addressText;//住所を入力するUI要素
};