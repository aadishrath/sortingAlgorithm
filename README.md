# Visualize Sorting Algorithms
See how different sorting algorithms sort sample data
### Data Length
| 1    |     logn	 |n, n^2, n^3,...| 2^n  | 
|   :---:| :---:   | :---:    |  :---:    |
|constant|logarithm|polynomial|exponential|

- The further right they are, the longer it takes.

### Time complexity
| Algorithm    |      Best	 |   Average	  |    Worst	   | 
|   :---:      |     :---:   |     :---:    |     :---:    |										 
|Selection Sort|	   Ω(n^2)	 |    θ(n^2)	  |    O(n^2)    |
|Bubble Sort   |     Ω(n)	   |    θ(n^2)	  |    O(n^2)    |
|Insertion Sort|	   Ω(n)	   |    θ(n^2)	  |    O(n^2)    |
|Heap Sort	   | Ω(n log(n)) |  θ(n log(n))	|  O(n log(n)) |
|Quick Sort	   | Ω(n log(n)) |  θ(n log(n))	|    O(n^2)    |
|Merge Sort	   | Ω(n log(n)) |	θ(n log(n))	|  O(n log(n)) |
|Bucket Sort   |   	Ω(n+k)	 |    θ(n+k)	  |    O(n^2)    |
|Radix Sort	   |    Ω(nk)	   |    θ(nk)	    |    O(nk)     |
- n: array length
- k: constant
### Algorithm Definitions
<details>
<summary>Big-O notation O(n):</summary>
	<p>- With big O notation we express the runtime in terms of how quickly it grows relative to the input, as the input gets arbitrarily large.</p>
	<p>- The Big O notation defines an upper bound of an algorithm, it bounds a function only from above.</p>
	 <img src="https://media.geeksforgeeks.org/wp-content/uploads/AlgoAnalysis-2.png">
</details>
<details>
<summary>Theta Notation Θ(n):</summary>
	<p>- The theta notation bounds a functions from above and below, so it defines exact asymptotic behavior.</p>
	<p>- A simple way to get Theta notation of an expression is to drop low order terms and ignore leading constants.</p>
	<img src="https://media.geeksforgeeks.org/wp-content/uploads/AlgoAnalysis-1.png">
</details>
<details>
<summary>Omega Notation Ω(n):</summary>
	<p>- It provides an asymptotic lower bound.</p>
	<p>- Can be useful when we have lower bound on time complexity of an algorithm.</p>
	<img src="https://media.geeksforgeeks.org/wp-content/uploads/AlgoAnalysis-3.png">
</details>
