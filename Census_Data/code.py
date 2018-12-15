# --------------
# Importing header files
import numpy as np
path
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n", data)
print("\nType of data: \n\n", type(data))
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

census = np.concatenate((data,new_record))
# Path of the file has been stored in variable called 'path'

#New record

#Code starts here



# --------------
#Code starts here
age = census[...,0]
print(age)
max_age=np.max(age)
min_age=np.min(age)
print(max_age)
print(min_age)
age_mean= np.mean(age)
age_std=np.std(age)


# --------------
#Code starts here
#census=census[...,2]
#print(census)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0 =len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

list1 = [len_0,len_1,len_2,len_3,len_4]

val=np.min(list1)
minority_race =list1.index(val)
print(minority_race)



# --------------
#Code starts here
#senior_citizens=np.extract(np.array(census[...,0]>60),census[...,0])
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum = senior_citizens.sum(axis=0)[6]
#print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
#print(senior_citizens_len)
avg_working_hours = working_hours_sum /senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high =census[census[:,1]>10]
low =census[census[:,1]<=10]
sum_High =high.sum(axis=0)[7]
avg_pay_high = sum_High/len(high)

sum_Low =low.sum(axis=0)[7]
avg_pay_low=sum_Low/len(low)
print(avg_pay_high)
print(avg_pay_low)



