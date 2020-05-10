# include <stdio.h>
# include <stdlib.h>

typedef struct Meeting
{
	int s;
	int e;
	int flag = 0;
}Meeting, *pMeeting;

void sort(pMeeting, int);
void greedy(pMeeting, int);
void show(pMeeting, int);

int main(void)
{
	int n;	// 记录活动的个数
	pMeeting p;	// 存储会议的起始时间
	int i;
	
	scanf("%d", &n) ;
	p = (pMeeting)malloc(sizeof(Meeting) * n);
	
	for (i=0; i<n; i++)
	{
		scanf("%d %d", &p[i].s, &p[i].e);
	}
	
	sort(p, n);
	greedy(p, n);
	show(p, n);
	
	return 0;
}

// 改进版的选择排序 
void sort(pMeeting p, int n)
{
	int i, j;
	int min_index;
	Meeting temp;
	
	for (i=0; i<n-1; i++)
	{
		min_index = i;
		for (j=i+1; j<n; j++)
		{
			if (p[j].e < p[min_index].e)
			{
				min_index = j;
			}
		}
		
		if (min_index != i)
		{
			temp = p[min_index];
			p[min_index] = p[i];
			p[i] = temp;
		}
	}
	
	return;
}

// 贪心算法 
void greedy(pMeeting p, int n)
{
	int i, j;
	
	i = 0;
	p[i].flag = 1;
	
	for (j=1; j<n; j++)
	{
		if (p[j].s >= p[i].e)
		{
			p[j].flag = 1;
			i = j;
		}
	}
	
	return;
}

// 打印选择的会议 
void show(pMeeting p, int n)
{
	int i;
	
	for (i=0; i<n; i++)
	{
		if (p[i].flag == 1)
		{
			printf("%d %d\n", p[i].s, p[i].e);
		}
	}
	
	return;
}
