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
	d := next()
	n := next()
	diff := make([]int, d+2)
	for i := 0; i < n; i++ {
		l := next()
		r := next()
		diff[l] += 1
		diff[r+1] -= 1
	}
	sum := make([]int, d+2)
	for i := 1; i <= d; i++ {
		sum[i] = sum[i-1] + diff[i]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 1; i <= d; i++ {
		fmt.Fprintln(out, sum[i])
	}
}
