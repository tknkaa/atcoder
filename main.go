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
	h, w, n := next(), next(), next()
	raw := make([][]int, h+2)
	sum := make([][]int, h+2)
	for i := 0; i <= h+1; i++ {
		raw[i] = make([]int, w+2)
		sum[i] = make([]int, w+2)
	}

	for i := 1; i <= n; i++ {
		a, b, c, d := next(), next(), next(), next()
		raw[a][b] += 1
		raw[a][d+1] -= 1
		raw[c+1][b] -= 1
		raw[c+1][d+1] += 1
	}
	for i := 1; i <= h; i++ {
		for j := 1; j <= w; j++ {
			sum[i][j] = sum[i][j-1] + raw[i][j]
		}
	}

	for i := 1; i <= h; i++ {
		for j := 1; j <= w; j++ {
			sum[i][j] += sum[i-1][j]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 1; i <= h; i++ {
		for j := 1; j <= w; j++ {
			fmt.Fprint(out, sum[i][j])
			if j != w {
				fmt.Fprintf(out, " ")
			}
		}
		fmt.Fprintf(out, "\n")
	}
}
