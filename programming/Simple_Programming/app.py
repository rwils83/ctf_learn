my_count = 0
with open("data.dat") as f:
    for each_line in f:
        count_ones = 0
        count_zeroes = 0
        for x in each_line:
            if x == "1":
                count_ones += 1
            if x == "0":
                count_zeroes += 1 
        if count_ones % 2 == 0:
            my_count += 1
        elif count_zeroes % 3 == 0:
            my_count += 1 
        print("My count is: " +str(my_count))
