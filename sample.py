
'''
num1 = 10
num2 = 102.34
num3 = 1020+4j
value1 = "ab" \
        "cd"

value2 = 'ab' \
        'cd'
value3 =


flag = True
val = None

print(num1,type(num1))
print(num2,type(num2))
print(num3,type(num3))
print(value1,type(value1))
print(value2,type(value2))
print(value3,type(value3))
print(flag,type(flag))
print(val,type(val))

#complex Datatypes -- can hold hetrogeneous data elements
values = [10,1203.3,'avd',"asjd",True,12993,394+3j]
print(values,type(values))

    complex -- list,set,dict -- can grow   ----tuple  
            - can hold homogenous + hetrogenous data elements
                        same type       diffrt
                        
            
    
    list --  [] or [102,30,40]
            hom + hetro
            preserves seq order
            multiple none types are allowed
            index based retrival --  0 -- len-1  or 
            array - -index - +ve nos started zero till len-1                
            Array  --- Object
            Array  --  the creates new array and copies the existing elements to newly created
                        array and ref will be pointing out to new array instead existing
                        as existing array will not have ref..wil be gc

            mutable
            frequently searching retrival


	extend -- accepts only iterable type -- collection of elements
		will consume single element and will add it into original list
		original list len = original list len + new list len
	appends -- accepts both -- single as well as iterable type
		will consume all as single element and will add it into original list
		original list len = original list len + 1

    set -- set() or {10,20,30}
    dict--- {} or {1:100,2:2003}
    tuple -- () or(10,203,)
    
    
    
    Array -- 
            to hold same type of data elements
            fixed
            index based retrival
            0 to len-1
            
            

t = ()
print(t,type(t))

setv = set()

print(setv,type(setv))

values = (10,1203.3,'avd',"asjd",True,12993,394+3j)
print(values,type(values))



values = {10,1203.3,'avd',"asjd",True,12993,394+3j}
print(values,type(values))

values = {"T":10,"A":1203.3,'avd':"ABC",1023:"asjd",True:"Tabc"}
print(values,type(values))


num =[10,20,30]
num = [10,20,30,40,None,None]    
    
'''


values1 = [10,39,40,40,50,20,30,40,20,304,40,30,40,50]
values1.sort(reverse=True)
print(values1)
#ind = values1.index(40,5,9)

#values1.pop(ind)
#print(values1)

#print('Before' , values1)
#values1.sort(reverse=True)
#print('After' , values1)

#values1[2]=300
#print(values1)
#values1.remove(30)
#print(values1)

#values2 = [10,30,40,50]

#values1.extend([120,203,40,503])
#values2.extend([120])

#values.append(200)
#values.append(2034)
#values.insert(2,3882)
#val = [10,20,30,4050,506]
#values.append(10)

#print(values1)
#print(values2)

