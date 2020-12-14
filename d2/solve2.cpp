#include <bits/stdc++.h>
using namespace std;

int main(){
  freopen("input.txt", "r", stdin);
  int from, to;
  char what;
  char pass[1000];
 int ok = 0;
  while (scanf("%d-%d %c: %s\n", &from, &to, &what, pass) != EOF) {
    // index in problem is 1-based so subtract 1
    if ((pass[from-1] == what) != (pass[to-1] == what)) ok++;
  }
  printf("%d\n", ok);
  return 0;

}
