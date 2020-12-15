#include <bits/stdc++.h>
using namespace std;

int a[1010];
map<int, int> cnt;

// output from previous part
#define NUM 507622668 

// for example 2
// #define NUM 127 

long long qs[1010];
map<long long, int> pos;


int main() {
  int n = 0;
  // freopen("input-example2.txt", "r", stdin);
  freopen("input.txt", "r", stdin);

  while (scanf("%lld", &qs[n]) != EOF) {
    if (n > 0)
      qs[n] += qs[n-1];
    pos[qs[n]] = n+1; // offset pos by + 1 so it's always > 0, dis
    // printf("%lld\n", qs[n]);

    if (pos[qs[n] - NUM] != 0) {
      
      long long mn = -1ul/2, mx = 0;
                  // actual pos, the + 1 since it exclude
      for (int i=(pos[qs[n] - NUM] - 1) + 1; i <= n; i++) {
        mn = min(mn, qs[i]-qs[i-1]);
        mx = max(mx, qs[i]-qs[i-1]);
      }
      printf("%lld\n", mx + mn); // 76688505
      break;
    }

    n++;
  }



  return 0;
}