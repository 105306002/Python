import time

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        print('i',i)
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fibs(10)
    print(result)


if __name__ == '__main__':
    main()