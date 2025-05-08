<caption>
    <div class="container" style="text-aling:center";>
        <h1>Chatbot GABY v-1.0</h1>
    </div>
</caption>

<section>
<div class="container">
    <p>El chatbot Gaby v-1.0 se conecta con la API de Gemini AI en su versión 2.0 flash (versión Gratuita), y en tiempo real permite mantener un chat.</p>
    <p>Cuenta con un selector de módulo para seleccionar la AI con la que se quiere interactuar, una casilla donde poder escribir el chat, así como, un contenedor para ver las 
        respuesta de la AI. </p>
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
    <h4>URL</4>
    <p>"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"</p>
</div>
</section>

<div class="container">
    <h4>Note:</4>
    <p>Para interactuar con Gemini AI, se debe registrar y solicitar una API_KEY en:</p>
        <a>https://ai.google.dev/aistudio?hl=es-419</a>
</div>

<footer>
<div class="container my-2">
    <h4>Technical aspects:</h4>
</div>

<div class="container my-2">
    <li>Arrancar el servidor, ingresando a la terminal de VSCode y colocar el comando:</li> 
        <p>python gemini.py</p>
</div>
</footer>
