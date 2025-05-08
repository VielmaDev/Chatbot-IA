<caption>
    <div class="container" style="text-aling:center";>
        <h1>Chatbot GABY v-1.0</h1>
    </div>
</caption>

<section>
<div class="container">
    <p>El chatbot Gaby v-1.0 se conecta con la API de Gemini AI en su versión 2.0 flash, en tiempo real permite mantener un chat y hacer preguntas.</p>
    <p>Cuenta con un selector de módulo para seleccionar la AI con la que se quiere interactuar, una casilla donde poder escribir el chat, así como, un contenedor para ver las 
        respuesta de la AI. </p>
</div>

<div class="container">
    <h4>lenguage and framework:</4>
    <ol>Python</ol>
    <ol>Flet</ol>
</div>
    
<div class="container">
    <h4>Virtual environment:</4>
    <li>pip install virtualenv</li>
</div>

<div class="container">
    <h4>virtual environment activation:</4>
    <p>\venv\Scripts\activate</p>
</div>
        
<div class="container">
    <h4>Library:</4>
    <li>pip install flet</li>
    <li>pip instalar google-generativeai</li>
    <li>pip instalar python-dotenv</li>
</div>

<div class="container">
    <h4>URL:</4>
    <ol>"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"</ol>
</div>
</section>

<div class="container">
    <h4>Note:</4>
    <ol>Para interactuar con Gemini AI, se debe registrar y solicitar una API_KEY en:</ol>
        <ol>https://ai.google.dev/aistudio?hl=es-419</ol>
</div>

<footer>
<div class="container my-2">
    <h4>Technical aspects:</h4>
</div>

<div class="container my-2">
    <ol>Arrancar el servidor ingresando a la terminal de VSCode y colocar el comando:</ol> 
        <li>python gemini.py</li>
</div>
</footer>
