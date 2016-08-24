#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <memory.h>

char *trim( char *) ;

void main()
{
	char line[50] ;
	char *ip ;
	char *cp = line ;
	char *tmp = "bifurcate_ip = 172.30.10.27    " ;
	strcpy( cp, tmp )  ;
	printf("%s\n", cp ) ;
	cp = strchr(cp, '=');
	printf("strchr. %s\n", cp ) ;
	cp = trim(cp + 1);
	printf("trim. %s\n", cp ) ;
	ip = strdup(cp);
	printf("strdup. %s\n", cp ) ;

}

char *trim( char *s ) {
    int i, j;
 
    //文字列の最後から空白を読み飛ばして除外する
    for( i = strlen(s)-1; i >= 0 && isspace( s[i] ); i-- ) ;
    s[i+1] = '\0';
    //先頭から空白でない文字まで読み飛ばす
    for( i = 0; isspace( s[i] ); i++ ) ;
    //前方の空白を詰める
    if( i > 0 ) {
        j = 0;
        while( s[i] ) s[j++] = s[i++];
        s[j] = '\0';
    }
	return s;
}
/*


char *trim(char *cp)
{
    int i;
    int len;
    int count=0;
    
    len = strlen(cp);
    i=len;
    while ( --i >= 0 && (cp[i] == ' ' || cp[i] == '\n') ) count++;
    cp[i+1] = '\0';
    i = 0;
    while ( cp[i] != '\0' && (cp[i] == ' ' || cp[i] == '\n') ) i++;
    strcpy(cp, cp+i);
    return cp;
}
*/
