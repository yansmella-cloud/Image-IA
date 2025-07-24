import streamlit as st
from PIL import Image
import torch
from transformers import MedGemmaProcessor, MedGemmaForConditionalGeneration

@st.cache_resource
def load_model():
    processor = MedGemmaProcessor.from_pretrained("google/medgemma-7b")
    model = MedGemmaForConditionalGeneration.from_pretrained("google/medgemma-7b", device_map="auto")
    return processor, model

st.title("🧠 MedGemma para Triaje Clínico")
st.markdown("Asistente clínico preliminar basado en imagen médica + síntomas del paciente.")

uploaded_file = st.file_uploader("📸 Sube una imagen médica (rayos X, etc)", type=["jpg", "jpeg", "png"])
symptoms = st.text_area("📝 Describe los síntomas del paciente")

if uploaded_file and symptoms:
    with st.spinner("Analizando..."):
        processor, model = load_model()
        image = Image.open(uploaded_file).convert("RGB")
        inputs = processor(images=image, text=symptoms, return_tensors="pt").to(model.device)
        output = model.generate(**inputs, max_new_tokens=128)
        result = processor.batch_decode(output, skip_special_tokens=True)[0]

        st.success("✅ Reporte generado:")
        st.write(result)