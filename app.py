# app.py

import streamlit as st
from ats import analyze_cv, process_response

# Mock API key (not used in this version)
API_KEY = "AIzaSyB7LMxK0WfTrRrmWHbCd8RmxBWcG1YzLWI"

st.title("Applicant Tracking System")
st.write("Upload your CV and Job Description to get a CV score and improvement suggestions.")

job_description = st.text_area("Job Description", height=200)
cv_text = st.text_area("CV Text", height=200)

if st.button("Analyze CV"):
    if job_description and cv_text:
        response = analyze_cv(job_description, cv_text, API_KEY)
        cv_score, improvements, suggestions = process_response(response)

        st.write(f"**CV Score:** {cv_score}")
        st.write("**Things that can be improved in CV:**")
        for item in improvements:
            st.write(f"- {item}")
        st.write("**Skills Improvement Suggestions:**")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
    else:
        st.error("Please enter both Job Description and CV Text.")



