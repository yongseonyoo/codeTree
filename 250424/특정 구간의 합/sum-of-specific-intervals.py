n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def add_val():
    for i in range(m):
        val = 0
        for j in range(queries[i][0], queries[i][1] + 1):
            # print(arr[j-1])
            val += arr[j-1]
        print(val)

add_val()