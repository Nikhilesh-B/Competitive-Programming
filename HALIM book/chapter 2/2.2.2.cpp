#include <iostream>
#include <vector>

using namespace std;

int return_bubble_sort_swaps(vector<int> &arr, vector<int> &sorted_array)
{
    int swap_count = 0;
    const int n = {arr.size()};
    vector<int> displacements 
    int displacements [n] = {0};
}

int main()
{
    vector<int> arr = {5, 4, 3, 2, 1};
    vector<int> sorted_array = arr; // Copy constructor
    sort(sorted_array.begin(), sorted_array.end());
    cout << return_bubble_sort_swaps(arr, sorted_array);
}