#include <bits/stdc++.h>
using namespace std;

struct pass {
  int row;
  int col;
};

char buf[20];

int main() {
  int i=0;
  pass passes[2000];

  freopen("input.txt", "r", stdin);

  int mx = 0;
  while (scanf("%s\n", buf) != EOF) {
  // for (int i=0; i<10; i++) {
    // printf("%s\n", buf);
    int row = 0;
    for (int i=0; i<7; i++) {
      row = 2*row + (buf[i] == 'B');
    }
    int col = 0;
    for (int i=7; i<10; i++) {
      col = 2*col + (buf[i] == 'R');
    }
    passes[i] = {row, col};
    mx = max(mx, row*8 + col);
  }
  printf("%d\n", mx);
  return 0;
}