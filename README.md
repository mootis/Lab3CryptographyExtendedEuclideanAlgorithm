# ChongParkLab3CSCI4554

Our results are as follows:
1) 105401
2) 11
3) 21301
4) 46108

Primality Tests:<br/>
Fermat) both composite and probably prime <br/>
Miller) composite

To run our program use terminal and clone the repo.<br/> From there navigate to the folder Lab3 and can see the EEA.py file.<br/> Run "python EEA.py" This should return our results.

We were unable to implement a counter for the number of cycles. It was causing errors that we could not figure out. The primality tests are only passed the number to check and not the security key as that was causing issues. You can see the code that we tried to use commented out in the EEA.py file.

CSci 4554 Lab 3: Extended Euclidean Algorithm; primality testing <br/>
Due Monday, November 19th at 11:59pm (by e-mail) <br/>
45 points total <br/>
This lab is done in groups of 2. <br/>

The purpose of the lab is to explore extended Euclidean algorithm and probabilities of finding large primes. The Extended Euclidean algorithm can be implemented for long data type or for BigInteger. For the second part you are to implement both the Fermat primality test and the Miller-Rabin test (see below for details). You will be using it with very large numbers, so use BigInteger class if you are using Java. You may use any programming language, and some have a more seamless implementation of large numbers than Java. However, below I assume Java BigInteger in the instructions.

# Task 1 (20 points): Extended Euclidean Algorithm
You goal is to implement and test the Extended Euclidean algorithm (also given in the textbook). It must be implemented as a function (or a method) that takes r0, r1 as parameters. You also need to write an interactive program that reads two numbers from the user and passes them to your function. 
You may use any programming language, as long as it runs in the CSci labs and you provide clear instructions for how to run it and how to pass data to it.

Test your program on small numbers to make sure it works (submit your test). Then use it to compute the following:

1) Greatest common divisor of 11069529223 and 188351587
2) Coefficients S and T that solve the equation 435985 * S + 288651 * T = 11
3) Multuiplicative inverse of 300 modulo 104759
4) Multiplicative inverse of 300 modulo 104003

# Task 2 (25 points) Implementing and testing primality tests
Your goal is to explore the differences between the two primality tests, and find out how many computations you need to find two large random numbers for different bit lengths.

You will be working with integers of bit lengths 512 and 1024.

Your tasks is to implement the two primality tests with counters for the number of tests you have performed. Specifically you need to:

* Implement Fermat primality test as described in your textbook or here. Set k to some initial number. Add a counter to count the number of candidates a that you tried before you have determined that your nubmer is composite. Your number is prime if you have finished all k tests and didn't find a counterexample. 
Some really helpful methods:
>* The method modPow of BigInteger allows you to calcualte a very large power of a very large number modulo another large number efficiently: it reduces all intermediate results modulo a given N.
>* A BigInteger constructor that allows you to generate a random BigInteger of a given bit length.
>* A BigInteger constructor that generates a random prime integer. You can use it for testing your primality tests, but not for the last task of your lab (fidning the large primes).
* Test your method on numbers that you know to be prime (obtained from the prime number constructor) and on numbers that you know to be composite, such as a product of two large primes, each half the length and a number that has a lot of small prime factors. You need to test it for both the length 512 and 1024 bits (approximately). Record the counters for all your test cases. Adjust k if needed.
* Implement Miller-Rabin test as described in the book or here.
* Test it on a few numbers of bit length 512 and 1024 that you know to be prime (i.e. generated by the prime numbers constructor) or you know to be composite (i.e. generated as a product of two smaller primes). Adjust the number of candidates a you try. Record the number of candidates and operations per candidate.
# Comparing the two primality tests
Try both primality tests on the following number: 9746347772161. Explain your results.

# Finding large primes
Use the Miller-Rabin test to generate two primes of the bit length 512 and two of the bit length 1024. Do not use the prime number constructor. Record the number of random candidates you tried, the number of candidates a for each random candidate, and the average number of operations per candidate a.

Write down your conclusions from comparing these two bit lengths.

# What to submit (by e-mail to me, CC your partner)
All your program code (well-documented) and instructions for running it.
The answers to the questions, with explanations if needed
