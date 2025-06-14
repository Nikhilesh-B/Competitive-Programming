#include <iostream>

using namespace std;

int main()
{
    vector<int> vec {1, 2, 3, 4, 5, 6};
    for (auto num : vec)
    {
        num = 3;
        cout << num << endl;
    }

    for (auto &num : vec)
    {
        cout << num << endl;
        if (num == 1)
            num = 1000;
    }

    for (auto &num : vec)
    {
        cout << num << endl;
    }
}