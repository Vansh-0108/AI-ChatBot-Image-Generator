from openai import OpenAI

openai = OpenAI(
    api_key = "<secret-key>"
)

response = openai.images.generate(
    prompt="a donkey on a horse",
    n=1,
    size="256x256"
)

image_url = response.data[0].url
print(image_url)