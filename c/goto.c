#include <stdio.h>

void func1()
{
	goto FUNC_END;
	printf("%s:%s(%d)\n",__FILE__, __FUNCTION__, __LINE__ ) ;
FUNC_END:
	printf("last line %s:%s(%d)\n",__FILE__, __FUNCTION__, __LINE__ ) ;
}
void func2()
{
	goto FUNC_END;
	printf("%s:%s(%d)\n",__FILE__, __FUNCTION__, __LINE__ ) ;
FUNC_END:
	printf("last line %s:%s(%d)\n",__FILE__, __FUNCTION__, __LINE__ ) ;
}
void main()
{
	func1();
	func2();
}
