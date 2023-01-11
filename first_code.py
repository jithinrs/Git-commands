html_file = open('index.html', 'w')

hello = ("Hello world!!!")

list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [100,200,99,21,55,77,12,43,4,19]
result_list = []

for i in range(0, len(list_1)):
    result_list.append(list_1[i] + list_2[i])

# print(type(result_list))

result = str("the result is = {}".format(result_list))
print(result)

print(type(result))




html_file.write(result)
html_file.close()