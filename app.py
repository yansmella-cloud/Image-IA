import streamlit as st
from PIL import Image

st.title("🧠 Asistente de Triaje con IA (Demo)")
st.markdown("Este prototipo simula un análisis clínico a partir de una imagen médica + síntomas.")

uploaded_file = st.file_uploader("📸 Sube una imagen médica", type=["png", "jpg", "jpeg"])
symptoms = st.text_area("📝 Describe los síntomas del paciente")

if uploaded_file and symptoms:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen médica cargada", use_column_width=True)

    with st.spinner("Analizando con IA..."):
        # Simulación de resultado
        st.subheader("📄 Reporte Clínico Preliminar (simulado):")
        st.write("No se observan consolidaciones. Patrón bronquial aumentado. Posible proceso viral leve.")
        st.caption("Este resultado es una simulación mientras se integra el modelo real MedGemma.")
