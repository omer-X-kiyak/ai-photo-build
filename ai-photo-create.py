import openai
command=input("kelime grin :\t")
openai.api_key = "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"

response = openai.Completion.create(
    engine="davinci",
    prompt="Hello, how can I assist you today?",
    max_tokens=60
)

result = response.choices[0].text
print(result)

image_response = openai.Image.create(
    prompt=command,
    n=1,
    size="1024x1024"
)

print(image_response)
