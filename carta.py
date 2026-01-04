import streamlit as st

from PIL import Image

import os

import base64



# Configuración de la página

st.set_page_config(page_title="Para Ana María", page_icon="❤️", layout="centered")



# --- FUNCIÓN PARA LA IMAGEN (Solución definitiva) ---

def get_image_base64(path):

    if os.path.exists(path):

        with open(path, "rb") as img_file:

            return base64.b64encode(img_file.read()).decode()

    return None



# --- ESTILOS CSS REFORZADOS ---

st.markdown("""

    <style>

    .main { background-color: #fff5f5; }

    

    /* Título en ROSADO */

    .titulo-rosado {

        color: #d63384 !important;

        font-family: 'Georgia', serif;

        text-align: center;

        font-size: 35px;

        font-weight: bold;

    }



    /* FORZAR TODO EL TEXTO A NEGRO (Cuerpo y Expander) */

    .stMarkdown, p, span, li, label, .st-emotion-cache-pgh4id {

        color: white !important;

    }



    /* CARTA: NEGRO Y JUSTIFICADO TOTAL */

    .carta-box { 

        font-family: 'Verdana', sans-serif; 

        color: white !important;

        line-height: 1.8; 

        text-align: justify !important; /* Justificación forzada */

        background: white;

        padding: 25px;

        border-radius: 15px;

        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);

    }



    /* BOTÓN: FONDO ROSADO Y LETRA BLANCA */

    div.stButton > button {

        background-color: #d63384 !important;

        color: #FFFFFF !important; /* Blanco puro */

        border-radius: 20px;

        width: 100%;

        border: none;

        height: 3em;

        font-size: 18px;

        font-weight: bold;

    }

    

    /* Ajuste para el texto dentro del expander */

    .stDetails p {

        text-align: justify !important;

        color: white !important;

    }



    .footer { 

        text-align: right; 

        font-style: italic; 

        color: white !important; 

        margin-top: 20px; 

    }

    

    /* NUEVA REGLA PARA EL RECUADRO NEGRO */

    [data-testid="stToast"] {

        background-color: #111111 !important; /* Fondo oscuro */

        color: white !important; /* LETRA BLANCA */

    }

    [data-testid="stToast"] p {

        color: white !important;

    }

    </style>

    """, unsafe_allow_html=True)



# --- CONTENIDO ---



st.markdown('<p style="text-align: center; color: #000000;">💌 Un mensaje especial</p>', unsafe_allow_html=True)

st.markdown('<h1 class="titulo-rosado">Para Ana María</h1>', unsafe_allow_html=True)



# Lógica de la imagen mejorada

img_path = "pareja.jpg"

img_b64 = get_image_base64(img_path)



if img_b64:

    st.markdown(f'<img src="data:image/jpg;base64,{img_b64}" style="width:100%; border-radius:15px; margin-bottom:20px;">', unsafe_allow_html=True)

else:

    st.warning("📸 Coloca la foto 'image_2bf8a6.jpg' en la misma carpeta para que aparezca aquí.")







with st.expander("📖 Haz clic para leer sobre nuestro año"):

    st.markdown("""

    <div style="color: black; text-align: justify;">

    Debido al honor que se me ha concedido dirigirme a tan ilustre persona, por el presente, deseo expresar mis más sinceras palabras. Ya mucha cosa mejor escribo normal. <br><br>

    Para empezar no sé por qué se te ocurrió pero ya, no tengo otra opción. No tengo ni la más mínima idea de qué contenido debe tener lo que vaya a escribir, pero ya pensaré en algo coherente. Habiendo ya consultado sobre lo que debe contener el texto, ya tengo una idea más clara. Empezaré.

    Si tiene que ser del año vivido tendré que empezar por el primer mes supongo. En fin, qué pasó. Ah sí, tu cumpleaños. Qué hice. Si mal no recuerdo algo te di con tal de que no tengas nada de mi parte y ya nada más con tal que te haya gustado. Luego mes de transición creo no recuerdo muchas cosas relevantes. Ahh, el campeonato. Bueno eso no tiene que ver mucho contigo. Continúo, marzo. Entre tantas cosas pues lo más importante fue que cumplíamos un año de estar juntos. No hicimos nada especial como tal en esa oportunidad, pero ya será para este año. Siendo sincero no es que lo haya sentido como un logro, pero lo considero como algo importante en nuestra historia juntos pues porque lo que mayormente ocurre primero es lo que más se celebra y recuerda no?. Ya bueno eso. Lo siguiente, abril. Qué hubo. Aparte de la pascua creo que no muchas cosas. Pues lo más resaltante que queda es el intento de tener fotos juntos y la forma en que según tú siempre la mayoría salen mal. Pero bueno qué se le va hacer. Next, mayo. Siempre empieza con mi cumpleaños y pues es un día más. Al menos te tomaste el tiempo de pasar un momento conmigo y eso es lo que valoro. Luego, junio y julio creo que algo aparte de vernos y conversar algunos fines de semana pues no creo. Más meses de transición. Ah creo que en esos meses fue eso de que me pediste acompañarte a buscar un álbum y que para colmo no había, sumado a eso la lluvia y el intento fallido de entrar al parque de las aguas. En fin, si me dio rabia no lograr eso, ya será para otra fecha. Continuando el siguiente mes, pues ya andaba trabajando, porquería de trabajo también pero ya ps. De ese mes recuerdo que fuimos al cine a ver esa película de Lindsey Lohan, a mi me agradó y pues concluyó comiendo esas cosas que ni me gustaron. Lo que siguió fue septiembre que la verdad creo que nos vimos una sola vez en el mes y los siguientes meses también fueron así. Entre tanto que demandaba la universidad sumado a los intentos fallidos que se daban pues, me preocupé poco por mantener una frecuencia menos larga para compartir juntos. Y se notaba también porque era algo que empezaste a mencionar cada vez que nos despedíamos, pero ya pasó al menos. Me salto a diciembre mejor. El último mes pues ya en sí estaba casi todo resuelto por parte de la universidad y en lo que se trata de los dos pues empezaste con tener una foto antes de que acabase el año porque la anterior no te bastaba y tuve que pasarte la que había de mi cumpleaños para que al menos no digas nada. Aún así también pensé en darte el gusto y pues de tantos intentos en el parque, imagino que algunas salieron bien y pues con eso pudiste quedarte contenta. Ya de ahí pues fue más de conversaciones y de alguna forma fortalecer la relación. Y así se fue acabando el año.

    Para hacer un sumario y así cerrar la idea de la carta, como te he mencionado en algunas ocasiones el hecho de estar contigo en una relación me ha hecho ver unas cuantas cosas que aún tengo que mejorar. Durante el año que pasó, contigo me he sentido agradecido y sobre todo de alguna forma aceptado.También ya te he mencionado las cosas que me gustan de ti y de por qué estoy enamorado y sigo enamorándome de ti. Podrá ser muy repetitivo, pero nuevamente resalto tu paciencia e inteligencia.Espero que sigamos creciendo tanto de forma personal como en conjunto y que las cosas se den como Dios quiera. Listo me parece que ya terminé el texto. Te quiero.

    Dada en internet, el día cuarto del mes primero del año dos milésimo vigésimo sexto

    </div>

    """, unsafe_allow_html=True)



if st.button("Haz clic aquí ❤️"):

    st.balloons()

    st.toast("¡Te amo!", icon='😍')