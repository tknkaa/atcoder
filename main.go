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

	n := next()
	q := next()

	sum := make([]int, n+1)
	for i := 1; i <= n; i++ {
		val := next()
		sum[i] = sum[i-1] + val
	}

	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	for i := 0; i < q; i++ {
		l := next()
		r := next()
		fmt.Fprintln(out, sum[r]-sum[l-1])
	}
}
