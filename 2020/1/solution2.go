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
		for i2, v2 := range lines[i1+1:] {
			for _, v3 := range lines[i2+1:] {
				x, _ := strconv.Atoi(v1)
				y, _ := strconv.Atoi(v2)
				z, _ := strconv.Atoi(v3)
				res := x + y + z
				if res == 2020 {
					fmt.Println(x, "+", y, "+", z, "= 2020, x * y * z =", x * y * z)
					return
				}
			}
		}
	}
}
