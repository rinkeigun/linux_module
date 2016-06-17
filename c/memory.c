/*
	2016/06/17 Huiqun.Lin
	メモリ破壊
	実行結果
---------------------------------------------------
I had a girl friend.
Iboy friend.
*** stack smashing detected ***: ./a.out terminated
中止 (コアダンプ)
---------------------------------------------------
*/

#include <stdio.h>
#include <string.h>

int main(int argc, char ** argv){
  char s1[1], s2[12];

  strcpy(s1, "I had a girl friend."); // s1の領域を越えて代入．
  fprintf(stdout, "%s\n", s1);        // 『私には彼女がいました．』

  strcpy(s2, "boy friend.");          // 「彼氏」を s2 に代入
  fprintf(stdout, "%s\n", s1);        // 何が起こる？
  return 0;
}

