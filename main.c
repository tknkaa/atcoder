#include <stdio.h>

int main(){
  int a;
  int b;
  int c;
  char s[101];
  scanf("%d", &a);
  scanf("%d %d", &b, &c);
  scanf("%s", s);
  printf("%d %s", a + b + c, s);
  return 0;
}
