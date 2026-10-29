# def check_word():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open('practice_1.txt','r')as f:

#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#         return -1
# check_word()
word = "learning"
line_no = 1
with open('practice_1.txt','r')as f:
    data = True
    while data:
        data = f.readline()
        if word in data:
            print(line_no)
            break
        line_no += 1
    else:
        print(-1)
