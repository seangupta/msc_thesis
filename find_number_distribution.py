import numpy as np
import matplotlib.pyplot as plt

nums = \
{1: 17,
2: 70,
3: 245,
4: 489,
5: 796,
6: 1831,
7: 3775,
8: 4371,
9: 5305,
10: 5642,
11: 5495,
12: 5299,
13: 4939,
14: 3518,
15: 2945,
16: 2462,
17: 2032,
18: 1572,
19: 1482,
20: 1467,
21: 1410,
22: 1362,
23: 1226,
24: 1217,
25: 1101,
26: 688,
27: 902,
28: 712,
29: 709,
30: 895,
31: 581,
32: 726,
33: 397,
34: 326,
35: 451,
36: 329,
37: 263,
38: 301,
39: 138,
40: 183,
41: 242,
42: 228,
43: 116,
44: 81,
45: 113,
46: 136,
47: 43,
48: 71,
49: 17,
50: 72,
51: 16,
58: 9,
60: 1,
65: 14,
75: 19,
90: 90}

l = []
for key in nums:
    l.extend([key for i in range(nums[key])])

plt.hist(l, bins=20)
plt.xlabel("Number count")
plt.ylabel("Frequency")
plt.savefig("/Users/seangupta/Google Drive/Studies/UCL/Thesis/distribution")