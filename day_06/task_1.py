lanternfish = list(map(int, open("test_input.txt", "r").readline().strip().split(",")))
# index describes day - with 9 possible days - 0,1,2,3,4,5,6,7,8 
by_day = [lanternfish.count(i) for i in range(9)]

for i in range(80):
    # by popping from the front we move each element by one day (subscract one day)
    fish_num = by_day.pop(0)
    
    # add old fish to start at day 6 again
    by_day[6] += fish_num
    
    # add new fish to start at day 8
    by_day.append(fish_num)
    
    
print(f"Fish after 80 days: {sum(by_day)}")