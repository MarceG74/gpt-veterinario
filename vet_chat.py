import streamlit as st
import openai

# Configuración de la API de OpenRouter
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.base_url = "https://openrouter.ai/api/v1"

# Configuración de la página
st.set_page_config(page_title="VetChat - Diagnóstico Veterinario")
st.title("🐾 VetChat para Veterinarios")
st.markdown("Ingresá los **síntomas o signos clínicos** del paciente y recibí una orientación profesional.")

# Selector de modelo
modelos_disponibles = {
    "Mistral (rápido y gratuito)": "mistralai/mistral-7b-instruct",
    "Gemma (Google, claro y preciso)": "google/gemma-7b-it",
    "OpenChat (estilo ChatGPT)": "openchat/openchat-7b",
    "Neural Chat (Intel, generalista)": "intel/neural-chat-7b",
}
modelo_seleccionado = st.selectbox("🧠 Elegí el modelo de IA:", list(modelos_disponibles.keys()))
modelo_id = modelos_disponibles[modelo_seleccionado]

# Campo de entrada de síntomas
entrada = st.text_area("📋 Ingresá los síntomas clínicos observados:")

# Botón para analizar
if st.button("Analizar"):
    if entrada.strip() == "":
        st.warning("Por favor, ingresá una descripción antes de analizar.")
    else:
        with st.spinner("Analizando caso..."):

            # Enviar la consulta al modelo
            try:
                respuesta = openai.ChatCompletion.create(
                    model=modelo_id,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Sos un veterinario clínico experto en perros y gatos. "
                                "Respondé de forma clara, profesional, y sin hacer diagnósticos definitivos. "
                                "Ofrecé posibles causas, estudios complementarios sugeridos y conducta a seguir."
                            ),
                        },
                        {"role": "user", "content": entrada},
                    ],
                )

                # Mostrar la respuesta del modelo
                mensaje = respuesta['choices'][0]['message']['content']
                st.success("💡 Posible orientación:")
                st.markdown(mensaje)

            except Exception as e:
                st.error(f"Ocurrió un error al consultar el modelo: {e}")
