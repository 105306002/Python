import sys

class MyError(Exception):
    def __str__(self):
        return "I`m a self-defined Error!"

def main(): #判斷是否在啟動程式時輸入了命令列參數
    try:
        print("******start main***********")
        if len(sys.argv) == 1:
            raise MyError()
        print("******end of main**********")
    except MyError, e:
        print(e)

if __name__ == '__main__':
    main()                                                                 