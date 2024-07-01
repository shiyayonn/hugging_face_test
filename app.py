from transformers import pipeline

output = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

text = output("json.png")[0]["generated_text"]
print(text)

