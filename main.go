package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n, k := next(), next()
	a := make([]int, n+1)
	for i := 1; i <= n; i++ {
		a[i] = next()
	}

	r := make([]int, n+1)
	sum := 0
	for i := 1; i <= n-1; i++ {
		if i == 1 {
			r[i] = 1
		} else {
			r[i] = r[i-1]
		}
		for r[i] < n {
			if a[r[i]+1]-a[i] <= k {
				r[i] += 1
			} else {
				break
			}
		}

		sum += r[i] - i
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, sum)
}
