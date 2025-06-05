from google import genai
import os



def get_car_ai_bio(model, brand, model_year):
    api = os.environ.get("api")
    client = genai.Client(api_key=api)
    
    prompt = "Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. " \
    "Fale coisas específicas desse modelo. Descreva especificações técnicas desse modelo de carro."
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt.format(model, brand, model_year)
)
    
    return response.text


'''def get_car_ai_bi(model, brand, year):
    client = genai.Client(api_key="")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["Me mostre uma descrição de venda para o carro em apenas 250 caracteres. Fale coisas específicas desse modelo. "
                  "Descreva especificações técnicas desse modelo de carro."]
            
)
    return response'''