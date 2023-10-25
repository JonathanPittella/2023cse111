def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height / 4)
    return h

tower_height = 10 
tank_height = 8

water_height = water_column_height(tower_height, tank_height)
print(water_height)

def pressure_gain_from_water_height(height):
    pressure = (density_water * gravity * height) / 1000  # pressure in kilopascals
    return pressure

density_water = 998.2  # density of water in kg/m^3
gravity = 9.80665  # acceleration due to Earth's gravity in m/s^2


# Example usage
water_height = 10  # height of the water column in meters
pressure = pressure_gain_from_water_height(water_height)
print(pressure)

def pressure_loss_from_fitting(fluid_velocity, quantity_fittings):
    density_water = 998.2
    constant = 0.04 / 2000

    pressure_loss = -constant * density_water * fluid_velocity**2 * quantity_fittings
    return pressure_loss

def reynold_number(hydraulic_diameter, fluid_velocity, viscosity):
    density_water = 998.2
    
    the_reynold_number = (density_water * hydraulic_diameter * fluid_velocity) / viscosity
    return the_reynold_number

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    pressure_loss = (friction_factor * pipe_length * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

pipe_diameter = 0.05
pipe_length = 100
friction_factor = 0.02
fluid_velocity = 2


pressure_loss = pressure_loss_from_pipe(pipe_length, friction_factor, fluid_velocity, pipe_diameter)
print(pressure_loss)


def pressure_gain_from_water_height(height):
    density_water = 998.2  # density of water in kg/m^3
    gravity = 9.80665  # acceleration due to Earth's gravity in m/s^2
    pressure = (density_water * gravity * height) / 1000  # pressure in kilopascals
    return pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2
    constant = 0.04 / 2000
    pressure_loss = -constant * density_water * fluid_velocity**2 * quantity_fittings
    return pressure_loss

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_water = 998.2
    dynamic_viscosity = 0.0010016

    #calculate_reynolds = (density_water * larger_diameter * fluid_velocity) / dynamic_viscosity
    
    larger_diameter = 0.28687
    fluid_velocity = 1.65
    smaller_diameter = 0.048692
    reynolds_number = (density_water * larger_diameter * fluid_velocity) / dynamic_viscosity

    k = 0.1 + 50 * reynolds_number / (larger_diameter / smaller_diameter)**4 - 1
    pressure_loss = -k * density_water * fluid_velocity**2 / 2000
    return pressure_loss

def reynolds_number(diameter, fluid_velocity):
    density_water = 998.2
    dynamic_viscosity = 0.0010016

    hydraulic_diameter = diameter

    reynolds_number = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds_number

diameter = float(input("Enter the diameter of the pipe (in meters): "))
velocity = float(input("Enter the velocity of water (in meters/second): "))

reynolds_number_value = reynolds_number(diameter, velocity)
print(f"Reynolds number: {reynolds_number_value:.2f}")

PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters (11.294 inches)
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters / second

HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters (1.917 inches)
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters / second

def main():
    tower_height = 36.6
    tank_height = 9.1
    length1 = 1524.0
    quantity_angles = 3
    length2 = 15.2
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    fluid_velocity = SUPPLY_VELOCITY
    quantity_fittings = quantity_angles

    reynolds = reynolds_number(diameter, velocity)
    
    loss = pressure_loss_from_pipe(diameter, length1, friction, fluid_velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, fluid_velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    fluid_velocity = HOUSEHOLD_VELOCITY
    reynolds = reynolds_number(diameter, fluid_velocity)
    quantity_fittings = 0  # Assuming no fittings in the household pipe
    loss = pressure_loss_from_pipe(diameter, length2, friction, fluid_velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()