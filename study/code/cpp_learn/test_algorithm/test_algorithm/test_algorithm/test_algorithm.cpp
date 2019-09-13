#include "test_algorithm.h"

namespace dezhi_test
{
	template<class T>
	string AddressOf(const T& t)
	{
		return  to_string(reinterpret_cast<const int>(reinterpret_cast<const void*>(&t)));
	}

	vector<int> getV()
	{
		vector<int>N;
		N.push_back(1);
		print("N address:", AddressOf(N), "N.size:", N.size());
		return N;
	}

	void test_ptr()
	{
		unique_ptr<int> ptr;
	}

	// 右值引用一般用于：传入参数将被销毁
	// move将左值转换为右值
	// forward完美保持原本的类型
	// 传入临时参数应使用move，不会发生复制
	// 传出临时参数使用引用即可，不会发生复制
	void test_YouZhiYinYong ()
	{
		vector<int> N = move(getV());

		print("N address:", AddressOf(N), "N.size:", N.size());
	}

	void test()
	{
		test_YouZhiYinYong();
	}



	void print() {
		cout << endl;
	}
	template <typename T>
	void print(const vector<T> &v)
	{
		for (const T &t : v)
		{
			cout << t << "\t";
		}
		cout << endl;
	}
	template <typename T>
	void print(T t)
	{
		cout << t << endl;
	}
	template <typename T, typename... Args>
	void print(T t, Args... args)
	{
		cout << t << "\t";
		print(args...);
	}
}



namespace test_algorithm
{
#pragma region Custom Print Function By Jiangdezhi

	void print() {
		cout << endl;
	}
	template <typename T>
	void print(const vector<T> &v)
	{
		for (const T &t : v)
		{
			cout << t << "\t";
		}
		cout << endl;
	}
	template <typename T>
	void print(T t)
	{
		cout << t << endl;
	}
	template <typename T, typename... Args>
	void print(T t, Args... args)
	{
		cout << t << "\t";
		print(args...);
	}

#pragma endregion


	vector<int> Nconstruct(string shortstr)
	{
		vector<int>N(shortstr.size(),0) ;
		if (shortstr.empty()) { return N; }
		

		int i = 1, j = 0;
		while (i < (int)shortstr.size())
		{
			if (shortstr.at(i) == shortstr.at(j))
			{
				N[i] = j + 1;
				i++;
				j++;
			}
			else
			{
				if (j > 0) { j = N[j - 1]; }
				else { i++; }
			}
		}
		return N;
	}

	bool KMP(string longstr, string shortstr)
	{
		vector<int> N = move(Nconstruct(shortstr));

		int i = 0, j = 0;
		while (i < longstr.size())
		{
			if (longstr.at(i) == shortstr.at(j))
			{
				i++;
				j++;
				if (j == shortstr.size()) { return true; }
			}
			else
			{
				if (j > 0) { j = N[j - 1]; }
				else { i++; }
			}
		}

		return false;
	}



}