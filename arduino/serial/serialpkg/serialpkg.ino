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

int delay_l = 1000 ;  //１秒=100
typedef struct cmdt
{
  char cmd ;
  char body[1024] ;
} cmd_t ;

void setup() {
  Serial.begin(9600); //初期化、速度
}

void loop() {
  char msg[1024] ;
  char tmp[1024] ;
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
  //char incoming[1024] ;
  memset( msg, '\0', 1024 ) ;
  
  while(1)
  {
    if( Serial.available()>0)
    {
      char ch1 = Serial.read();
      if( ch1 == '\r' ) break ; // return code(CR,LF,CR/LF)
      msg[cnt] = ch1 ;
      cnt ++ ;
    }
  }
  return cnt ;
}

void analyzeMSG(char *msg, cmd_t *tmp_cmd )
{
  Serial.print( msg ) ;
  //memcpy( &cmd->cmd , msg, 1 );

  tmp_cmd->cmd = msg[0] ;
  //Serial.println( "qqq" ) ;
  //Serial.println("\n") ;
  /*
  msg++ ;
  memcpy(cmd->body , msg, strlen(msg) ) ;
  Serial.print( cmd->body ) ;
  */
}
void sendMSG(char *msg )
{
  Serial.println( msg ) ;
}
