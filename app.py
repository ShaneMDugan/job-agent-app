import streamlit as st
from generator.cover_letter_generator import generate_cover_letter
from utils.gpt_prompts import extract_match_points

st.set_page_config(page_title="AI Job App Assistant", layout="centered")

st.title("📄 AI Job Application Assistant")
st.markdown("Tailor a cover letter with GPT-4 from your resume and job description.")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (.txt)", type="txt")

# Paste job description
job_desc = st.text_area("Paste Job Description", height=200)

# Form inputs
with st.form("generate_form"):
    hiring_manager = st.text_input("Hiring Manager", value="Hiring Manager")
    job_title = st.text_input("Job Title")
    company = st.text_input("Company Name")
    user_name = st.text_input("Your Name", value="Shane Dugan")
    submitted = st.form_submit_button("Generate Cover Letter")

if submitted:
    if uploaded_file is None or not job_desc.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        resume_text = uploaded_file.read().decode("utf-8")
        st.info("Generating match points with GPT-4...")
        match_points = extract_match_points(resume_text, job_desc)

        context = {
            "hiring_manager": hiring_manager,
            "job_title": job_title,
            "company": company,
            "skills": "Agile, backlog grooming, stakeholder collaboration",
            "match_points": match_points,
            "name": user_name
        }

        file_path = generate_cover_letter(context)
        st.success("✅ Cover Letter Generated!")

        with open(file_path, "rb") as f:
            st.download_button(
                label="📥 Download Cover Letter",
                data=f,
                file_name=f"{company}_Cover_Letter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
