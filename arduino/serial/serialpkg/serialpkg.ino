/* 
Serial.begin(speed) 
Serial.end() 
Serial.available() 
Serial.read() 
Serial.peek() 
Serial.flush() 
Serial.print(data, format) 
Serial.println(data, format) 
Serial.write(val) 
*/
#include <stdio.h>
#define MAXLEN 50
#define STRLEN 50
int delay_l = 1000 ;  //１秒=1000

typedef struct cmdt
{
  char cmd ;
  char body[] ;
} cmd_t ;

void setup() {
  Serial.begin(9600); //初期化、速度
}

void loop() {
  char msg[STRLEN] ;
  char tmp[STRLEN] ;
  cmd_t cmd_c ;
  
  receiveMSG( msg );
  
  analyzeMSG( msg, &cmd_c ) ;
  /*
  //sprintf(tmp, "%c:%s", cmd_c->cmd, cmd_c->body ); 
  Serial.print(  cmd_c.cmd ) ;
  Serial.print(  ":" ) ;
  Serial.print(  cmd_c.body ) ;
  //Serial.println("") ;
  //Serial.println( tmp ) ;
  //sendMSG( msg ) ;
  */
  
  delay(delay_l);
}

int receiveMSG(char *msg)
{
  int cnt=0;
  memset( msg, '\0', STRLEN ) ;
  
  while(1)
  {
    if( Serial.available()>0)
    {
      char ch1 = Serial.read();
      if( ch1 == '\r' || cnt >=MAXLEN-1 ) break ; // return code(CR,LF,CR/LF)
      msg[cnt] = ch1 ;
      cnt ++ ;
    }
  }
  return cnt ;
}

void analyzeMSG(char *msg, cmd_t *tmp_cmd )
{

  tmp_cmd->cmd = msg[0] ;           // コマンド
  memcpy(&tmp_cmd->body , &msg[1], strlen(msg) ) ;  //メッセージのBody
  Serial.print( tmp_cmd->cmd ) ;
  Serial.print(":") ;
  Serial.println( tmp_cmd->body ) ;
  Serial.flush() ;
}

void doWork()
{
  // 何をしたい？
}
void sendMSG(char *msg )
{
  Serial.println( msg ) ;
  Serial.flush() ;
}
