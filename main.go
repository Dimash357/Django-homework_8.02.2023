package main

import (
	"fmt"
	"math/rand"
	"time"
)

func bubbleSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

func main() {
	rand.Seed(time.Now().UnixNano())
	arr100 := rand.Perm(100)
	arr1000 := rand.Perm(1000)

	start := time.Now()
	sortedArr100 := bubbleSort(arr100)
	elapsed := time.Since(start)
	fmt.Println(sortedArr100)
	fmt.Println("100 elements:", elapsed)

	start = time.Now()
	sortedArr1000 := bubbleSort(arr1000)
	elapsed = time.Since(start)
	fmt.Println(sortedArr1000)
	fmt.Println("1000 elements:", elapsed)
}
