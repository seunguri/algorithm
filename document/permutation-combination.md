## 정의

#### 순열: 서로 다른 n개중에 r개를 선택하는 경우의 수 ( 순서 상관 있음 )

1. 반복 가능한 객체(=길이가 n인)에 대해서 중복을 허용하지 않고 r개를 뽑아서 나열한다.
2. 뽑힌 순서대로 나열하기 때문에 순서가 의미가 있다. (즉, 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 취급한다.)

nPr = n! / (n-r)!

#### 조합: 서로 다른 n개중에 r개를 선택하는 경우의 수 ( 순서 상관 없음 )

1. 반복 가능한 객체(=길이가 n인)에 대해서 중복을 허용하지 않고 r개를 뽑는다.
2. 어떤 것을 뽑는지만 중요하게 보기 때문에 뽑은 순서는 고려하지 않는다.

nCr = n! / (n-r)!r!

### 순열 Permutations

- itertools mudule

```
from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")
```

- recursive

```python
def permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for (i, num) in enumerate(arr):
        for j in permutations(arr[:i] + arr[i+1:], n-1):
            result.append([num] + j)
    return result

permutation = permutations([1,2,3,4], 3)
print(permutation)
```

### 조합 Combinations

- itertools

  ```
  from itertools import combinations

  for i in combinations([1,2,3,4], 2):
      print(i, end=" ")

  ```

- recursive

  ```
  def combinations(arr, n):
      result = []

      if n == 0:
          return [[]]

      for (i, num) in enumerate(arr):
          for j in combinations(arr[i+1:], n-1):
              result.append([num] + j)
      return result

  combination = combinations([1,2,3,4], 3)
  print(combination)
  ```
