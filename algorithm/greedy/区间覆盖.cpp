# include <stdio.h>
# include <stdlib.h>

typedef struct Field
{
	int s;
	int e;
}Field;

int main(void)
{
	int n;	// 存储区间的个数 
	int i;
	Field *p;
	int *q;
	
	scanf("%d", &n);
	p = (Field *)malloc(sizeof(Field) * n);
	q = (int *)malloc(sizeof(int) * n);
	
	for (i=0; i<n; i++)
	{
		scanf("%d %d", &p[i].s, &p[i].e);
		q[i] = 0;
	}
	
	return 0;
}
