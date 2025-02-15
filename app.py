import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.deepinfra import DeepInfraEmbeddingModel
from llama_index.llms.deepinfra import DeepInfraLLM

# Configuración de la aplicación Streamlit (Mover a la parte superior)
st.set_page_config(page_title="Asistente de Emergencia", page_icon="🚨", layout="centered")

# Configuración de DeepInfra API
# Cargar variables de entorno desde .env
load_dotenv()
deepinfra_api_key = os.getenv("DEEPINFRA_TOKEN")

if not deepinfra_api_key:
    # Cargar la API Key de DeepInfra desde las secrets de Streamlit Cloud
    deepinfra_api_key = st.secrets["DEEPINFRA_TOKEN"]
    
    if not deepinfra_api_key:
        st.error("Falta la API Key de DeepInfra. Configúrala en un archivo .env o en el apartado secrets de stramlit cloud")
    

# Definir el modelo de embeddings y LLM de DeepInfra
# Configurar el modelo de embeddings con el nuevo modelo BGAI/bge-m3
Settings.embed_model = DeepInfraEmbeddingModel(
    model_id="BAAI/bge-m3",  # ID del modelo de embeddings de DeepInfra
    api_token=deepinfra_api_key,  # Token de la API
    normalize=True,  # Normalización opcional
    text_prefix="text: ",  # Prefijo de texto
    query_prefix="query: ",  # Prefijo de consulta
)

Settings.chunk_size = 512

# Crear el modelo de embeddings
embedding_model = Settings.embed_model

# Configuración centralizada del modelo LLM utilizando Settings
Settings.llm = DeepInfraLLM(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Modelo de DeepInfra
    api_key=deepinfra_api_key,  # Tu clave API de DeepInfra
    temperature=0,  # Configuración de temperatura para control de creatividad
)

# Función para cargar y guardar el índice y el modelo de embeddings
@st.cache_resource
def load_index():    
    docs_folder = "docs"  # Asegúrate de que tus documentos estén en esta carpeta
    documents = SimpleDirectoryReader(docs_folder).load_data()
    
    # Usar DeepInfraEmbeddingModel para el índice
    index = VectorStoreIndex.from_documents(documents, embed_model=embedding_model)
    return index.as_query_engine()

# Cargar el índice y el modelo de embeddings
query_engine = load_index()

# Configuración de la conversación
promt = "Eres un asistente experto en emergencias llamado AsistAI. Responde únicamente preguntas relacionadas con la información en los documentos proporcionados. Si la pregunta no está cubierta, indica que no puedes responder. Si es necesario, complementa con información de internet, pero solo si está estrictamente relacionada con los documentos. No incluyas información no verificada ni hagas referencia a los documentos. Da respuestas claras, precisas y directas, sin explicaciones innecesarias. Intenta dar siempre la solución al problema planteado con una respuesta concisa."

# opcion 2
#promt = "Eres un asistente experto en emergencias. Solo puedes responder preguntas relacionadas con la información contenida en los documentos proporcionados. Si la consulta no está dentro de estos temas, responde educadamente que no puedes ayudar.Si la respuesta requiere información adicional para ser más precisa o actualizada, puedes buscar en internet, pero solo si está estrictamente relacionada con los temas cubiertos en los documentos. No generes respuestas con información no verificada o fuera de contexto.Responde de manera clara, precisa y útil, sin hacer referencia explícita a los documentos en tus respuestas."

# Saludo
saludo = "👋 ¡Hola! Soy **AsistAI**, tu asistente en situaciones de emergencia. Estoy aquí para ayudarte a resolver cualquier urgencia o aprender qué hacer en momentos críticos. ¿En qué puedo ayudarte?"

# Inicializar historial de conversación en la sesión de Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": promt},
        {"role": "assistant", "content": saludo}
    ]

# Inicializar el estado de la sesión
if "processing" not in st.session_state:
    st.session_state.processing = False  # Variable de bloqueo para evitar múltiples consultas simultáneas

# Configuración de la aplicación
st.title("🚨 Asistente de Emergencia")
st.write("Pregunta sobre emergencias y obtén respuestas basadas en documentos.")

# Sidebar de la aplicación
with st.sidebar:
    # Botón "Nuevo chat" para reiniciar la conversación
    if st.button("Nuevo chat"):
        st.session_state.messages = [
            {"role": "system", "content": promt},
            {"role": "assistant", "content": saludo}
        ]
        st.session_state.processing = False
    
    # Información sobre la aplicación
    st.markdown("---")
    st.markdown("### Descripción")
    st.write("Este amable asistente de emergencia proporciona respuestas a preguntas basadas en documentos.")
    st.write("Hecho con ❤️ por los estudiantes de **Accenture**")
    st.markdown("---")

# Mostrar historial de chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user", avatar="🧑‍💼").write(f"{msg['content']}")
    elif msg["role"] == "assistant":
        st.chat_message("assistant", avatar="🤖").write(f"{msg['content']}")
    
# Entrada del usuario
if user_query := st.chat_input("Escribe tu pregunta...", disabled=st.session_state.processing, key="user_input"):
    st.session_state.processing = True  # Bloquear entrada de usuario durante la consulta
    
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user", avatar="🧑‍💼").write(f"{user_query}")
    
    st.rerun()  # Recargar la interfaz para reflejar el cambio
    
    # Procesar respuesta en una iteración separada después de que la UI ya se haya actualizado
if st.session_state.processing and len(st.session_state.messages) > 1 and st.session_state.messages[-1]["role"] == "user":
    with st.spinner("Buscando respuesta..."):
        # Crear un contexto con todas las preguntas y respuestas previas
        conversation_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages]
        )
    
        # Incluir el historial en la consulta
        response = query_engine.query(f"Historial de conversación:\n{conversation_history}\n\nNueva pregunta: {user_query}")

        # Agregar la respuesta del motor de búsqueda al historial de mensajes
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Mostrar respuesta en el chat
        #st.chat_message("assistant").write(response)
        st.chat_message("assistant", avatar="🤖").write(response.response)
        
        st.session_state.processing = False  # Desbloquear entrada de usuario después de la consulta
        st.rerun()  # Recargar la interfaz para reflejar el cambio