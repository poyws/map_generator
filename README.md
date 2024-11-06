# Gerador de Mapas Procedurais

Este projeto é um **Gerador de Mapas Procedurais** desenvolvido em Python, utilizando o algoritmo de **Perlin Noise** para criar terrenos variados, como água, planícies, colinas e montanhas. Este gerador pode ser usado para simular terrenos em jogos ou simulações, com visualização em diferentes cores para cada tipo de elevação.

## Funcionalidades

- **Geração de Terreno com Perlin Noise**: Cria mapas procedurais com diferentes elevações ajustáveis por parâmetros.
- **Classificação de Tipos de Terreno**: Terrenos como água, planícies, colinas e montanhas são identificados automaticamente.
- **Visualização com Matplotlib**: Exibe o mapa como uma imagem colorida, onde cada tipo de terreno recebe uma cor específica.

## Estrutura do Projeto

```plaintext
map_generator_project/
├── main.py                    # Arquivo principal para executar o projeto
├── map_generator/             # Pasta para os módulos de geração do mapa
│   ├── __init__.py            # Torna a pasta um pacote Python
│   ├── perlin_noise.py        # Módulo para geração de Perlin Noise
│   └── map_generator.py       # Módulo para geração do mapa de terreno
├── visualization/             # Pasta para os módulos de visualização
│   ├── __init__.py            # Torna a pasta um pacote Python
│   └── visualization.py       # Módulo para exibir o mapa
└── requirements.txt           # Lista de dependências do projeto


Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
