import random
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import pandas as pd

# 30 days:
Sep = Apr = Jun = Nov = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# 31 days:
Jan = Mar = May = Jul = Aug = Oct = Dec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
# 28 days:
Feb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

def gen_a_birthday():
    return random.randint(1, 365)

def label_a_birthday(date):
    # To convert a number out of 365 to a date
    if date <= 31:
        w_date = str("Jan " + str(date))
    elif 32 <= date <= 59:
        w_date = str("Feb " + str(date - 31))
    elif 60 <= date <= 90:
        w_date = str("Mar " + str(date - 59))
    elif 91 <= date <= 120:
        w_date = str("Apr " + str(date - 90))
    elif 121 <= date <= 151:
        w_date = str("May " + str(date - 120))
    elif 152 <= date <= 181:
        w_date = str("Jun " + str(date - 151))
    elif 182 <= date <= 212:
        w_date = str("Jul " + str(date - 181))
    elif 213 <= date <= 243:
        w_date = str("Aug " + str(date - 212))
    elif 244 <= date <= 273:
        w_date = str("Sep " + str(date - 243))
    elif 274 <= date <= 304:
        w_date = str("Oct " + str(date - 273))
    elif 305 <= date <= 334:
        w_date = str("Nov " + str(date - 304))
    elif 335 <= date <= 365:
        w_date = str("Dec " + str(date - 334))
    else:
        w_date = "bug"
    return w_date

def simulation(max):
    list_of_num_dates = []
    list_of_w_dates = []
    for i in range(max):
        date = gen_a_birthday()
        list_of_num_dates.append(str(date))
        list_of_w_dates.append(str(label_a_birthday(date)))
    if len(list_of_num_dates) != len(set(list_of_num_dates)):
        same = True
        seen = set()
        dupes = [x for x in list_of_w_dates if x in seen or seen.add(x)]
    else:
        same = False
        dupes = None
    return list_of_num_dates, list_of_w_dates, same, dupes

def main():
    for j in range(100):
        print("Sim {}".format(str(j)))
        num_of_bdays = j
        num_of_sims = 10000
        same_counter = 0
        sim_count = 0
        pandas_set = []
        for i in range(num_of_sims):
            num_dates, w_dates, same, dupes = simulation(num_of_bdays)
            # print(f"Simulation {str(i + 1)}:")
            # print("Birthdays: " + ", ".join(w_dates))
            # print(f"Same: {same}")
            if same == True:
                # print("Duplicates: " + ", ".join(dupes))
                same_counter += 1
            sim_count += 1
            pandas_set.append(same_counter/sim_count)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(f"Out of {str(num_of_sims)} simulations, a birthday was shared {same_counter} or {str(round(((same_counter/num_of_sims)*100), 2))}% of the time")
        s = pd.Series(pandas_set)
        s.plot()

main()
plt.show()