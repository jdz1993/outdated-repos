#ifndef TEST_ALGORITHM_H_
#define TEST_ALGORITHM_H_

#include <string>
#include <iostream>
#include <vector>
#include <memory>

using namespace std;

namespace test_algorithm
{
	extern void print();

	template <typename T>
	extern void print(const vector<T> &v);

	template <typename T>
	extern void print(T t);

	template <typename T, typename... Args>
	extern void print(T t, Args... args);


	extern bool KMP(string longstr, string shortstr);

}

namespace dezhi_test
{

	extern void test();


	extern void print();

	template <typename T>
	extern void print(const vector<T> &v);

	template <typename T>
	extern void print(T t);

	template <typename T, typename... Args>
	extern void print(T t, Args... args);
}

#endif // !TEST_ALGORITHM_H_