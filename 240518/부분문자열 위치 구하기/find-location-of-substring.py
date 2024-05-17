# a = input()
# b = input()



# a_l = len(a)
# b_l = len(b)

# s = []

# def check(i,c):
#     if c < b_l:
#         if a[i+c] == b[c]:
#             check(i+1,c+1)
#     else:
#         print(i)

# if b in a:
#     for i in range(a_l-b_l+1):
#         check(i, 0)
#         # if a[i] == b[0]:
#         #     if a[i+1] == b[1]:
#         #         if a[i+2] == b[2]:

# else:
#     print(-1)

# # def check(s):
# #     if 

# # for i in a:
# #     if i == b[0]:
# #         s.append(i)


a = input()
b = input()

index = a.find(b)
print(index)