package main

import (
	"fmt"
	"reflect"
)

var meters_per_liter float64

func paint_need(width float64, height float64) (float64, error) {
	if width < 0 {
		return 0, fmt.Errorf("A width of %.2f is invalid", width)
	}
	if height < 0 {
		return 0, fmt.Errorf("A width of %.2f is invalid", height)
	}
	area := width * height
	return area / meters_per_liter, nil
}

func double(number *int) {
	*number *= 2
}

func main() {
	meters_per_liter = 10.0
	var amount, total float64
	//err := errors.New("Height can't be negative")

	amount, err := paint_need(4.2, -3.0)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("%.2f liters needed\n", amount)
	}
	//log.Fatal(err)
	total += amount
	amount, err = paint_need(5.2, 3.5)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("%.2f liters needed\n", amount)
	}
	total += amount
	fmt.Printf("Total: %0.2f liters\n", total)

	var myInt int
	fmt.Println(reflect.TypeOf(&myInt))
	var myFloat float64
	fmt.Println(reflect.TypeOf(&myFloat))
	var myBool bool
	fmt.Println(reflect.TypeOf(&myBool))

	num := 6
	double(&num)
	fmt.Println(num)
}
