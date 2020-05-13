# include <stdio.h>

int a[10];
int binary_search(int, int, int);

int main(void)
{
	int x, pos, i;
	int len;
	
	scanf("%d", &len);
	
	for (i=1; i<=len; i++)
	{
		scanf("%d", a+i);
	}
	
	scanf("%d", &x);
	
	pos = binary_search(1, len, x);
	
	if (pos == -1)
	{
		printf("没有找到%d\n", x);
	}
	else
	{
		printf("%d位于第%d个位置!\n", x, pos);
	}
	
	return 0;
}

int binary_search(int low, int high, int x)
{
	int mid;
	
	mid = (low+high) / 2;
	
	if (low>high)
	{
		return -1;
	}
	
	if (a[mid] == x)
	{
		return mid;
	}
	else if (a[mid] > x)
	{
		binary_search(low, mid-1, x);
	}
	else
	{
		binary_search(mid+1, high, x);
	}
}
