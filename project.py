# Project for Calculating Aircraft Performance with preliminary data 
fuel_capacity = 1000 # gallons
fuel_consumption_rate = 50
true_air_speed = 150 # knots

payload = 5000 # pounds

fuel_weight = 6000 # pounds

moment_list = [10000, 2500] # pound-feet
total_weight = 1500 # pounds

cl = 1.5 # lift coefficient

rho = 1.225 # air density in kg/m"3

v =100 # velocity in m/s

s = 20 # wing area in m"2

cd = 0.02 # drag coefficient

mass = 5000 # mass in kg

g = 9.81 # acceleration due to gravity in m/s"2
thrust = 6000 # thrust in N
drag = 5000
velocity = 50
acceleration = 2
time = 10


def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    range_in_hours = fuel_capacity / fuel_consumption_rate
    range_in_miles = range_in_hours * true_air_speed
    return range_in_miles

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    endurance_in_hours = fuel_capacity / fuel_consumption_rate
    return endurance_in_hours

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight 

def calculate_cg_positions(moment_list, total_weight):
    total_moment = sum(moment_list)
    cg = total_moment / total_weight
    return cg

def calculate_moment(weight, arm):
    return weight * arm

def calculate_lift(cl, rho, v, s):
    return 0.5*cl*rho*v**2*s

def calculate_drag(cd, rho, v, s):
    return 0.5*cl*rho*v**2*s

def calculate_weight(mass,g):
    return mass * g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust-drag-weight)/mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration*time

def distancee(velocity,time):
    return velocity*time

def print_aspects(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    print("Aircraft Performance Calculations:")
    print("Range: {} miles".format(range))
    print("Endurance: {} hours".format(endurance))
    print("Total Weight: {} pounds".format(total_weight))
    print("Center of Gravity Position: {} inches".format(cg_position))
    print("Lift: {} pound-feet".format(lift))
    print("Drag: {} pound-feet".format(drag))
    print("Weight: {} pounds".format(weight))
    print("Acceleration: {} m/s^2".format(acceleration))
    print("Velocity: {} m/s".format(velocity))
    print("Distance: {} miles".format(distance))

range = calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed)

endurance = calculate_endurance(fuel_capacity, fuel_consumption_rate)

total_weight = calculate_total_weight(payload, fuel_weight)

cg_position = calculate_cg_positions(moment_list, total_weight)

lift = calculate_lift(cl, rho, v, s)

drag = calculate_drag(cd, rho, v, s)

weight = calculate_weight(mass, g)

acceleration = calculate_acceleration(thrust, drag, weight, mass)

velocity = calculate_velocity(velocity, acceleration, time)

distance = distancee(velocity, time)

print_aspects(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance)

def save_information_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    file.write("Performance Calculations:\n")
    file.write("Range: {} miles\n".format(range))
    file.write("Endurance: {} hours\n".format(endurance))
    file.write("Total Weight: {} pounds\n".format(total_weight))
    file.write("Center of Gravity Position: {} inches\n".format(cg_position))
    file.write("Lift: {} pound-feet\n".format(lift))
    file.write("Drag: {} pound-feet\n".format(drag))
    file.write("Weight: {} pounds\n".format(weight))
    file.write("Acceleration: {} m/s^2\n".format(acceleration))
    file.write("Velocity: {} m/s\n".format(velocity))
    file.write("Distance: {} miles\n".format(distance))
    file.close()

with open("aircraft_performance_analysis.txt", "w") as f:
    save_information_to_file(range, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, f)