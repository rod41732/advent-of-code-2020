#include <bits/stdc++.h>
using namespace std;

int a[1010];
map<int, int> cnt;

int main() {
  int n = 0;
  freopen("input.txt", "r", stdin);

  while (scanf("%d", &a[n]) != EOF) {
    n++;
  }
  for (int i=0; i<25; i++) {
    for (int j=1; j<25; j++)
      cnt[a[i]+a[j]]++;
  }

  for (int i=25; i<n; i++) {
    if (cnt[a[i]] == 0) {
      printf("row %d: value: %d\n", i, a[i]); //row 633: value: 507622668
      break;
    }

    // add [ .... 24 nums ] [a[i]]
    for (int j=i-24; j<i; j++)
      cnt[a[i]+a[j]]++;
    // remove [a[i-25]] [ .... 24 nums]
    for (int j=i-24; j<i; j++)
      cnt[a[i-25]+a[j]]--;
  }


  return 0;
}