
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>GLACEON - Pokédex</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body {
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }
                .badge {
                    font-size: 14px;
                    padding: 8px 12px;
                    margin: 2px;
                    border-radius: 12px;
                }
                .container {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                .card {
                    border: none;
                    border-radius: 12px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }
                .img-fluid {
                    max-width: 100%;
                    height: auto;
                }
                .card-body {
                    padding: 15px;
                }
            </style>
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center mb-4">GLACEON</h1>
                <div class="row justify-content-center">
                    <div class="col-md-4">
                        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/471.png" class="img-fluid rounded-start" alt="GLACEON">
                    </div>
                    <div class="col-md-8">
                        <div class="card mb-3">
                            <div class="row g-0">
                                <div class="col-md-12">
                                    <div class="card-body">
                                        <h5 class="card-title">glaceon</h5>  <!-- Nome original do Pokémon -->
                                        <p class="card-text">
                                            <strong>Tipos:</strong> <span class="badge" style="background-color: #A8A878; color: white;">Gelo</span>
                                        </p>
                                        <p class="card-text">
                                            <strong>Estatísticas:</strong> HP: 65, Ataque: 60, Defesa: 110, Sp. Ataque: 130, Sp. Defesa: 95, Velocidade: 65
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-3">
                    <!-- Modificando o link para direcionar para a página do tipo -->
                    <a href="gelo.php" class="btn btn-primary">Voltar para o tipo</a>
                </div>
            </div>
        </body>
        </html>
        