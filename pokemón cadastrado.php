<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <title>Lista de Pokémons</title>
    </head>
    <body>

        <header>
                <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">Pokédex</a>
                    <div class="collapse navbar-collapse">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Pok-dex-master/Pok%c3%a9dex.php">Início</a></li>
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Pok-dex-master/Tipos%20de%20Pokemon.php">Pokémons por Tipos</a></li>
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Pok-dex-master/Cadastro%20de%20pokem%c3%b3n.php">Cadastrar Pokémon</a></li>
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Pok-dex-master/pokem%c3%b3n%20cadastrado.php">Pokémon Cadastrar</a></li>
                            <li class="nav-item"><a class="nav-link" href="http://localhost/Pok-dex-master/Treinador.php">Treinador</a></li>
                        </ul>
                        
                    </div>
                </nav>
            </header>

        <?php
        $link = mysqli_connect("localhost", "root", "", "pokede");

        if (!$link) {
            die("Erro na conexão: " . mysqli_connect_error());
        }

        $sql = "SELECT nome, tipo, imagen FROM pokemon";
        $result = $link->query($sql);

        if ($result->num_rows > 0) {

            echo '<div class="container mt-5">';
            echo '<div class="row">';


            while($row = $result->fetch_assoc()) {
                echo '<div class="col-sm-6 col-md-4 mb-4">';
                    echo '<div class="card">';
                        echo '<img class="card-img-top" src="' . $row["imagen"] . '" alt="Imagem de capa do card">';
                        echo '<div class="card-body">';
                            echo '<h5 class="card-title">' . $row["nome"] . '</h5>';
                            echo '<p class="card-text"><strong>Tipo:</strong> ' . $row["tipo"] . '</p>';
                        echo '</div>';
                    echo '</div>';
                echo '</div>';
            }


            echo '</div>';
            echo '</div>';
        } else {
            echo "Nenhum Pokémon encontrado.";
        }

        mysqli_close($link);
        ?>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
    </body>
</html>