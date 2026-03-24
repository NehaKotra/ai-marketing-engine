from openai import OpenAI
import requests

# put your key here
client = OpenAI(api_key="OPENAI_API_KEY")

def generate_marketing_image(prompt):

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )

        image_url = response.data[0].url

        image_path = "generated_marketing_image.png"

        img = requests.get(image_url).content

        with open(image_path, "wb") as f:
            f.write(img)

        return image_path

    except Exception as e:
        print("Image generation error:", e)
        return None