# include <stdio.h>

int walk(int m, int n)
{
	if (m<=0 || n<=0)
	{
		return 0;
	}
	
	int dp[m][n];
	int i, j;
	
	// 初始化最左边一列 
	for (i=0; i<m; i++)
	{
		dp[i][0] = 1;
	}
	
	//  初始化最上边一行 
	for (j=0; j<n; j++)
	{
		dp[0][j] = 1;
	}
	
	for (i=1; i<m; i++)
	{
		for (j=1; j<n; j++)
		{
			dp[i][j] = dp[i-1][j] + dp[i][j-1];
		}
	}
	
	return dp[m-1][n-1];
	
}

int main(void)
{
	int m, n;	// m,n分别代表网格的行或者列 
	int ret;
	
	scanf("%d %d", &m, &n);
	
	ret = walk(m, n);
	
	printf("总共有%d种走法!\n", ret);
	
	return 0;
}
