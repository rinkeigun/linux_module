//#include "addressbook.h"
//#include "ui_AddressBook.h"//Qt�f�U�C�i�[�ō쐬����ui�p
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
    QLineEdit *nameLine;//���O����͂���UI�v�f
    QTextEdit *addressText;//�Z������͂���UI�v�f
};