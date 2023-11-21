from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
def main(path):
    # load image from the IAM database
    url = path
    image = Image.open(requests.get(url, stream=True).raw).convert("RGB")


    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

