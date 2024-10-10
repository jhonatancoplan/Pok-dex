<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <style type="text/css">

        </style>
    </head>
    <body>
        
        <form method="POST">
            imagem do Pokémon: <input type="file" name="imagem do Pokémon" required><br>
            nome do Pokémon: <input type="text" name="nome do Pokémon" required><br>

            <div class="input-group mb-3">
                tipo 1
                <select name="tipo 1" required>
                    <option value="0">escolha</option>
                    <option value="2">Grama</option>
                    <option value="3">Escuro</option>
                    <option value="4">Elétrico</option>
                    <option value="5">Inseto</option>
                    <option value="6">Voador</option>
                    <option value="7">Gelo</option>
                    <option value="8">Fogo</option>
                    <option value="9">Água</option>
                    <option value="10">Veneno</option>
                    <option value="11">Rocha</option>
                    <option value="12">Dragão</option>
                    <option value="13">Fada</option>
                    <option value="14">Fantasma</option>
                    <option value="15">Psíquico</option>
                    <option value="16">Aço</option>
                    <option value="17">Chão</option>
                    <option value="18">Lutando</option>
                </select>
 
                tipo 2
                <select name="tipo 2" required>
                    <option value="0">escolha</option>
                    <option value="1">Normal</option>
                    <option value="2">Grama</option>
                    <option value="3">Escuro</option>
                    <option value="4">Elétrico</option>
                    <option value="5">Inseto</option>
                    <option value="6">Voador</option>
                    <option value="7">Gelo</option>
                    <option value="8">Fogo</option>
                    <option value="9">Água</option>
                    <option value="10">Veneno</option>
                    <option value="11">Rocha</option>
                    <option value="12">Dragão</option>
                    <option value="13">Fada</option>
                    <option value="14">Fantasma</option>
                    <option value="15">Psíquico</option>
                    <option value="16">Aço</option>
                    <option value="17">Chão</option>
                    <option value="18">Lutando</option>
                </select>

            </div>

            descrição do pokémon: <input type="text" name="descrição do pokémon" required><br>
            <input type="submit" value="Enviar">
            </form>
        </div>

        <?php



        
        echo"<img src=''";

        ?>


        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    </body>
</html>