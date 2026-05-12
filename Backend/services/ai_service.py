from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



def tailor_resume(resume_text, jd_text, keywords):

    prompt = f"""
You are a professional ATS resume writer.

TASK:
Rewrite and tailor the resume according to the job description.

RULES:
1. Keep information truthful.
2. Improve bullet points.
3. Add ATS keywords naturally.
4. Make it professional.
5. Keep formatting ATS friendly.
6. Do not add fake experience.

JOB DESCRIPTION:
{jd_text}

IMPORTANT KEYWORDS:
{keywords}

ORIGINAL RESUME:
{resume_text}
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content