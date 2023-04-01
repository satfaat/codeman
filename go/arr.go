package main

import "fmt"

func main() {
	notes := [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}
	fmt.Println(len(notes), notes)

	for i := 0; i < len(notes); i++ {
		fmt.Println(i, notes[i])
	}

	fmt.Printf("%#v\n", notes)

	fmt.Println("for range cycle")
	for index, note := range notes {
		fmt.Println(index, note)
	}

	for _, note := range notes {
		fmt.Println(note)
	}
}
