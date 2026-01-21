from openai import OpenAI
import json

#

client = OpenAI()

def request_to_openai(context: list[dict]) -> str:
    
    request = client.responses.create(
        model="gpt-4.1",
        input=context
    )
    
    #
    
    return request.output_text
#

def generate_qa(qa_base: str, question: str, answer: str) -> str:
    
    context = list()
    
    with open("static/generate_qa.txt", "r", encoding = "utf-8") as file:
        
        context.append({"role": "system", "content": file.read().format(qa_base=qa_base)})
    #
    
    context.append({"role": "user", "content": f"Вопрос пользователя: {question}\nОтвет администратора: {answer}"})
    
    #
    
    return request_to_openai(context)
#