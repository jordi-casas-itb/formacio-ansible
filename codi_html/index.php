<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Productes Dinàmics</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px 0;
        }
        .product-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .product-card {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .product-card h3 {
            color: #0056b3;
        }
        .product-card .price {
            font-weight: bold;
            color: #28a745;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <header style="background: #333; color: #fff; padding: 1rem 0; text-align: center;">
        <h1>Els Nostres Productes</h1>
    </header>

    <div class="container">
        <h2>Llista de Productes Obtinguts de la Base de Dades:</h2>
        <div class="product-list">
            <?php
            // Inclou el fitxer de configuració de la base de dades
            include 'db_config.php';

            // Consulta SQL per seleccionar tots els productes
            $sql = "SELECT id, nom, descripcio, preu FROM productes";
            $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                // Iterar sobre cada fila de resultats
                while($row = $result->fetch_assoc()) {
                    echo '<div class="product-card">';
                    echo '<h3>' . htmlspecialchars($row["nom"]) . '</h3>';
                    echo '<p>' . htmlspecialchars($row["descripcio"]) . '</p>';
                    echo '<p class="price">' . number_format($row["preu"], 2, ',', '.') . ' €</p>';
                    echo '</div>';
                }
            } else {
                echo '<p>No s\'han trobat productes.</p>';
            }

            // Tancar la connexió a la base de dades
            $conn->close();
            ?>
        </div>
    </div>

    <footer style="background: #333; color: #fff; text-align: center; padding: 1rem 0; margin-top: 30px;">
        <p>&copy; 2025 Productes Dinàmics. Tots els drets reservats.</p>
    </footer>
</body>
</html>
