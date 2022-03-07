my_list=[25,26,27,28,29,30]
odd_list=list(filter(lambda x:(x%2!=0),my_list))
print(odd_list)
odd_list=list( map(lambda x:(x%2!=0),my_list))
odd_list=list(map(lambda x:x*2,my_list))
print(odd_list)
