package main

import (
	"fmt"
)

const (

	writePost = 1 << iota
	readPost
	deletePost
	addUser
	deleteUser
)

func main() {

	var administrator byte = writePost | readPost | deletePost | addUser | deleteUser
        var moderator byte = readPost | deletePost | deleteUser
        var writer byte = writePost | readPost
        var guest byte = readPost
	fmt.Printf("%b\n", administrator)
	fmt.Printf("%b\n", moderator)
	fmt.Printf("%b\n", writer)
	fmt.Printf("%b\n", guest)
}
