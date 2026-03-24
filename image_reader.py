from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# load model once
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def extract_image_text(image_file):

    image = Image.open(image_file).convert("RGB")

    inputs = processor(image, return_tensors="pt")

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    return caption