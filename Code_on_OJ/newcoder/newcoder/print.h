#pragma once
#ifndef JDZ_PRINT_H_
#define JDZ_PRINT_H_

#include <iostream>
#include <vector>
using namespace std;


	extern void print();

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

#endif
