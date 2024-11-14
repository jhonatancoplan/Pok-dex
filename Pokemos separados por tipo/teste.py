import pypokedex
import os
import re
import requests

# Dicionário de traduções dos tipos de Pokémon e outras palavras-chave
translations = {
    "types": "tipos",
    "base_stats": "estatísticas base",
    "sprite": "imagem",
    "Pokédex": "Pokédex",
    "Fire": "Fogo",
    "Water": "Água",
    "Grass": "Planta",
    "Electric": "Elétrico",
    "Psychic": "Psíquico",
    "Ghost": "Fantasma",
    "Dark": "Sombrio",
    "Fairy": "Fada",
    "Bug": "Inseto",
    "Normal": "Normal",
    "Fighting": "Luta",
    "Flying": "Voador",
    "Poison": "Veneno",
    "Ground": "Terrestre",
    "Steel": "Aço",
    "Ice": "Gelo",
    "Dragon": "Dragão",
    "Rock": "Pedra"
}

# Dicionário de cores para os tipos
type_colors = {
    "Fire": "#F08030",
    "Water": "#6493EB",
    "Grass": "#74CB48",
    "Electric": "#F8D030",
    "Psychic": "#F85888",
    "Ghost": "#705898",
    "Dark": "#6F6F6F",
    "Fairy": "#EE99AC",
    "Bug": "#A8B820",
    "Normal": "#A8A878",
    "Fighting": "#C03028",
    "Flying": "#A890F0",
    "Poison": "#A040A0",
    "Ground": "#E0C068",
    "Steel": "#B8B8D0",
    "Ice": "#98D8D8",
    "Dragon": "#7038F8",
    "Rock": "#B8A038"
}

# Função para traduzir os tipos de Pokémon
def translate_type(type_):
    return translations.get(type_.capitalize(), type_)

# Função para gerar um HTML de tipo estilizado com cor
def get_type_html(type_):
    translated_type = translate_type(type_)
    color = type_colors.get(type_, "#A8A878")  # Usar a cor padrão "Normal" se o tipo não tiver cor
    return f'<span class="badge" style="background-color: {color}; color: white;">{translated_type}</span>'

# Função para limpar e formatar o nome do arquivo (remover espaços, acentos, etc)
def sanitize_filename(name):
    name = name.strip().lower()  # Tornar tudo minúsculo
    name = re.sub(r'[^a-z0-9á-úçãõáàâãéêíóôúà]+', '_', name)  # Permitir acentos e caracteres especiais
    return name

# Função para obter a URL da imagem do Pokémon do site
def get_pokemon_image_url(pokemon):
    try:
        pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.dex}"
        response = requests.get(pokemon_url)
        response.raise_for_status()  # Levanta uma exceção se houver erro na requisição
        data = response.json()
        return data['sprites']['front_default']
    except Exception as e:
        print(f"Erro ao buscar imagem para {pokemon.name}: {e}")
        return None

# Função para formatar as estatísticas base para exibição
def format_base_stats(base_stats):
    return f"HP: {base_stats.hp}, Ataque: {base_stats.attack}, Defesa: {base_stats.defense}, " \
           f"Sp. Ataque: {base_stats.sp_atk}, Sp. Defesa: {base_stats.sp_def}, Velocidade: {base_stats.speed}"

# Função para criar o arquivo PHP com informações do Pokémon
def create_pokemon_php(pokemon):
    try:
        if not pokemon.name or not pokemon.types or not pokemon.base_stats:
            print(f"Dados incompletos para o Pokémon {pokemon.name}. Pulando...")
            return
        
        file_name = f"{sanitize_filename(pokemon.name)}.php"
        translated_types = [get_type_html(type_) for type_ in pokemon.types]
        pokemon_image_url = get_pokemon_image_url(pokemon)
        
        if not pokemon_image_url:
            print(f"Imagem não encontrada para {pokemon.name}. Pulando...")
            return
        
        formatted_base_stats = format_base_stats(pokemon.base_stats)
        
        # Traduzir o tipo para usar no link
        translated_type_links = [sanitize_filename(translate_type(type_)) for type_ in pokemon.types]
        
        # Nome do Pokémon (mantendo a capitalização original, mas exibe em maiúsculas no título da página)
        pokemon_name = pokemon.name  # Nome original do Pokémon
        pokemon_name_upper = pokemon_name.upper()  # Nome em maiúsculas para exibição no título
        
        # Criar o conteúdo HTML com o link para o tipo correspondente
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>{pokemon_name_upper} - Pokédex</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {{
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }}
                .badge {{
                    font-size: 14px;
                    padding: 8px 12px;
                    margin: 2px;
                    border-radius: 12px;
                }}
                .container {{
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .card {{
                    border: none;
                    border-radius: 12px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }}
                .img-fluid {{
                    max-width: 100%;
                    height: auto;
                }}
                .card-body {{
                    padding: 15px;
                }}
            </style>
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center mb-4">{pokemon_name_upper}</h1>
                <div class="row justify-content-center">
                    <div class="col-md-4">
                        <img src="{pokemon_image_url}" class="img-fluid rounded-start" alt="{pokemon_name_upper}">
                    </div>
                    <div class="col-md-8">
                        <div class="card mb-3">
                            <div class="row g-0">
                                <div class="col-md-12">
                                    <div class="card-body">
                                        <h5 class="card-title">{pokemon_name}</h5>  <!-- Nome original do Pokémon -->
                                        <p class="card-text">
                                            <strong>Tipos:</strong> {', '.join(translated_types)}
                                        </p>
                                        <p class="card-text">
                                            <strong>Estatísticas:</strong> {formatted_base_stats}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-3">
                    <!-- Modificando o link para direcionar para a página do tipo -->
                    <a href="{translated_type_links[0]}.php" class="btn btn-primary">Voltar para o tipo</a>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Especificando codificação UTF-8 ao abrir o arquivo
        if os.path.exists(file_name):
            print(f"Arquivo {file_name} já existe, não será sobrescrito.")
        else:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"Arquivo PHP para {pokemon_name} criado com sucesso!")
    
    except Exception as e:
        print(f"Erro ao criar o arquivo para o Pokémon {pokemon.name}: {str(e)}")

# Função para atualizar o catálogo do tipo
def update_type_catalog(pokemon):
    try:
        for type_ in pokemon.types:
            type_html = get_type_html(type_)
            translated_type = translate_type(type_)
            type_filename = f"{sanitize_filename(translated_type)}.php"
            
            pokemon_image_url = get_pokemon_image_url(pokemon)
            
            if not pokemon_image_url:
                print(f"Imagem não encontrada para {pokemon.name}. Pulando...")
                return
            
            # Garantir que o arquivo do tipo tenha o Bootstrap
            if not os.path.exists(type_filename):
                with open(type_filename, 'w', encoding='utf-8') as f:
                    f.write(f"""
                    <!DOCTYPE html>
                    <html lang="pt-br">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        <title>{translated_type} - Pokédex</title>
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
                        <style>
                            body {{
                                background-color: #f4f4f4;
                                font-family: Arial, sans-serif;
                            }}
                            .badge {{
                                font-size: 14px;
                                padding: 8px 12px;
                                margin: 2px;
                                border-radius: 12px;
                            }}
                            .container {{
                                background-color: #fff;
                                padding: 20px;
                                border-radius: 8px;
                                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container mt-5">
                            <h1 class="text-center">{translated_type}</h1>
                            <div class="row">
                    """)
            
            # Nome do Pokémon (mantendo a capitalização original)
            pokemon_name = pokemon.name
            pokemon_name_upper = pokemon_name.upper()  # Nome em maiúsculas para exibição no título
            
            with open(type_filename, 'a', encoding='utf-8') as f:
                f.write(f"""
                <div class="card mb-3">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <a href='{sanitize_filename(pokemon.name)}.php'>
                                <img src="{pokemon_image_url}" class="img-fluid rounded-start" alt="{pokemon_name_upper}">
                            </a>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">{pokemon_name}</h5>  <!-- Nome original do Pokémon -->
                                <p class="card-text">{type_html}</p>
                            </div>
                        </div>
                    </div>
                </div>
                """)
                print(f"Adicionando {pokemon_name} ao catálogo do tipo {translated_type}")
    
    except Exception as e:
        print(f"Erro ao atualizar o catálogo para o tipo {type_}: {str(e)}")

# Função para obter e processar todos os Pokémon da região de Sinnoh (Geração 4)
def process_sinnoh_pokemons():
    sinnoh_pokemon_list = []
    
    for dex in range(387, 494):  # Geração 4 vai do dex 387 ao 493
        try:
            pokemon = pypokedex.get(dex=dex)
            sinnoh_pokemon_list.append(pokemon)
            
            create_pokemon_php(pokemon)
            update_type_catalog(pokemon)
        
        except Exception as e:
            print(f"Erro ao processar o Pokémon de dex {dex}: {str(e)}")
            continue  # Continuar para o próximo Pokémon

    print("Processamento concluído para todos os Pokémon da região de Sinnoh.")

# Chamada da função principal
process_sinnoh_pokemons()