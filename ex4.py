cars = 100 # 定义汽车数量
space_in_a_car = 4 # 定义汽车载客数
drivers = 30 # 定义司机数量
passengers = 90 # 定义乘客数量
cars_not_driven = cars - drivers # 定义空车数量
cars_driven = drivers # 定义出车数量
carpool_capacity = cars_driven * space_in_a_car # 定义总载客数
average_passengers_per_car = passengers / cars_driven # 定义平均载客数量
# average_passengers_per_car = carpool_capacity / passengers 

print("There are", cars, "cars available.") # 打印空余汽车数量
print("There are only", drivers, "drivers available.") # 打印司机数量
print("There will be", cars_not_driven, "empty cars today.") # 打印今日空车数量
print("We can transport", carpool_capacity, "people today.") # 打印转运容量
print("We have", passengers, "to carpool today.") # 打印乘客数
print("We need to put about", average_passengers_per_car,
      "in each car.") # 打印平均载客数