#include "wangyi_data_2018.h"
#include "universal_2017.h"
#include "print.h"
#include "Prime.h"
using namespace std;

void test_1()
{
	const int N = 10;
	const int M = 2;
	int *a = new int[N];
	for (int i = 0; i < N; ++i)
	{
		a[i] = (0 == i % 2) ? (i + 2) : i;
		int(*b)[N / M] = (int(*)[N / M])a;
		for (int i = 0; i < M; i++)
		{
			for (int j = 0; j < N / M; ++j)
			{
				printf("%d", b[i][j]);
			}
		}
	}
}
int QuJian[101] = { 0 };
void Test3()
{
	int temp;
	for (int i = 2; i < 101; ++i)
	{
		QuJian[i] = i;
		for (int j = 1; j < i; j++)
		{
			temp = (j >= (1 + QuJian[i - j])) ? j : (1 + QuJian[i - j]);
			if (QuJian[i] > temp)
				QuJian[i] = temp;
		}
	}
}

void test_2()
{

}

#if 1
#include <map>
#include <vector>
#include <queue>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;
/*
a
/  \
b    c
/ \  /  \
d   e f   g
\  / \
h j   i
\
k
\
l
a:托马斯（Thomas）
b:艾德华（Edward）
c:亨利（Henry）
d:高登（Gordon）
e:詹姆士（James）
f:培西（Percy）
g:托比（Toby）
h:达克（Duke）
j:唐纳德&道格拉斯（Donald&Douglas）
j:奥利佛（Oliver）
k:亚瑟（Arthur）
l:艾蜜莉（Emily）
*/

struct BT
{
	int key;
	BT *l, *r;
};

BT* create_n(int key)
{
	BT* b = new BT();
	b->key = key;
	return b;
}

void  dfs(BT* rt, int key, BT* target)
{
	if (rt == NULL)
	{
		return ;
	}
	if (rt->key == key)
	{
		target = rt;
		return ;
	}
	BT *tmp;

	dfs(rt->l, key, target);
	dfs(rt->r, key, target);

}

void back(BT* rt, map<int, string> &m_train)
{
	if (rt == NULL) { return; }
	back(rt->l, m_train);
	back(rt->r, m_train);	
	cout << " "<< m_train[rt->key-'a'];
}

bool train_schedule(BT* rt, int index)
{
	if (!rt)
		return false;

	map<int, string> m_train;
	m_train[0] = "Thomas";
	m_train[1] = "Edward";
	m_train[2] = "Henry";
	m_train[3] = "Gordon";

	m_train[4] = "James";
	m_train[5] = "Percy";
	m_train[6] = "Toby";
	m_train[7] = "Duke";

	m_train[8] = "Donald&Douglas";
	m_train[9] = "Oliver";
	m_train[10] = "Arthur";
	m_train[11] = "Emily";
	//TODO:write the real train schedule code here 
	BT * bb;
	dfs(rt, index + 'a',bb);
	if (bb == NULL)
	{
		cout << "No";
	}
	else
	{
		back(rt, m_train);
	}
	return true;
}
int main()
{
	int i = 0;
	BT *rt = create_n('a');
	rt->l = create_n('b');
	rt->r = create_n('c');
	rt->l->l = create_n('d');
	rt->l->r = create_n('e');
	rt->r->l = create_n('f');
	rt->r->r = create_n('g');
	rt->r->l->r = create_n('h');
	rt->r->r->r = create_n('i');
	rt->r->r->l = create_n('j');
	rt->r->r->l->r = create_n('k');
	rt->r->r->l->r->r = create_n('l');
	std::cin >> i;

	train_schedule(rt, i);

	system("pause");
	return 0;
}
#else


#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;


void helper(int n, int m, double p, const vector<vector<double>>& prices, int ni, int mi, double & max, double  money, double cash, double buyprice)
{
	if (mi < m-1)
	{
		double newmoney, newcash, newbuyprice;

		//sell, not sell, buy, not buy
		if (money > 0)
		{
			for (int i = 0; i < n; i++)
			{
				helper(n, m, p, prices, i, mi + 1, max, money, cash, buyprice);
			}

			newcash = money* prices[mi][ni] / buyprice*(1 - p);
			newmoney = 0;
			for (int i = 0; i < n; i++)
			{
				helper(n, m, p, prices, i, mi + 1, max, newmoney, newcash, buyprice);
			}

			newmoney = cash;
			newcash = 0;
			newbuyprice = prices[mi][ni];

			for (int i = 0; i < n; i++)
			{
				helper(n, m, p, prices, i, mi + 1, max, newmoney, newcash, newbuyprice);
			}
		}
		else
		{
			for (int i = 0; i < n; i++)
			{
				helper(n, m, p, prices,i, mi + 1, max, money, cash, buyprice);
			}

			newmoney = cash;
			newcash = 0;
			newbuyprice = prices[mi][ni];

			for (int i = 0; i < n; i++)
			{
				helper(n, m, p, prices, i, mi + 1, max, newmoney, newcash, newbuyprice);
			}
		}

	}
	else if (mi == m-1)
	{
		cash += money*prices[mi][ni] / buyprice*(1 - p);
		if (max < cash)
		{
			max = cash;
			return;
		}
	}
}

/*请完成下面这个函数，实现题目要求的功能*/
/*当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ */
/******************************开始写代码******************************/
double StockGod(int n, int m, double p, const vector<vector<double>>& prices)
{
	// origin cash 对应的钱
	//double origin = 1 * (1 + p);

	// 每一天的选择在一下两种中选择
	// 与昨天的一致
	// 选择最大的收益并交印花税

	double max = -1;

	for (int i = 0; i < n; i++)
	{
		helper(n, m, p, prices, i, 0, max, 0, 1, 0);
	}
	return max;
}

/******************************结束写代码******************************/


int main()
{
	//int n = 0;
	//int m = 0;
	//double p = 0;
	//cin >> n >> m >> p;

	//vector<vector<double>> prices;
	//for (int i = 0; i < m; ++i) {
	//	prices.push_back(vector<double>());
	//	for (int j = 0; j < n; ++j) {
	//		double x = 0;
	//		cin >> x;
	//		prices.back().push_back(x);
	//	}
	//}

	int n = 1, m = 2;
	double p = 0.1;
	vector<vector<double>> prices;
	prices.push_back(vector<double>{1});
	prices.push_back(vector<double>{2});

	double final = StockGod(n, m, p, prices);
	printf("%.1f\n", final);

	system("pause");
	return 0;
}


#endif