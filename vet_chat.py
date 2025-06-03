import openai
import streamlit as st

# Clave API desde configuración de Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="GPT Veterinario", layout="centered")

st.title("M.V. GPT 🐶🐱")
st.write("Consultá casos clínicos de perros y gatos ingresando signos clínicos.")

# Campo de entrada
prompt = st.text_area("✍️ Describí el caso clínico:", height=200)

# Botón de consulta
if st.button("Consultar"):
    instrucciones = """
    Actuás como un clínico veterinario especializado en perros y gatos.
    Recibís descripciones clínicas e historial de signos o síntomas.
    Respondés en español con:
    - Diagnóstico presuntivo
    - Diagnóstico diferencial (mínimo 2 posibles)
    - Indicaciones de pasos diagnósticos complementarios
    - Recomendaciones clínicas generales y específicas para el diagnóstico presuntivo
    Indicás principios activos o grupos farmacológicos orientativos, según el diagnóstico presuntivo.
    """

    respuesta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": prompt}
        ]
    )

    # Mostrar la respuesta
    st.markdown("### 🧾 Respuesta del M.V. GPT:")
    st.write(respuesta['choices'][0]['message']['content'])
