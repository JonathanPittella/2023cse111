import math

def main():
    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    print(f"{name} {storage_efficiency:.2f}")

    name = "#1 Tall"
    radius = 7.78
    height = 11.91
    return volume, surf_area, storage_efficiency
    print(f"{name} {storage_efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

main()

print()

import math

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surf_area
    return storage_efficiency

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

def main():
    name = "#1 Picnic"
    radis_picnic = 6.83
    height_picnic = 10.16
    storage_efficiency_picnic = compute_storage_efficiency(radis_picnic, height_picnic)
    print(f"{name} {storage_efficiency_picnic:.2f}")

    name = "#1 Tall"
    radis_tall = 7.78
    height_tall = 11.91
    storage_efficiency_picnic = compute_storage_efficiency(radis_tall, height_tall)
    print(f"{name} {storage_efficiency_picnic:.2f}")

if __name__ == "__main__":
    main()