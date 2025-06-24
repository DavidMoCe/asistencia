# 🚨 AsistAI - Asistente de Emergencia

AsistAI es una aplicación inteligente desarrollada con **Streamlit** que actúa como un asistente experto en situaciones de emergencia. Utiliza modelos de lenguaje grandes (LLMs) y vectores de documentos para responder preguntas basadas en información contenida en archivos PDF cargados por el usuario.

---

## 🧠 Características

- 🔍 Respuestas precisas basadas en documentos PDF cargados localmente.
- 💬 Interfaz tipo chat desarrollada con Streamlit.
- 🤖 Uso de modelos LLM y embeddings a través de DeepInfra.
- 📚 Indexación de documentos mediante `llama-index` (VectorStore).
- 🔐 Carga segura de claves API desde `.env` o `secrets` en Streamlit Cloud.

---

## 📁 Estructura del proyecto

asistencia-main/
│
├── app.py # Aplicación principal de Streamlit
├── docs/ # Carpeta donde se colocan los documentos PDF
├── .env # Archivo con variables de entorno (token DeepInfra)
├── vector_index.pkl # Archivo generado con el índice vectorial
└── requirements.txt # Dependencias necesarias


---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/asistencia-main.git
cd asistencia-main
```

### 2. Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🔑 Configuración
### 1. Variables de entorno
Crea un archivo .env en el directorio raíz con el siguiente contenido:
```env
DEEPINFRA_TOKEN=tu_clave_api_deepinfra
```

## 🚀 Ejecución
```bash
streamlit run app.py
```
La app se abrirá automáticamente en tu navegador predeterminado.

## 📌 Uso
1. Coloca tus documentos PDF en la carpeta docs/.

2. Inicia la app y escribe tus preguntas relacionadas con emergencias.

3. El asistente responderá solo con base en los documentos disponibles.

## 🧰 Tecnologías usadas
- [Streamlit](https://streamlit.io)
- [llama-index](https://www.llamaindex.ai)
- [DeepInfra](https://deepinfra.com) para LLMs y embeddings
- [pypdf](https://pypi.org/project/pypdf) para leer PDFs
- [dotenv](https://pypi.org/project/python-dotenv) para gestionar claves

## 📜 Licencia
Este proyecto está licenciado bajo la licencia **CC BY-NC 4.0**. Consulta el archivo [`LICENSE`](#) para más detalles.

## ❤️ Créditos
Desarrollado por **David Moreno Cerezo**
