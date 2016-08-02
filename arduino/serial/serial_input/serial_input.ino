#include <MsTimer2.h>

int len = 5 ;
char incomingByte[6];   // for incoming serial data
char disp_char[5] ;
int cnt = 0 ;
int flg = 0 ;
int cnt_delay = 0 ;


void have_command( )
{
  
  Serial.print( "I receive \"" );
  Serial.print( disp_char );
  Serial.println("\". I know what I need to do." ) ;
  Serial.flush() ;
}

void no_command()
{
  Serial.println( "I am waitting for your command" ) ;
  Serial.flush() ;
}

void disp()
{
    //while(1)
  {
  if (Serial.available() > 0) {
    incomingByte[cnt] = Serial.read();
    cnt++;
  }
  if( cnt >= len-1 )
  {   
    memcpy(disp_char, incomingByte, len ) ;
    disp_char[4]='\0' ;

    
    //sprintf(disp_char, "%5s", incomingByte ) ;
    if( incomingByte[0] == 'a' )
    {
     flg = 1 ;
    }
    if(incomingByte[0] == 'b')
    {
     flg = 0 ;
    }
    cnt = 0 ;
  }
  
  MsTimer2::start();
    if( flg == 1 )
  {
     have_command(  ) ;
  }
  else
  {
    no_command() ;
  }
  }
}

void setup() {
  Serial.begin(9600);
  MsTimer2::set(1000, disp);
  MsTimer2::start();
}
void loop() {
  
  while(1)
  {
  if (Serial.available() > 0) {
    incomingByte[cnt] = Serial.read();
    cnt++;
  }
  if( cnt >= len-1 )
  {   
    memcpy(disp_char, incomingByte, len ) ;
    disp_char[4]='\0' ;

    
    //sprintf(disp_char, "%5s", incomingByte ) ;
    if( incomingByte[0] == 'a' )
    {
     flg = 1 ;
    }
    if(incomingByte[0] == 'b')
    {
     flg = 0 ;
    }
    cnt = 0 ;
  }
  } 

/*
  delay(100) ;
  if( cnt_delay++ >= 10 )
  {
    disp() ;
    cnt_delay = 0 ;
  }
  */
   //MsTimer2::start();
  //disp() ;

  // say what you got:
  /*
  if( flg == 1 )
  {
     have_command(  ) ;
  }
  else
  {
    no_command() ;
  }
*/
/*  }

 */
  
}

