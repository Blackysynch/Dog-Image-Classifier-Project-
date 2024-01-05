with open('./dognames.txt','r') as f:
    dog_names = f.readlines()
    dognames_dic = dict()
    
    for dog_name in dog_names:
        dog_name = dog_name.rstrip()
        if dog_name not in dognames_dic:
            dognames_dic[dog_name] = 1
        else:
            print("{} already in dictionary".format(dogname))
        
        print(dognames_dic)
