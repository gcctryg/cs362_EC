array = []


while True:
    input_int = input("Enter integer in the array (type 'Done' to stop): ")
    if input_int == "Done":
        break
    else:
        input_int = int(input_int)
        array.append(input_int)
#print(array)

target_sum = int(input("Enter a targer sum: "))

for x in range(0, len(array)-1):
    for y in (1, len(array)-1):
        if array[x] + array[y] == target_sum:
             print("Result - [" + str(array[x]) + "," + str(array[y]) + "]")
             break



        # if array[x] + array[y] == target_sum:
        #     print("Result - [", array[x], ",", array[y], "]")
        #     break