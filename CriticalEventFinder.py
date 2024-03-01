"""
Ryan Moore
Problem: Given an array A of integers and a particular threshold value t, an event E between indices i<j
is a 'critical' event if a[i]>t*a[j]

Solution: Front and Back linear search will be marginally faster than traditional linear search. 
In front-back linear search, there are two cursors evaluating the poles of the array. 

On the front cursor, everything to the left is searched while everything to the right up to a middle partition is unsearched.
On the back cursor, everything to the right is searched while everything to the left up to the middle partition is unsearched. 

At each iteration of the loop, the algorithm will evaluate the values stored at a[front] and a[back]. If a critical event
is encountered, E will be incremented by 1. At the termination of the program, the entire array will have been searched,
and the algorithm will return the value of E.  
"""

from array import*

def search(arr, t):
    # Initialize the counter for critical events
    e = 0
    # Initialize front and back cursors
    front = 0
    back = len(arr) - 1

    # Continue the loop until front and back cursors meet or pass each other
    while front <= back:
        # Check for a critical event on the front and back cursors
        if arr[front] > (arr[front + 1]) * t or arr[back - 1] > (arr[back] * t):
            # Increment the count of critical events
            e += 1
        
        # Move the front cursor to the right
        front += 1
        # Move the back cursor to the left
        back -= 1

    # Return the total count of critical events
    return e

if __name__ == "__main__":
    # Example array and threshold value
    arr = [6, 2, 8, 1, 9, 34, 2]
    x = 2

    # Function call
    result = search(arr, x)
    # Print the result
    print(result)
