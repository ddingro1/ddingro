#include<stdio.h>
int main(void)
{
	int x;
	int y;
	int z;
	int e;
	int c;
	printf("두 수를 입력하시오 : ");
	scanf_s("%d", &x);
	scanf_s("%d", &y);
	z = y / 100;
	e = (y - (z * 100)) / 10;
	c = y - (z * 100 + e * 10);
	printf("(3) : %d\n", x*c);
	printf("(4) : %d\n", x * e);
	printf("(5) : %d\n", x * z);
	printf("(6) : %d\n", x * c + x * e * 10 + x * z * 100);

}
//과제 1