package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)
	var s string
	fmt.Scanf("%s", &s)
	missing := n - len(s)
	var ans strings.Builder
	for _ = range missing {
		ans.WriteString("o")
	}
	ans.WriteString(s)
	fmt.Println(ans.String())
}
