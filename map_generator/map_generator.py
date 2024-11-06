import numpy as np
from perlin_noise import generate_perlin_noise

def generate_terrain_map(width, height, scale):
    noise_map = generate_perlin_noise(width, height, scale)
    terrain_map = []

    for y in range(height):
        row = []
        for x in range(width):
            value = noise_map[y][x]
            if value < -0.2:
                row.append('water')       # Áreas baixas (água)
            elif value < 0.2:
                row.append('plains')      # Planícies
            elif value < 0.5:
                row.append('hills')       # Colinas
            else:
                row.append('mountains')   # Montanhas
        terrain_map.append(row)

    return np.array(terrain_map)
