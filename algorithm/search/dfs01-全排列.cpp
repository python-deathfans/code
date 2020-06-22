/*
假设数字的全排列
看作是扑克牌放进盒子里
现在有三个盒子三张扑克牌 
*/

# include <stdio.h>

int a[20];	// 盒子，存放扑克牌
int book[20];	// 记录哪个牌在手上 
int n;

void dfs(int);

int main(void)
{
	int step = 1;
		
	scanf("%d", &n);	// 存放扑克牌的个数，从1开始 
	
	dfs(step);	// 刚开始在1号盒子前 
	
	getchar();	getchar();
	
	return 0;
}

void dfs(int step)
{
	if (step == n+1)
	{
		for (int i=1; i<=n; i++)
		{
			printf("%d  ", a[i]);
		}
		printf("\n");
		
		return;
	}
	
	for (int i=1; i<=n; i++)
	{
		// 判断i号扑克牌是否还在手上 
		if (book[i] == 0)
		{
			a[step] = i;
			book[i] = 1;
			dfs(step+1);
			book[i] = 0;	// 收回刚才尝试的扑克牌 
		}
	}
	
	return;
}
