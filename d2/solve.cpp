#include <bits/stdc++.h>
using namespace std;

int main(){
  freopen("input.txt", "r", stdin);
  int from, to;
  char what;
  char pass[1000];
  int ok = 0;
  while (scanf("%d-%d %c: %s\n", &from, &to, &what, pass) != EOF) {
      int cnt =0;
      int n = strlen(pass);
     for (int i=0; i<n; i++) {
       if (pass[i] == what) cnt++;
     }
    if (from <= cnt && cnt <= to) ok++;
  }
  printf("%d\n", ok);
  return 0;

}
