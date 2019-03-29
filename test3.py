def main():
    dic = {"a": 1, "b": 2, "c": 3, "d": 4, "key": "solution"}

    print(dic["a"])
    print(dic.get("a"))

    list = [1, 2, 3, 4]

    print()
    print(list)
    print()
    list.pop(0)
    list.remove(2)
    #print("removing: " + str(list.pop(0)))
    print(list)

main()
