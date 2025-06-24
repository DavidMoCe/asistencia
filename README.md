# 🚨 AsistAI - Emergency Assistant

## 🌍 Choose Your Language / Elige tu idioma:
- [English](#english-gb)
- [Español](#español-es)

---

## English GB

AsistAI is an intelligent application built with Streamlit that acts as an expert assistant in emergency situations. It uses large language models (LLMs) and document vectorization to answer questions based on information contained in user-uploaded PDF files.

---

## 🧠 Features
- 🔍 Accurate answers based on locally uploaded PDF documents.
- 💬 Chat-style interface built with Streamlit.
- 🤖 Uses LLMs and embedding models via DeepInfra.
- 📚 Document indexing powered by llama-index (VectorStore).
- 🔐 Secure API key loading from .env or secrets in Streamlit Cloud.

## 📁 Project Structure
```bash
asistencia-main/
│
├── app.py                 # Main Streamlit application
├── docs/                  # Folder for user-provided PDF documents
├── .env                   # Environment variables file (DeepInfra token)
├── vector_index.pkl       # Generated file for the document vector index
└── requirements.txt       # Required Python dependencies
```

## ⚙️ Installation
1. Clone the repository
```bash
git clone https://github.com/your_username/asistencia-main.git
cd asistencia-main
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Configuration
1. Environment variables
Create a .env file in the root directory with the following content:
```env
DEEPINFRA_TOKEN=your_deepinfra_api_key
```

## 🚀 Running the App
```bash
streamlit run app.py
```

The app will automatically open in your default browser.

## 📌 Usage
1. Place your PDF documents in the docs/ folder.
2. Start the app and type your emergency-related questions.
3. The assistant will respond based solely on the content of the available documents.

## 🧰 Technologies Used
- [Streamlit](https://streamlit.io)
- [llama-index](https://www.llamaindex.ai)
- [DeepInfra](https://deepinfra.com) for LLMs and embeddings
- [pypdf](https://pypi.org/project/pypdf) for PDF parsing
- [dotenv](https://pypi.org/project/python-dotenv) for managing API keys

## 📜 License
This project is licensed under the CC BY-NC 4.0 license. See the [`LICENSE`](https://github.com/DavidMoCe/asistencia/blob/main/LICENSE.txt) file for more details.

## ❤️ Credits
Developed by **David Moreno Cerezo**


---

## Español ES

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
```bash
asistencia-main/
│
├── app.py # Aplicación principal de Streamlit
├── docs/ # Carpeta donde se colocan los documentos PDF
├── .env # Archivo con variables de entorno (token DeepInfra)
├── vector_index.pkl # Archivo generado con el índice vectorial
└── requirements.txt # Dependencias necesarias
```

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
Este proyecto está licenciado bajo la licencia **CC BY-NC 4.0**. Consulta el archivo [`LICENSE`](https://github.com/DavidMoCe/asistencia/blob/main/LICENSE.txt) para más detalles.

## ❤️ Créditos
Desarrollado por **David Moreno Cerezo**
