import streamlit as st
from openai import OpenAI

# Configuración inicial de la app
st.set_page_config(page_title="Vet GPT", page_icon="🐾")
st.title("🩺 Vet GPT 🐶🐱")
st.markdown("Consultas orientativas para colegas. **Especializado en perros y gatos.**")

# Campo de entrada del usuario
prompt = st.text_area("✍️ Describí el caso clínico:")

# Configuración del cliente OpenAI. Clave API desde configuración de Streamlit Cloud
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Lógica al presionar el botón
if st.button("Consultar") and prompt:

    # Instrucciones al modelo GPT
    instrucciones = """
Actuás como un clínico veterinario especializado en perros y gatos.
Recibís descripciones clínicas e historial de signos clínicos.
Respondés en español con:
- Diagnóstico presuntivo
- Diagnóstico diferencial (mínimo 2 posibles)
- Indicás pasos diagnósticos complementarios
- Recomendaciones clínicas generales
- Indicás tratamiento específico para el diagnóstico presuntivo
- Indicás principios activos o grupos farmacológicos, según el diagnóstico presuntivo.
Siempre recordás que es imprescindible la evaluación presencial.
"""

    # Solicitud a la API de OpenAI
    respuesta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": prompt}
        ]
    )

    # Mostrar la respuesta generada
    st.markdown("### 🧾 Respuesta de Vet GPT:")
    st.write(respuesta.choices[0].message.content)
