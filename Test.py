def migratoryBirds(arr):
    freq = [-1, 0, 0, 0, 0, 0]
    freq_len = len(freq)
    arr_len = len(arr)
    max = 0

    # klo klo tipenya 1, masuk ke index 1
    for i in range(0, arr_len):
        freq[arr[i]] += 1

        print("arr[", i, "] = ", arr[i])
        print("freq[", arr[i], "] = ", freq[arr[i]], "\n")

    print("freq = ", end="")
    for i in range(0, freq_len-1):
        print(freq[i], end=", ")
    print("")

    for i in range(0, freq_len-1):
        # print(freq[i], end=", ")
        if i != arr_len:
            print("check is curr max < freq[", i, "]?", end=" | ")
            print(max, "<", freq[i], "?", end=" ")
            if max < freq[i]:
                max = freq[i]
                print("yes. Max = ", max)
            else:
                # max = freq[i+1]
                print("no. Max = ", max)
        else:
            break

    print("max freq = ", max)

    for i in range(0, freq_len-1):
        if freq[i] == max:
            print("out = ", i)
            break

# migratoryBirds([1, 4, 4, 4, 5, 3])
# 0 1 2 3 4 5 6
#-1 1 0 1 3 1 0
# max freq = 3
# out = 4

# migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
# 0 1 2 3 4 5 6
#-1 2 2 3 3 1 0
# max freq = 3
# out = 3

migratoryBirds([1, 1, 2, 2, 3])
# 0 1 2 3 4 5 6
#-1 2 2 1 0 0 0
# max freq = 2
# out = 1