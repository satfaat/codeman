package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	seconds := time.Now().Unix()
	rand.Seed(seconds)
	target := rand.Intn(100) + 1
	fmt.Println("I've chosen a random number between 1 and 100.")
	fmt.Println("Can you guess it?")
	//fmt.Println(target)

	reader := bufio.NewReader(os.Stdin)

	success := false
	try := 6
	for guesses := 0; guesses < try; guesses++ {
		fmt.Println("You have", 10-guesses, "guesses left.")

		fmt.Print("Make a guess: ")
		input, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		input = strings.TrimSpace(input)
		guess, err := strconv.Atoi(input)
		if err != nil {
			log.Fatal(err)
		}

		if guess == target {
			success = true
			fmt.Println("Good job! You guessed it!")
			break
		} else if guess > target {
			fmt.Println("Oops. Your guess was high")
		} else {
			fmt.Println("Oops. Your guess was low.")
		}
	}
	if !success {
		fmt.Println("Sorry, you didn't guess my number. It was:", target)
	}
	fmt.Println("Bye*2")
}
