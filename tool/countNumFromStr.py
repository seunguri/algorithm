from collections import Counter
import re

pic = """		
		2027 2028 2030 2038 2039 2040 2041 2043, 2044
"""
nums = re.findall(r'\d+', pic)

counter = Counter(nums)
count_pic = sorted(dict(counter).items(), key = lambda item: item[1], reverse = True)

for c in count_pic:
    print(c[0], ": " , c[1])
