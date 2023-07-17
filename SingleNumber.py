def singleNumber(numberList):
    result = 0

    for i in range(len(numberList)):
        result ^= numberList[i]

    return result


if __name__ == "__main__":
    numberList = list(map(int, input().strip('[').strip(']').split(',')))

    print(singleNumber(numberList))
