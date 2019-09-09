def change(x):
    change=1024-x
    num64=int(change/64)
    num16=int((change%64)/16)
    num4=int((change%64%16)/4)
    num1=(change%64%16%4)
    num=num64 + num16 + num4 + num1
    print(num)
if __name__ == '__main__':

    x=int(input())
    change(x)
# N = int(input())
# last = 1024 - N
# count = 0
# while last != 0:
#     if last >= 64:
#         count += last // 64
#         last = last - 64 * (last // 64)
#
#     elif last >= 16:
#         count += last // 16
#         last = last - 16 * (last // 16)
#
#     elif last >= 4:
#         count += last // 4
#         last = last - 4 * (last // 4)
#
#     else:
#         count += last
#         last = 0
#
# print (count)
