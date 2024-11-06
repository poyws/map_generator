import matplotlib.pyplot as plt
import numpy as np

def display_map(terrain_map):
    color_map = {
        'water': (0, 0, 0.8),         # Azul para água
        'plains': (0.3, 0.6, 0.3),    # Verde para planícies
        'hills': (0.5, 0.4, 0.2),     # Marrom para colinas
        'mountains': (0.6, 0.6, 0.6)  # Cinza para montanhas
    }

    height, width = terrain_map.shape
    image = np.zeros((height, width, 3))

    for y in range(height):
        for x in range(width):
            terrain_type = terrain_map[y][x]
            image[y, x] = color_map[terrain_type]

    plt.imshow(image)
    plt.axis('off')
    plt.show()
