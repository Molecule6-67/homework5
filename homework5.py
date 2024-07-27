tuple_0 = 0, 2, 1, 4, 7, "a", "b"
print(tuple_0)
#tuple_0[0]= 0
#print(tuple_0) # Объяснение: т.к кортежи являются упорядоченными коллекциями элементов. Имеенно пожэтому кортежи в отличии от списка является не изменным.
mutable_list = ([1, 2, 3, "A"], "b", "S")
print(mutable_list)
mutable_list[0][1]=0
print(mutable_list)
mutable_list[0][2]=1
print(mutable_list)
mutable_list = (1, 2, [3, "A", "b", "S"])
mutable_list[2][0]="D"
print(mutable_list)