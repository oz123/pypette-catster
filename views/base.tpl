<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cat Gallery</title>
    <!-- Fomantic UI CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.css">
    <style>
        body {
            padding: 20px;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .image-container img {
            max-width: 100%;
            max-height: 70vh;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .navigation {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="ui container">
        <h1 class="ui center aligned header">Cat Gallery</h1>
        {% include image.tpl %}
    </div>
    
    <!-- Fomantic UI JS -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.js"></script>
</body>
</html>
