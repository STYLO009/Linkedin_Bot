from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Give greetings to the user on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
template="""
Write a professional LinkedIn post about: {topic}.

Rules:

Do NOT use markdown (no *, #, -, backticks, etc.)
Do NOT use bullet points
Write in clean plain text only
Keep it engaging and professional
You may use simple emojis

Output should be like a normal paragraph that can be directly posted on LinkedIn.
""",
input_variables=["topic"]
)

chain = RunnableParallel({
    'about': prompt1 | llm | parser,
    'linkedin': prompt2 | llm | parser
})

@app.post("/generate")
def generate(request: TopicRequest):
    return chain.invoke({'topic': request.topic})