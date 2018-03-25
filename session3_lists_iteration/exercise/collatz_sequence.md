### The Collatz Sequence

Given a positive integer as a starting point, we can generate a sequence of numbers according to the following algorithm:
1. If n is even, create a new number by dividing n by 2;  if it is odd, multiply by 3 and add 1
2. Repeat this process until you arrive at the number 1.

This is known as the Collatz sequence or the Hailstone sequence associated with the starting number.   The Collatz conjecture states that given any positive starting number n, the sequence will eventually terminate at 1.   This has not been proven mathematically, but it is true for every number anyone has ever tested.

Write a function that returns the Collatz sequence of a given number.  The sequence should be returned as a list of numbers.

For example, if we evaluation collatz_seq(5), we should get:
[ 5,16,8,4,2,1 ]

collatz_seq(20) will yield:
[ 20, 10, 5, 16, 8, 4, 2, 1 ] 

