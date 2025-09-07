#include <stdio.h>

int main(){
  int a;
  int b;
  scanf("%d %d", &a, &b);
  int product = a*b;
  if (product%2 == 0) {
    printf("Even");
  } else {
    printf("Odd");
  }
  return 0;
}
