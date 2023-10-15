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

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    pressure_loss = (friction_factor * pipe_length * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

pipe_diameter = 0.05
pipe_length = 100
friction_factor = 0.02
fluid_velocity = 2


pressure_loss = pressure_loss_from_pipe(pipe_length, friction_factor, fluid_velocity, pipe_diameter)
print(pressure_loss)