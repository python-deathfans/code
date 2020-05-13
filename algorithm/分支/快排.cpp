# include <stdio.h> 

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

void swap(int a[], int low, int high)
{
	int t;
	
	t = a[low];
	a[low] = a[high];
	a[high] = t;
	
	return;
}

int partition(int a[], int low, int high)
{
	int base;
	int i, j;
	
	base = a[low];
	i = low;
	j = high;
	
	while (i != j)
	{
		while (i<j && a[j]>=base)
		{
			j--;
		}
//		swap(a, low, high);
		
		while (i<j && a[i]<=base)
		{
			i++;
		}
		
		if (i<j)
			swap(a, i, j);
	}
	
	// 基准值归位 
	a[low] = a[i];
	a[i] = base;
	
	
	return low;
}

void quicksort(int a[], int low, int high)
{
	if (low<high)
	{
		int pos = partition(a, low, high);
		
		quicksort(a, low, pos-1);
		quicksort(a, pos+1, high);
	}
	
	return;
}

// 快速排序 
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
	
	quicksort(a, 0, n-1);
	
	show(a, n);
	
	return 0;
}
