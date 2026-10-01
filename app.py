import streamlit as st
from modules.resume_parser import extract_resume_text


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="📄",
    layout="wide"
)


# -----------------------------------
# APP TITLE
# -----------------------------------

st.title("CareerMatch AI")

st.subheader("AI Resume Analyzer & Job Matching System")

st.write(
    "Upload your resume and compare it with a job description "
    "to find your match score, matching skills, and skill gaps."
)

st.divider()


# -----------------------------------
# RESUME UPLOAD
# -----------------------------------

st.header("1. Upload Your Resume")

resume = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"]
)

if resume is not None:
    st.success(f"Uploaded: {resume.name}")


# -----------------------------------
# JOB DESCRIPTION
# -----------------------------------

st.header("2. Enter Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder=(
        "Example: We are looking for a Python developer "
        "with experience in Machine Learning, SQL, Git, "
        "Pandas and Data Analysis..."
    )
)


# -----------------------------------
# ANALYZE BUTTON
# -----------------------------------

if st.button(
    "Analyze Resume & Match Job",
    type="primary"
):

    # Check resume
    if resume is None:

        st.warning(
            "Please upload your resume."
        )

    # Check job description
    elif not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

    else:

        # -----------------------------------
        # EXTRACT RESUME TEXT
        # -----------------------------------

        try:

            resume_text = extract_resume_text(resume)

            if resume_text.strip():

                st.success(
                    "Resume analyzed successfully!"
                )

                st.divider()

                # -----------------------------------
                # SHOW RESUME TEXT
                # -----------------------------------

                st.header("3. Extracted Resume Text")

                st.text_area(
                    "Resume Content",
                    value=resume_text,
                    height=350
                )

                # -----------------------------------
                # SHOW JOB DESCRIPTION
                # -----------------------------------

                st.header("4. Job Description")

                st.text_area(
                    "Job Description Content",
                    value=job_description,
                    height=250,
                    disabled=True
                )

                st.divider()

                # Placeholder for next feature

                st.info(
                    "Next step: AI will compare the resume "
                    "with this job description and calculate "
                    "the job match score."
                )

            else:

                st.error(
                    "Could not extract text from the resume."
                )

        except Exception as error:

            st.error(
                f"Error while reading resume: {error}"
            )


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "CareerMatch AI | LLM-Based Resume Analysis & Job Matching Project"
)