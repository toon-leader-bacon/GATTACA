from src.Classifier import process_image, process_image_label
from PIL import Image
from datasets import load_dataset
from transformers import AutoImageProcessor, ResNetForImageClassification
import time
import os
import csv

from src.Genetic import MAX_BLEND_RATIO, Generation, GenerationFactory, Organism


def main():

    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

    # start = time.time()
    global MAX_BLEND_RATIO
    for blend_ratio in range(1, 11):
        MAX_BLEND_RATIO = blend_ratio / 10
        gen: Generation = Generation.make_random(size=20, max_blend_ratio=MAX_BLEND_RATIO)
        print(f"{MAX_BLEND_RATIO}")
        
        for gen_count in range(10):
            print(f"  {gen_count}")
            for filename in os.listdir("./TestImages"):
                if ".jpg" not in filename:
                    continue
                print(f"    - {filename}")
                initial_image = Image.open(f"./TestImages/{filename}")
                predicted_id, _, initial_confidence_value = process_image(initial_image, processor, model)

                for org in gen.organisms():
                    new_image = org.modify_image(initial_image)
                    _, _, new_confidence_value = process_image_label(new_image, processor, model, predicted_id)

                    fitness = initial_confidence_value - new_confidence_value
                    gen.add_fitness_entry(org, fitness)

            best_k = gen.get_best_k(8)
            with open('./Results.csv', 'a') as f:
                writer = csv.writer(f)
                for org, fitness in best_k:
                    writer.writerow([gen_count, org.to_json(), fitness])

            next_generation = GenerationFactory.breed_next_generation([org for org, fitness in best_k])
            gen = next_generation
            # print(len(next_generation.orgs_to_fitness))
        

    # end = time.time()
    # delta_t = end - start
    # print(f"Time for 1 generation: {delta_t / 10.0}")
    # print(f"Time for 10 generations: {delta_t}")
    # print(f"Time for 100 generation: {delta_t * 10.0}")
    # print(f"Time for 1000 generation: {delta_t * 100.0}")


if __name__ == "__main__":
    main()
