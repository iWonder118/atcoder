#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    int total = 0;
    cin  >> n >> x;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++){
        cin >> numbers[i];
        total += numbers[i];
        if (i % 2 != 0) {
            total--;
        }
    }
    if (total <= x){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

}