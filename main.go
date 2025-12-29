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
	h := next()
	w := next()
	field := make([][]int, h+1)
	for i := 1; i <= h; i++ {
		field[i] = make([]int, w+1)
		for j := 1; j <= w; j++ {
			field[i][j] = next()
		}
	}

	sum0 := make([][]int, h+1)
	for i := 1; i <= h; i++ {
		sum0[i] = make([]int, w+1)
		for j := 1; j <= w; j++ {
			sum0[i][j] = sum0[i][j-1] + field[i][j]
		}
	}

	sum1 := make([][]int, h+1)
	for i := 0; i <= h; i++ {
		sum1[i] = make([]int, w+1)
	}
	for i := 1; i <= h; i++ {
		for j := 1; j <= w; j++ {
			sum1[i][j] = sum1[i-1][j] + sum0[i][j]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	q := next()
	for _ = range q {
		a := next()
		b := next()
		c := next()
		d := next()
		sum := sum1[c][d] - sum1[c][b-1] - sum1[a-1][d] + sum1[a-1][b-1]
		fmt.Fprintln(out, sum)
	}
}
