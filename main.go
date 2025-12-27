package main

import (
	"fmt"
)

type masu struct {
	done  bool
	value int
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	field := make([][]masu, n)
	for i := range n {
		field[i] = make([]masu, n)
	}
	r := 0
	c := (n - 1) / 2
	k := 1
	field[r][c] = masu{
		done:  true,
		value: k,
	}
	for _ = range n*n - 1 {
		if !field[mod(r-1, n)][mod(c+1, n)].done {
			field[mod(r-1, n)][mod(c+1, n)] = masu{
				done:  true,
				value: k + 1,
			}
			r = mod(r-1, n)
			c = mod(c+1, n)
			k += 1
		} else {
			field[mod(r+1, n)][c] = masu{
				done:  true,
				value: k + 1,
			}
			r = mod(r+1, n)
			k += 1
		}
	}
	for i := range n {
		for j := range n {
			fmt.Print(field[i][j].value)
			if j != n-1 {
				fmt.Print(" ")
			}
		}
		fmt.Printf("\n")
	}
}

func mod(x, n int) int {
	if x < 0 {
		for x < 0 {
			m := (-x) / n
			x += n * (m + 1)
		}
	}
	return x % n
}
