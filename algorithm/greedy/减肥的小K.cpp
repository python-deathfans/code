# include <stdio.h>

int a[100];	// 存储每堆砖头的个数 
void sort(int);
void greedy(int);

int main(void)
{
	int n;	// 存储砖头的堆数
	int i;
	
	scanf("%d", &n) ;
	
	for (i=0; i<n; i++)
	{
		scanf("%d", &a[i]);
	}
	
	sort(n);
	greedy(n);
	
	return 0;
}

void sort(int n)
{
	int i, j, min_index;
	int t;
	
	for (i=0; i<n-1; i++)
	{
		min_index = i;
		for (j=i+1; j<n; j++)
		{
			if (a[j] < a[min_index])
			{
				min_index = j;
			}
		}
		
		if (min_index != i)
		{
			t = a[min_index];
			a[min_index] = a[i];
			a[i] = t;
		}
	}
	
	return;
}

void greedy(int n)
{
	int cost = 0;
	int i, temp;
	int j;
	
	for (i=0; i<n-1; i++)
	{
		temp = a[i] + a[i+1];
		cost += temp;
		
		// 找到合适的位置，把temp插进去 
		for (j=i+2; j<n && temp>a[j]; j++)
		{
			a[j-1] = a[j];
		}
		a[j-1] = temp;
	}
	printf("总共消耗%d\n", cost);
	
	return;
}
