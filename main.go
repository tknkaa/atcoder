package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
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
	b := make([]int, n+1)
	c := make([]int, n+1)
	d := make([]int, n+1)
	for i := range n {
		a[i] = next()
	}

	for i := range n {
		b[i] = next()
	}

	for i := range n {
		c[i] = next()
	}

	for i := range n {
		d[i] = next()
	}
	p := make([]int, n*n+1)
	q := make([]int, n*n+1)
	for i := range n {
		for j := range n {
			p = append(p, a[i]+b[j])
			q = append(q, c[i]+d[j])
		}
	}
	slices.Sort(q)
	for _, v := range p {
		// does q include k - v?
		target := k - v
		_, found := slices.BinarySearch(q, target)
		if found {
			fmt.Println("Yes")
			return
		}
	}
	fmt.Println("No")
}
