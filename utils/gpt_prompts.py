import openai

def extract_match_points(resume_text, job_description):
    prompt = f"""Compare the following resume to the job description. Extract key alignment points.

Resume:
{resume_text}

Job Description:
{job_description}

List 3–5 match points as bullet points.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
