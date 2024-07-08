import streamlit as st
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

##########################################################
genai.configure(api_key=GOOGLE_API_KEY)

contexto = (
    "Eres un especialista en medio ambiente basado en las leyes vigentes de Argentina. "
    "Un usuario realizará consultas sobre cuidados del medioambiente. "
    "Responde de forma amable a sus preguntas con información precisa, clara y adaptada a su contexto, considerando siempre las normativas legales y recomendaciones actuales en Argentina."
    "Ley General del Ambiente (Ley 25.675) que establece los presupuestos mínimos para la protección ambiental."
    "Ley de Bosques (Ley 26.331) que reglamenta la protección de los bosques nativos."
    "Ley de Residuos Peligrosos (Ley 24.051) Normativa para la gestión de residuos peligrosos y su tratamiento adecuado."
    "Ley de Energías Renovables (Ley 27.191) Promoción de energías renovables en la matriz energética nacional."
)

model = genai.GenerativeModel('gemini-1.0-pro')
  
def consultaGemini(contexto, consulta, edad, sexo, metodo):
#  prompt = " Quien consulta es una persona de " + str(edad) + " años de edad, de sexo " + sexo + ", que utiliza como método de reciclado " + metodo + " y su consulta es la siguiente: " + consulta
  persona = f" Tengo " + str(edad) + " años de edad, de sexo " + sexo + " y " + metodo
  prompt = persona + consulta
  respuestaIA = model.generate_content(contexto + prompt)
  return respuestaIA.text
    

################################################################################################
# Título de la aplicación
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/2560px-Google_Gemini_logo.svg.png", width=200)
st.header('ECOconcienc(IA)', divider='rainbow')
st.subheader("Un espacio para asesorarte sobre medio ambiente.")
st.write("por Javier Bergaglio")

# Crear solapas
tabs = st.tabs(["Presentación", "Cómo funciona?", "Tu consulta"])

# Solapa de Presentación
with tabs[0]:
    st.header("Presentación")
    st.markdown("""
    Bienvenido a ***ECOconcienc(IA)***. Esta aplicación está diseñada para proporcionar información sobre cuidados del medio ambiente basada en las leyes vigentes de Argentina.  
    La aplicación te responderá con información precisa y clara, adaptada a tu contexto y necesidades.  
                
    """)
    st.divider()
    st.markdown(""" ⚠️ ***Mensaje para el profe***  
               Inicialmente el proyecto trataba de mensajes sobre anticoncepción en adolescencias (adolescencIA) pero decidi cambiar la temática debido a que no logré evitar bloqueos de la API por la temática. :blue[Mantengo la funcionalidad explicada para el proyecto inicial pero cambiando por una temática donde no recibo bloqueos de la API.]""")
    st.divider()

# Solapa Como funciona
with tabs[1]:
    st.header("Cómo funciona?")

    st.markdown("""
    La aplicación te solicitara ***unos pocos datos personales*** con el fin de conocerte un poco más y podeere bridarte una mejor respuesta.  Los datos que te solicitaremos son:  
    • tu edad,  
    • sexo  
    • y si realizás algún tipo de reciclado.  
    
    Con estos datos, podrás realizar tu consulta y ***recibirás una respuesta de un agente de IA especializado en medio ambiente basado en la normativa argentina vigente***.
    """)

# Solapa de Consulta
with tabs[2]:
    st.header("Consulta")

    # Formulario de entrada de datos del usuario
    edad = st.number_input("Edad:", min_value=13, max_value=100, step=1)
    sexo = st.radio("Sexo:", ("Masculino", "Femenino", "No binario", "Otro"))
    metodo = st.selectbox("¿Utilizás algún método de reciclado actualmente?", ("No utilizo método de reciclado actualmente", "Separo plásticos y cartón como método de reciclado actualmente", "Separo plásticos y cartón y además realizo compost con los orgánicos como método de reciclado actualmente", "No conozco sobre métodos de reciclado"))

    # Espacio de preguntas del usuario
    st.write("Puedes hacer tus consultas sobre cuidado del medio ambiente a continuación. Te ofrecemos absoluta confidencialidad y solo trataremos tu información con el fin de poder asesorarte de la mejor manera posible.")

    consulta = st.text_area("Ingresa tu consulta:")

    # Botón para enviar la consulta
    if st.button("Consultar"):
        if consulta:
            respuesta = consultaGemini(contexto, consulta, edad, sexo, metodo)
            st.markdown("***Respuesta del especialista:***")
            st.write(respuesta)
        else:
            st.write("Por favor, ingresa una consulta.")        
