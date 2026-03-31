import google.generativeai as genai

genai.configure(api_key="AIzaSyAWLYZF_lQ1v7mijgLNnXU0OB7mpCR45XM")

for model in genai.list_models():
    if "embedContent" in model.supported_generation_methods:
        print(model.name)

 