import flet
from flet import Page, TextField, ElevatedButton, Column, Text, Container, alignment, Dropdown, dropdown, Colors
import google.generativeai as genai
from dotenv import load_dotenv
import os
 
load_dotenv()

genai.configure(api_key=os.getenv( "GOOGLE_API_KEY" )) 

#Respuesta de Gemini AI 
def get_gemini_response(prompt):
    """Obtener respuesta de Gemini-2.0-flash"""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content([prompt])
        return response.text
    except Exception as e:
        return f"Error al consultar Gemini AI: {str(e)}"


#Interfaz Gráfica 
def main(page: Page):
    page.title = "Chatbot GABY v-1.0"
    page.bgcolor = Colors.BLUE_GREY_900
    page.theme_mode = "dark"

    input_box = TextField(
        label="Escribe tu chat",
        border_color=Colors.BLUE_400,
        focused_border_color=Colors.BLUE_400,
        text_style=flet.TextStyle(color=Colors.YELLOW),
        expand=True
    )

    #Opciones de chat
    mode_dropdown = Dropdown(
        options=[
            dropdown.Option("chat", "Gemini 2.0 flash"),
        ],
            value="chat",
        label="Módulo",
        border_color=Colors.BLUE_400,
        color=Colors.WHITE
    )
    
    chat_area = Column(scroll='auto', expand=True)
    
    def send_message(e):
        user_message = input_box.value
        if not user_message:
            return
        
        # Mortrar mensaje del usuario
        chat_area.controls.append(Text(f"Usuario: {user_message}"))

        # Prosesar según em modo seleccionado
        if mode_dropdown.value == "chat":
            response = get_gemini_response(user_message)

        # Mostrar respuesta
        chat_area.controls.append(Text(f"Chatbot: {response}"))

        # Limpiar input y actualizar UI
        input_box.value = ""
        page.update()


    #Boton enviar
    send_button = ElevatedButton(
        text="Enviar",
        on_click=send_message,
        bgcolor=Colors.BLUE_700,
        color=Colors.WHITE
    )

    #Contenedor del chat
    chat_container = Container(
        content=chat_area,
        bgcolor=Colors.BLUE_GREY_800,
        padding=10,
        border_radius=10,
        expand=True
    )

    input_container = Container(
        content=flet.Row(
            controls=[
                mode_dropdown,
                input_box,
                send_button
            ],
            spacing=10
        )
    )

    page.add(
        chat_container,
        input_container
    )

    page.window_width = 600
    page.window_height = 400
    page.update()

if __name__ == "__main__":
    flet.app(target=main)





