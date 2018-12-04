# Dynamic programming on the example of the n-th Fibonacci number.

**Dynamic Programming** - it's a way of making your algorithm more efficient by storing some intermedia results. It works really well when algorithm has a lot of repetitive parts, so you don't have to repeat this parts over and over again.

## Content 

* [Recursion solution](https://github.com/DaveFres/Python_Projects/tree/master/Interesting_Tasks/Fibonacci_n/Recursive) : The easiest solution to implement. But there are many repetitive parts. Also T(n) = O(2^n).
* [Memoize solution](https://github.com/DaveFres/Python_Projects/tree/master/Interesting_Tasks/Fibonacci_n/Store_Memoize) : In this solution, we store the repetitive parts using DP principles. T(n) = O(n).
* [Bottom-up solution](https://github.com/DaveFres/Python_Projects/tree/master/Interesting_Tasks/Fibonacci_n/Bottom_Up) : The bottom-up approach is similar to the Memoize solution. But in the bottom-up approach we explicitly build array from left to right instead of build it recursively. T(n) = O(n).
