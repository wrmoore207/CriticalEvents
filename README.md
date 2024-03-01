# CriticalEvents

## Problem Description:

You are tasked with developing an algorithm to identify and count 'critical' events in an array of integers. A 'critical' event is defined as follows: given an array A of integers and a threshold value 't', an event E between indices i < j is considered 'critical' if the value at index i (a[i]) is greater than 't' times the value at index j (t * a[j]).

Input:

An array A of n integers (1 <= n <= 10^5), representing the elements of the array.
A threshold value 't' (0 <= t <= 100).
Output:

An integer representing the count of 'critical' events in the given array based on the specified threshold value.

## Function Signature

```
def search(arr: List[int], t: float) -> int:
    """
    Count the number of 'critical' events in the given array based on the threshold value.

    Parameters:
    - arr: List of integers representing the array elements.
    - t: Threshold value.

    Returns:
    - An integer representing the count of 'critical' events.
    """
    # Implementation goes here


arr = [6, 2, 8, 1, 9, 34, 2]
t = 2
result = search(arr, t)
Output: 3
```

Explanation:
In the given example, the 'critical' events occur at the following indices:

(arr[0] > t * arr[1])
(arr[2] > t * arr[3])
(arr[4] > t * arr[5])
Therefore, the total count of 'critical' events is 3.