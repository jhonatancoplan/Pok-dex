import pypokedex

# Obter os dados do Pokémon
pokemon = pypokedex.get(dex= 50)

teste_1 =  ""
teste_2 =  ""

# Criar ou abrir o arquivo HTML em modo de append   
with open("oi.html", "a") as f:
    # Adicionar uma estrutura básica de HTML
    f.write("<html>\n")
    f.write("<head><title>Pokémon</title></head>\n")
    f.write("<body>\n")
    
    # Escrever os detalhes do Pokémon
    f.write(f"<h1>{pokemon.name}</h1>\n")
    f.write(f"<p><strong>Types:</strong> {', '.join(pokemon.types)}</p>\n")
    f.write(f"<p><strong>Base Stats:</strong> {pokemon.base_stats}</p>\n")
    f.write(f"<p><strong>Sprites:</strong></p>\n")
    f.write(f"<img src='{teste_1}' alt='{pokemon.name} sprite' />\n" pip install pypokedex)
    
    f.write("</body>\n")
    f.write("</html>\n")

# Ler e imprimir o conteúdo do arquivo HTML
with open("oi.html", "r") as f:
    print(f.read())