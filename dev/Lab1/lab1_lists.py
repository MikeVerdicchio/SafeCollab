# Mike Verdicchio, mpv3ms
# CS 3240, Lab 1
# January 25, 2016
# lab1_lists.py

def maxmin(list):
    if not list:
        return None

    max = list[0]
    min = list[0]

    for i in range(0, len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]

    ans = (max, min)
    return ans

def common_items(list1, list2):
    ans = []

    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            for k in range(0, len(ans)):
                if list1[i] == ans[k]:
                    break
            if list1[i] == list2[j]:
                ans.append(list1[i])

    return ans

if __name__ == "__main__":
    test1 = [8, 9, 1672, 384, 192843, -10]
    test2 = []
    test3 = ['Q', 'Z', 'C', 'A']
    print(maxmin(test1))
    print(maxmin(test2))
    print(maxmin(test3))
    print()

    test4 = [1, 2, 3, 4, 5, 6]
    test5 = [4, 5, 6, 7, 8, 9]
    test6 = [7, 8]
    print(common_items(test4, test5))
    print(common_items(test4, test6))