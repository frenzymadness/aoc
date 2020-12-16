package main

import (
    "fmt"
    "regexp"
    "io/ioutil"
    "strings"
    "strconv"
)


func main() {
    content, _ := ioutil.ReadFile("input1.txt")
    lines := strings.Split(string(content), "\n")
    regex := *regexp.MustCompile(`^(\d+)-(\d+) (\w): (\w+)$`)
    var valid_passwords int

    for _, line := range(lines) {
        if len(line) == 0 {
            continue
        }

        res := regex.FindAllStringSubmatch(line, -1)
        id1, _ := strconv.Atoi(res[0][1])
        id2, _ := strconv.Atoi(res[0][2])
        char := res[0][3]
        passwd := res[0][4]
        substr := string(passwd[id1-1]) + string(passwd[id2-1])

        count := strings.Count(substr, char)

        if count == 1 {
            valid_passwords += 1
        }
    }

    fmt.Println(valid_passwords)
}
