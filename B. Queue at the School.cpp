#include <bits/stdc++.h>
using namespace std;

int main() {
    // Your code here
    int n, t;
    cin >> n >> t;
    string s;
    cin >> s;       
    while (t--) {
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == 'B' && s[i + 1] == 'G') {
                swap(s[i], s[i + 1]);
                i++; // Skip the next position as it has just been swapped
            }
        }
    }   
    cout << s << endl;
    
    return 0;
}
