#include <iostream>

using namespace std;

void f_1()
{
	int a, b;
	while (cin >> a >> b)
	{
		cout << a + b << endl;
	}
}

int main()
{
	f_1();
	return 0;
}