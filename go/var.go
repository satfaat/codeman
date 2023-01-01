package main

import (
	"fmt"
	"reflect"
	"strings"
)

func main() {

	var quantity int
	var length, width float64
	var customer_name string

	quantity = 7
	customer_name = "Faat"
	length, width = 2.2, 4.8

	short_qnty := 8
	short_name := "Nemo"

	broken := "G# r#cks"
	replacer := strings.NewReplacer("#", "o")
	fixed := replacer.Replace(broken)

	fmt.Println(reflect.TypeOf(quantity))
	fmt.Println(reflect.TypeOf(length))
	fmt.Println(reflect.TypeOf(true))
	fmt.Println(reflect.TypeOf(customer_name))

	fmt.Println(reflect.TypeOf(float64(short_qnty)))
	fmt.Println(fixed, width, short_name)

	fmt.Printf("A float: %f\n", 3.1415)
	fmt.Printf("An integer: %d\n", 15)
	fmt.Printf("A string: %s\n", "hello")
	fmt.Printf("A boolean: %t\n", false)
	fmt.Printf("Values: %v %v %v\n", 1.2, "\t", true)
	fmt.Printf("Values: %#v %#v %#v\n", 1.2, "\t", true)
	fmt.Printf("Types: %T %T %T\n", 1.2, "\t", true)
	fmt.Printf("Percent sign: %%\n")
}
