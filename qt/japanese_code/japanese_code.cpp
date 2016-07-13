#include <QApplication>
#include <QLabel>
#include <QTextCodec>
#include <QString>

int main(int argc, char** argv)
  {
    QApplication app(argc, argv);
    QTextCodec::setCodecForTr(QTextCodec::codecForLocale());
    QLabel* label = new QLabel(QObject::tr("‚±‚ñ‚É‚¿‚Í Qt"));
    label->show();
    return app.exec();
}
