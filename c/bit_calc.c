#include <stdio.h> 
  
int main(int argc,char **argv) 
{ 
    int test1,test2; 
  
    test1 = 0x0100; 
    test2 = 0x0101; 
  
    //論理積 
    printf("論理積 test1(%#x) & test2(%#x) → 0x%04x\n",test1, test2, test1 & test2); 
  
    //論理和 
    printf("論理和 test1(%#x) | test2(%#x) → 0x%04x\n",test1, test2, test1 | test2); 
  
    //排他的論理和 
    printf("排他的論理和 test1(%#x) ^ test2(%#x) → 0x%04x\n",test1, test2, test1 ^ test2); 
  
    //否定演算 
    printf("否定演算 ~test1(%#x) → 0x%04x\n",test1, ~test1); 
  
      
    return 0; 
} 

