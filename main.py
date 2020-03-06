import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubbleSort import bubblesort
from selectionSort import selectionsort
from quickSort import quicksort
from mergeSort import mergesort
from insertionSort import insertionsort


# n is the number of random data to be sorted
n = int(input("Enter number of integers to sort: "))
method = "Enter sorting method:\n1. Bubble sort\n2. Insertion sort\n3. Merge sort \
    \n4. Quick sort\n5. Selection sort\n"
method = input(method)

# Build and randomly shuffle list of integers.
listOfRandomIntegers = [x + 1 for x in range(n)]
random.seed(time.time())
random.shuffle(listOfRandomIntegers)

# call sorting algorithm method based on user input
if method == "1":
    graphTitle = "Bubble sort"
    generator = bubblesort(listOfRandomIntegers)
elif method == "2":
    graphTitle = "Insertion sort"
    generator = insertionsort(listOfRandomIntegers)
elif method == "3":
    graphTitle = "Merge sort"
    generator = mergesort(listOfRandomIntegers, 0, n - 1)
elif method == "4":
    graphTitle = "Quicksort"
    generator = quicksort(listOfRandomIntegers, 0, n - 1)
elif method == "5":
    graphTitle = "Selection sort"
    generator = selectionsort(listOfRandomIntegers)
else:
    print("Wrong input. Exiting now")
    exit(0)

# Initialize figure and axis.
fig, ax = plt.subplots()
ax.set_title(graphTitle)

graphBars = ax.bar(range(len(listOfRandomIntegers)), listOfRandomIntegers, align="edge")

# Set the x range and y range
ax.set_xlim(0, n)
ax.set_ylim(0, int(1.07 * n))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
iteration = [0]


def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))


# shows the sorting of the data on the bar graph
anim = animation.FuncAnimation(fig, func=update_fig,
                               fargs=(graphBars, iteration), frames=generator, interval=1,
                               repeat=False)
plt.show()
