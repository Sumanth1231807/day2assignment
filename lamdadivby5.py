mylist=[i for i in range(1,10)]
div=list(map(lambda x:(x&5)==0,mylist))
square=list(map(lambda a:(a*a),mylist))
newlist=[i for i in range(1,10)]
square_exponent=list(map(lambda a:(a**2),newlist))
print(div)
print(square)
print(square_exponent)