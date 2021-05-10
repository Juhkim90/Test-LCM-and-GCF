# Test 

For this test, you will complete 2 functions. 

## LCM - Least Common Multiple

Given 2 numbers, find their LCM. 

The lowest number that is divisible by both the given values. 

Ex. `compute_lcm(15,25) = 75`

*Hint:  There is no one right answer but here is one way you can approach it. *

1. Create a `greater` variable that holds the value of the greater of the two given values 
2. Inside a while loop (`while(True)`), check if  `greater` is divisible by both the given values 
- If it is not, increase `greater` by one and continue to check the same condition 
- If it is divisible by both, `break` out of the loop and `return` that value 


## GCF - Greatest Common Factor 

Given 2 numbers, find their GCF 

The greatest number that both the given values are divisible by. 

Ex. `compute_gcf(15,25) = 5`

*Hint:  There is no one right answer but here is one way you can approach it. *

1. Create a `smaller` variable that holds the value of the smaller of the two given values 
2. Inside a for loop with range starting at 1 and ending at `smaller + 1`, check if both the given values are divisible by `LCV` 
- If both are divisible, set the LCV (loop control variable) as your new `smaller`
3. `return smaller`