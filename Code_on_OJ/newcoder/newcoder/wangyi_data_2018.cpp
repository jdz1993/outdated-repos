#include "wangyi_data_2018.h"


int f_1()
{
	int count = 0;
	for (int i = 0; i < 999999; i++)
	{
		size_t index = -1;
		while (true)
		{
			index = to_string(i).find('3', index + 1);

			if (index != string::npos)
				count++;
			else
				break;
		}
	}
	return count;
}

const int N = 101;
typedef int Matrix[N][N];
const int mod = 100;
long long c[N][N];
int n, k;

void mul(Matrix &a, Matrix &b) {
	memset(c, 0, sizeof(c));
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
				c[i][j] += (long long)(a[i][k] * b[k][j]);

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			a[i][j] = c[i][j] % mod;
}

void powMatrix(Matrix &a, int b) {
	Matrix res;
	memset(res, 0, sizeof(res));
	for (int i = 0; i < n; i++)
		res[i][i] = 1;

	while (b) {
		if (b & 1)
			mul(res, a);
		mul(a, a);
		b >>= 1;
	}

	memcpy(a, res, sizeof(res));
}

void f_1_1()
{
	//while (scanf("%d%d", &n, &k) == 2) {
	//	Matrix a;
	//	memset(a, 0, sizeof(a));
	//	for (int i = 0; i < n; i++)
	//		scanf("%d", &a[0][i]);

	//	Matrix b;
	//	memset(b, 0, sizeof(b));
	//	for (int i = 0; i < n; i++) {
	//		b[i][i] = 1;
	//		b[(i + 1) % n][i] = 1;
	//	}

	//	powMatrix(b, k);
	//	mul(a, b);
	//	for (int i = 0; i < n; i++) {
	//		printf("%d", a[0][i]);
	//		putchar(i == n - 1 ? '\n' : ' ');
	//	}
	//}
}

long long int convert2long(const  string &line)
{
	stringstream ss;
	ss << line;
	long long int ret;
	ss >> ret;
	return ret;
}

void handle_2(int start, string &line,int &count,const int n)
{
	cout << line << endl;
	if (start > line.size())
	{
		return;
	}
	if (start == line.size())
	{
		if (convert2long(line) % n == 0)
		{
			count++;
		}
	}
	if (line[start] == 'X')
	{
		for (int i = 0; i < 10; i++)
		{
			line[start] = i + '0';
			handle_2( start + 1, line,count,n);
		}
		line[start] = 'X';
	}
	else
	{
		handle_2(start + 1, line, count, n);
	}
}

int go_2(string &line,int n)
{
	long long int k = 0;

	int count = 0;

	if (line.empty())
	{
		return 0;
	}
	if (line[0] == 'X')
	{
		for (int i = 1; i < 10; i++)
		{
			line[0] = i + '0';
			handle_2( 1, line,count,n);
		}
	}
	else
	{
		handle_2( 0, line, count, n);
	}

	return count;
}

int f_2()
{
	string line;
	cin >> line;
	int n;
	cin >> n;
	return go_2(line, n);
}


int go_3(const string &line)
{
	size_t i1 = 0, i2 = 0;
	int ret = 0;
	int sum = 0;

	// G
	while (i2 < line.size())
	{
		while (i2 < line.size() && line[i2] != 'G')
		{
			i2++;
		}
		if (i2 == line.size())
		{
			break;
		}
		// line[i2]=='G'
		sum += i2 - i1;
		i1++;
		i2++;
	}

	ret = sum;
	i1 = 0;
	i2 = 0;
	sum = 0;

	// B
	while (i2 < line.size())
	{
		while (i2 < line.size() && line[i2] != 'B')
		{
			i2++;
		}
		if (i2 == line.size())
		{
			break;
		}
		// line[i2]=='B'
		sum += i2 - i1;
		i1++;
		i2++;
	}

	ret = (ret > sum) ? sum : ret;

	return ret;
}

int f_3()
{
	string line;
	cin >> line;
	return go_3(line);
}