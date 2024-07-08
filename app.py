import streamlit as st
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

##########################################################
genai.configure(api_key=GOOGLE_API_KEY)

contexto = (
    "Eres un especialista en medio ambiente basado en las leyes vigentes de Argentina. "
    "Un usuario realizará consultas sobre cuidados del medioambiente. "
    "Responde de forma amable a sus preguntas con información precisa, clara y adaptada a su contexto, considerando siempre las normativas legales y recomendaciones actuales en Argentina."
)

model = genai.GenerativeModel('gemini-1.0-pro')
  
def show_alert(message, alert_type="primary"):
    html_alert = f"""
    <div class="alert alert-{alert_type}" role="alert">
        {message}
    </div>
    """
    return st.markdown(html_alert, unsafe_allow_html=True)

def consultaGemini(contexto, consulta, edad, sexo, metodo):
#  prompt = " Quien consulta es una persona de " + str(edad) + " años de edad, de sexo " + sexo + ", que utiliza como método de reciclado " + metodo + " y su consulta es la siguiente: " + consulta
  persona = f" Tengo " + str(edad) + " años de edad, de sexo " + sexo + " y " + metodo
  prompt = persona + consulta
  respuestaIA = model.generate_content(contexto + prompt)
  return respuestaIA.text
    

################################################################################################
# Título de la aplicación
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/2560px-Google_Gemini_logo.svg.png", width=200)
st.header('concienc(IA)', divider='rainbow')
st.subheader("Un espacio para asesorarte sobre medio ambiente.")
st.write("por Javier Bergaglio")

# Crear solapas
tabs = st.tabs(["Presentación", "Consulta"])

# Solapa de Presentación
with tabs[0]:
    st.header("Presentación")
    st.write("""
    Bienvenido a concienc(IA). Esta aplicación está diseñada para proporcionar información sobre cuidados del medio ambiente basada en las leyes vigentes de Argentina.  
    Brindanos algunos datos básicos y podrás realizar tus consultas.  
    La aplicación te responderá con información precisa y clara, adaptada a tu contexto y necesidades.  
                
    """)
    st.divider()
    st.markdown(""" ⚠️ ***Mensaje para el profe***  
               Inicialmente el proyecto trataba de mensajes sobre anticoncepción en adolescencias (adolescencIA) pero decidi cambiar la temática debido a que no logré evitar bloqueos de la API por la temática. :blue[Mantengo la funcionalidad explicada para el proyecto inicial pero cambiando por una temática donde no recibo bloqueos de la API.]""")
    st.divider()

# Solapa de Consulta
with tabs[1]:
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
