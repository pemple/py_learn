# list_score =[]
#
# while True:
#     str_score=input('请输入成绩：')
#     if str_score=='':
#         break
#     list_score.append(int(str_score))
#
# for item in list_score:
#     print(item)
#
# print('最高分'+str(max(list_score)))
# print('最低分'+str(min(list_score)))
# print('平均分'+str(sum(list_score)/len(list_score)))

list = [9,20,8,15]
for i in range(len(list)-1,-1,-1):
    if list[i]>10:
        list.remove(list[i])
print(list)

# result = " ".join(str(list))
# print(result)

for i in range(1,11):
    print(i)


list
