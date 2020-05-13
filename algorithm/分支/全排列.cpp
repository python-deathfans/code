# include <stdio.h>
# include <string.h>

char a[100];
int k = 0;
int count = 0;

void swap(char a[], int i, int k)
{
	char t;
	
	t = a[i];
	a[i] = a[k];
	a[k] = t;
	
	return;
}

void arrangement(char a[], int k, int len)
{
	if (k == len-1)
	{
		puts(a);
		count++;
	}
	
	for (int i=k; i<len; i++)
	{
		swap(a, i, k);
		arrangement(a, k+1, len);
		swap(a, i, k);	// 交换完成之后一定要复原 
	}
	
	return;
}

int main(void)
{
	gets(a);
	int len = strlen(a);	// 字符串的长度
	
	arrangement(a, k, len);	// 全排列 
	
	return 0;
}
