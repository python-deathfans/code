# include <stdio.h>

int jump(int n)
{
	if (n<=2)
	{
		return n;
	}
	
	int dp[n+1];	// 存储每一级可能的结果
	
	// 给出初始值
	dp[0]  = 0;
	dp[1] = 1;
	dp[2] = 2;
	
	for (int i=3; i<=n; i++)
	{
		dp[i] = dp[i-1] + dp[i-2];
	}
	
	return dp[n];
}

int main(void)
{
	int n;
	int ret;
	
	scanf("%d", &n);
	
	ret = jump(n);
	printf("%d个台阶有%d种跳法~\n", n, ret);
	
	return 0;
}
