if __name__ == '__main__':
    
    # a = open("input_mock")
    a = open("input1")
    b = a.readlines()
    count = b.__len__()
    
    e_iterator = 0
    e_list = [[0, 0]]

    for x in range(count):
        if b[x] == "\n":
            e_iterator += 1
            e_list.append([0, 0])
        else:
            e_list[e_iterator][0] += 1
            e_list[e_iterator][1] += int(b[x])
    
    e_list_temp = [item[1] for item in e_list]
    e_list_temp.sort(reverse=True)

    print("max: ", max(e_list_temp))
    print("top 3: ", e_list_temp[0] + e_list_temp[1] + e_list_temp[2])
    