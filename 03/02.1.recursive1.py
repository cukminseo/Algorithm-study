def GetSome(count):
    if count == 0: return
    GetSome(count-1)
    print("재귀 호출 %d" %count)

GetSome(3)
