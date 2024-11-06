from map_generator import generate_terrain_map
from visualization import display_map

def main():
    width, height = 100, 100     # Tamanho do mapa
    scale = 20                   # Controle do detalhamento

    # Gerar o mapa do terreno
    terrain_map = generate_terrain_map(width, height, scale)

    # Exibir o mapa
    display_map(terrain_map)

if __name__ == "__main__":
    main()
