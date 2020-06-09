# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((data, new_record))

print(data.shape)

print(census.shape)

age = np.array(census[:,0])

max_age = np.max(age)
print('Max age:', max_age)

min_age = np.min(age)
print('Min age:', min_age)

age_mean = np.mean(age)
print('Age mean:', age_mean)

min_age = np.min(age)
print('Min age:', min_age)

age_std = np.std(age)
print('Age Standard Deviation:', age_std)

race_0 = len(census[census[:,2] == 0])
race_1 = len(census[census[:,2] == 1])
race_2 = len(census[census[:,2] == 2])
race_3 = len(census[census[:,2] == 3])
race_4 = len(census[census[:,2] == 3])

lengths = [race_0,race_1,race_2,race_3,race_4]
print(lengths)

minority_race = lengths.index(min(lengths))
print('Minority Race Count: ',minority_race)

senior_citizens = census[census[:,0] > 60]

working_hours_sum = np.sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)

print(working_hours_sum)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)



