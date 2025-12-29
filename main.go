package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	for i := 9; i >= 0; i-- {
		if (n>>i)&1 == 1 {
			fmt.Print(1)
		} else {
			fmt.Print(0)
		}
	}
	fmt.Print("\n")
}
