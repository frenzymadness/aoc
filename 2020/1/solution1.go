package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	"strconv"
)

func main() {
	content, _ := ioutil.ReadFile("input1.txt")

	lines := strings.Split(string(content), "\n")

	for i1, v1 := range lines {
		for _, v2 := range lines[i1+1:] {
			x, _ := strconv.Atoi(v1)
			y, _ := strconv.Atoi(v2)
			res := x + y
			if res == 2020 {
				fmt.Println(x, "+", y, "= 2020, x * y =", x * y)
				return
			}
		}
	}
}
