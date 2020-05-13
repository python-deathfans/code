# include <stdio.h>

int dp[100];

int fib(int n)
{
	if (n<=2)
	{
		return 1;
	}
	
	dp[1] = dp[2] = 1;
	
	for (int i=3; i<=n; i++)
	{
		dp[i] = dp[i-1] + dp[i-2];
	}
	
	return dp[n];
}

int main(void)
{
	int n;
	
	scanf("%d", &n);
	
	for (int i=1; i<=n; i++)
		printf("%d  ", fib(i));
	printf("\n");
	
	return 0;
}
