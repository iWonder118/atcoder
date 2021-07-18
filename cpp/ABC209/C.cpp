#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> C(n);
    for (int i = 0; i < n; i++){
        cin >> C[i];
    }
    sort(C.begin(), C.end());
    long long ans = 1;

    for(int i = 0; i < n; i++) ans = ans * max(0, C[i] - i) % 1000000007;

    cout << ans << endl;

}