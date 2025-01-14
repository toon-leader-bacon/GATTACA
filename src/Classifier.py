from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from datasets import load_dataset
from PIL import Image


def process_image(image, processor, model):
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
    # model predicts one of the 1000 ImageNet classes
    predicted_id = logits.argmax(-1).item()
    confidence_value = logits[0, predicted_id]
    predicted_label = model.config.id2label[predicted_id]
    return (predicted_id, predicted_label, confidence_value)


def process_image_label(image, processor, model, expected_id):
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits
    # model predicts one of the 1000 ImageNet classes
    confidence_value = logits[0, expected_id]
    predicted_label = model.config.id2label[expected_id]
    return (expected_id, predicted_label, confidence_value)


if __name__ == "__main__":

    dataset = load_dataset("huggan/cats")
    # image = dataset["test"]["image"][0]
    image = Image.open("./TestImages/cat1.jpg")

    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

    import time

    start = time.time()
    for i in range(10):
        print(i)
        image = dataset["train"]
        image = dataset["train"][i]
        image = dataset["train"][i]['image']
        # image = dataset["train"]["image"]
        # image = dataset["train"]["image"][i]
        print(i)
        process_image(image, processor, model)
    end = time.time()
    delta_t = end - start
    print(f"Time for 1 image: {delta_t / 10.0}")
    print(f"Time for 10 images: {delta_t}")
    print(f"Time for 100 image: {delta_t * 10.0}")
    print(f"Time for 1000 image: {delta_t * 100.0}")
