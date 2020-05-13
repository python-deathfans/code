# include <stdio.h>

void merging(int *list1, int list1_size, int *list2, int list2_size)
{
	int i, j, k;
	int temp[10];
	
	i = j = k = 0;
	
	while (i<list1_size && j<list2_size)
	{
		if (list1[i]<list2[j])
		{
			temp[k++] = list1[i++];
		}
		else
		{
			temp[k++] = list2[j++];
		}
	}
	
	while (i<list1_size)
	{
		temp[k++] = list1[i++];
	}
	
	while (j<list2_size)
	{
		temp[k++] = list2[j++];
	}
	
	for (i=0; i<k; i++)
	{
		list1[i] = temp[i];
	}
	
	return;
}

void mergesort(int a[], int len)
{
	int *list1, *list2, list1_size, list2_size;
	
	list1 = a;
	list1_size = len/2;
	list2 = list1+list1_size;
	list2_size = len - list1_size;
	
	if (len>1)
	{
		mergesort(list1, list1_size);
		mergesort(list2, list2_size);
		
		merging(list1, list1_size, list2, list2_size);
	}
	
	return;
}

void show(int a[], int n)
{
	int i;
	
	for (i=0; i<n; i++)
	{
		printf("%d  ", a[i]);
	}
	printf("\n");
	
	return;
}

// 二路归并算法 
int main(void)
{
	int n;
	
	printf("请输入需要排序的个数:");
	scanf("%d", &n);
	
	int i;
	int a[n+1];
	
	for (i=0; i<n; i++)
	{
		scanf("%d", a+i);
	}
	
	mergesort(a, n);
	
	show(a, n);
	
	return 0;
}
