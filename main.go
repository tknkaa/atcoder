package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func question(a, x int) bool {
	return a >= x
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n, x := next(), next()
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		a[i] = next()
	}
	left := -1
	right := n
	for right-left > 1 {
		mid := (left + right) / 2
		if question(a[mid], x) {
			right = mid
		} else {
			left = mid
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, right)
}
