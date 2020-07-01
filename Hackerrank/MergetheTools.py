def merge_the_tools(string, k):
    # your code goes here
    chunks = int(len(string)/k)

    for index in range(chunks):
        merge = ""
        T = string[index*k : (index+1)*k]
        for ch in T:
            if ch not in merge:
                merge += ch
        print(merge)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
