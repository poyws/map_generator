from noise import pnoise2

def generate_perlin_noise(width, height, scale, octaves=1, persistence=0.5, lacunarity=2.0):
    noise_map = []
    for y in range(height):
        row = []
        for x in range(width):
            noise_value = pnoise2(x / scale, 
                                  y / scale, 
                                  octaves=octaves, 
                                  persistence=persistence, 
                                  lacunarity=lacunarity, 
                                  repeatx=width, 
                                  repeaty=height, 
                                  base=0)
            row.append(noise_value)
        noise_map.append(row)
    return noise_map
