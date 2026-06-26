# counter and sorting according to frequency  gives O(nlogn) time and O(n) space. Also same for heap approach
# Optimal bucket sort give o(n)
from collections import Counter

def topKFrequent(nums, k):
    freq = Counter(nums)

    sorted_items = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [num for num, count in sorted_items[:k]]

#  heapq approach
from collections import Counter
import heapq

def topKFrequent(nums, k):
    freq = Counter(nums)

    return heapq.nlargest(
        k,
        freq.keys(),
        key=freq.get
    )


# Bucket sort 
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)

    freq = [[] for _ in range(len(nums) + 1)]

    for num, c in count.items():
        freq[c].append(num)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)

            if len(res) == k:
                return res