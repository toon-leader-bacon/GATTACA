import math
import random
from enum import Enum
from typing import Dict, List, Tuple
from PIL import Image, ImageChops
import json

from Transformer import Transformers


class Genetic:
    def __init__(self) -> None:
        pass


class Chromosome:
    def __init__(self) -> None:
        pass

    def to_json():
        pass

    def from_json():
        pass


CHROMOSOME_COST = 10
BLEND_RATIO_SCALE = 10
MAX_BLEND_RATIO = 0.4
GENETIC_DRIFT = 0.05  # 5%


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def drift_mult():
    return random.normalvariate(0, GENETIC_DRIFT)


def calculate_new_blend_ratio(old_blend_ratio):
    return clamp(old_blend_ratio + (MAX_BLEND_RATIO * drift_mult()),
                 0.001,
                 MAX_BLEND_RATIO)


class Chromosome_Empty():
    def __init__(self) -> None:
        pass

    def to_json(self):
        return {
            "Chromosome": "Empty"
        }

    def from_json(self, json_data):
        if "Chromosome" not in json_data:
            raise RuntimeError(f"Not a Chromosome Json blob: {json_data}")
        if "Empty" != json_data["Chromosome"]:
            raise RuntimeError(f"Not a Empty Chromosome Json blob: {json_data}")

    def modify_image(self, image: Image) -> Image:
        return image

    def cost(self):
        return 0

    def mutate(self) -> Chromosome:
        return Chromosome_Empty()

    def random_mutate(self) -> Chromosome:
        return Chromosome_Empty()


class Chromosome_Noise():
    def __init__(self, sigma=0.5, blend_ratio=0.2) -> None:
        self.sigma = sigma
        self.blend_ratio = blend_ratio

    def to_json(self):
        return {
            "Chromosome": "Noise",
            "Arguments": {
                "sigma": self.sigma,
                "blend_ratio": self.blend_ratio
            }
        }

    def from_json(self, json_data):
        if "Chromosome" not in json_data:
            raise RuntimeError(f"Not a Chromosome Json blob: {json_data}")
        if "Noise" != json_data["Chromosome"]:
            raise RuntimeError(f"Not a Noise Chromosome Json blob: {json_data}")

        self.sigma = json_data["Arguments"]["sigma"]
        self.blend_ratio = json_data["Arguments"]["blend_ratio"]

    def modify_image(self, image: Image) -> Image:
        t = Transformers()
        return t.noise(image, self.sigma, self.blend_ratio)

    def cost(self):
        return CHROMOSOME_COST + \
            (self.sigma * 5) + \
            (self.blend_ratio * BLEND_RATIO_SCALE)

    # def mutate(self) -> "Chromosome_Noise":

    #     sigma_points = (self.sigma * 5)
    #     blend_ratio_points = (self.blend_ratio * BLEND_RATIO_SCALE)
    #     remaining_total_points = sigma_points + blend_ratio_points

    #     # Modify sigma points +/- 5% (standard deviation)
    #     new_sigma_points = sigma_points * random.normalvariate(0, 0.05)
    #     remaining_total_points = remaining_total_points - new_sigma_points

    #     # Modify blend ration based on remaining points
    #     # If the other status go higher (above the total available points)
    #     # then blend ratio will effectively be 0
    #     remaining_total_points = remaining_total_points
    #     new_blend_ratio_points = remaining_total_points

    #     new_sigma = new_sigma_points / 5
    #     new_blend_ratio = min(MAX_BLEND_RATIO, max(new_blend_ratio_points / BLEND_RATIO_SCALE, 0.001))

        return Chromosome_Noise(new_sigma, new_blend_ratio)

    def random_mutate(self) -> "Chromosome_Noise":
        new_sigma = min(0, self.sigma * drift_mult())
        new_blend_ratio = calculate_new_blend_ratio(self.blend_ratio)
        return Chromosome_Noise(new_sigma, new_blend_ratio)


class Chromosome_Mandelbrot():
    def __init__(self, zoom_box=(-1.5, -1, 0.5, 1), quality=20, blend_ratio=0.2) -> None:
        self.zoom_box = zoom_box
        self.quality = quality
        self.blend_ratio = blend_ratio

    def to_json(self):
        return {
            "Chromosome": "Mandelbrot",
            "Arguments": {
                "zoom_box": self.zoom_box,
                "quality": self.quality,
                "blend_ratio": self.blend_ratio
            }
        }

    def from_json(self, json_data):
        if "Chromosome" not in json_data:
            raise RuntimeError(f"Not a Chromosome Json blob: {json_data}")
        if "Mandelbrot" != json_data["Chromosome"]:
            raise RuntimeError(f"Not a Mandelbrot Chromosome Json blob: {json_data}")

        self.zoom_box = json_data["Arguments"]["zoom_box"]
        self.quality = json_data["Arguments"]["quality"]
        self.blend_ratio = json_data["Arguments"]["blend_ratio"]

    def modify_image(self, image: Image) -> Image:
        t = Transformers()
        return t.mandelbrot(image, self.zoom_box, self.quality, self.blend_ratio)

    def cost(self):
        return CHROMOSOME_COST + \
            (self.quality) + \
            (self.blend_ratio * BLEND_RATIO_SCALE)

    def random_mutate_zoom_box(self):
        x0, y0, x1, y1 = self.zoom_box
        return (
            x0 + (2 * drift_mult()),
            y0 + (2 * drift_mult()),
            x1 + (2 * drift_mult()),
            y1 + (2 * drift_mult())
        )

    def random_mutate(self) -> "Chromosome_Mandelbrot":
        new_zoom_box = self.random_mutate_zoom_box()
        new_quality = max(2, int(self.quality + (100 * drift_mult())))
        new_blend_ratio = calculate_new_blend_ratio(self.blend_ratio)
        return Chromosome_Mandelbrot(new_zoom_box, new_quality, new_blend_ratio)


class Chromosome_LinearGradient():
    def __init__(self, rotation=180.0, blend_ratio=0.2) -> None:
        self.rotation = rotation
        self.blend_ratio = blend_ratio

    def to_json(self):
        return {
            "Chromosome": "LinearGradient",
            "Arguments": {
                "rotation": self.rotation,
                "blend_ratio": self.blend_ratio
            }
        }

    def from_json(self, json_data):
        if "Chromosome" not in json_data:
            raise RuntimeError(f"Not a Chromosome Json blob: {json_data}")
        if "LinearGradient" != json_data["Chromosome"]:
            raise RuntimeError(f"Not a LinearGradient Chromosome Json blob: {json_data}")

        self.rotation = json_data["Arguments"]["rotation"]
        self.blend_ratio = json_data["Arguments"]["blend_ratio"]

    def modify_image(self, image: Image) -> Image:
        t = Transformers()
        return t.linear_gradient(image, self.rotation, self.blend_ratio)

    def cost(self):
        return CHROMOSOME_COST + \
            (self.rotation * 5) + \
            (self.blend_ratio * BLEND_RATIO_SCALE)

    def random_mutate(self) -> "Chromosome_LinearGradient":
        new_rotation = clamp(self.rotation + (360 * drift_mult()), 0, 360)
        new_blend_ratio = calculate_new_blend_ratio(self.blend_ratio)
        return Chromosome_LinearGradient(new_rotation, new_blend_ratio)


class Chromosome_RadialGradient():
    def __init__(self, blend_ratio=0.2) -> None:
        self.blend_ratio = blend_ratio

    def to_json(self):
        return {
            "Chromosome": "RadialGradient",
            "Arguments": {
                "blend_ratio": self.blend_ratio
            }
        }

    def from_json(self, json_data):
        if "Chromosome" not in json_data:
            raise RuntimeError(f"Not a Chromosome Json blob: {json_data}")
        if "RadialGradient" != json_data["Chromosome"]:
            raise RuntimeError(f"Not a RadialGradient Chromosome Json blob: {json_data}")

        self.blend_ratio = json_data["Arguments"]["blend_ratio"]

    def modify_image(self, image: Image) -> Image:
        t = Transformers()
        return t.radial_gradient(image, self.blend_ratio)

    def cost(self):
        return CHROMOSOME_COST + \
            (self.blend_ratio * BLEND_RATIO_SCALE)

    def random_mutate(self) -> "Chromosome_RadialGradient":
        new_blend_ratio = calculate_new_blend_ratio(self.blend_ratio)
        return Chromosome_RadialGradient(new_blend_ratio)


MAX_DNA_LENGTH = 5


class Chromosome_Enum(Enum):
    Empty = 0
    Noise = 1
    Mandelbrot = 2
    LinearGradient = 3
    RadialGradient = 4


ALL_CHROMOSOME_ENUM = [Chromosome_Enum.Empty,
                       Chromosome_Enum.Noise,
                       Chromosome_Enum.Mandelbrot,
                       Chromosome_Enum.LinearGradient,
                       Chromosome_Enum.RadialGradient]


class ChromosomeFactory():

    def random_chromosome(self):
        enum = random.sample(ALL_CHROMOSOME_ENUM, 1)[0]
        return self.build_chromosome(enum)

    def build_chromosome(self, chromosome: Chromosome_Enum):
        global MAX_BLEND_RATIO
        if chromosome is Chromosome_Enum.Empty:
            return Chromosome_Empty()
        elif chromosome is Chromosome_Enum.Noise:
            return Chromosome_Noise(blend_ratio=MAX_BLEND_RATIO / 2)
        elif chromosome is Chromosome_Enum.Mandelbrot:
            return Chromosome_Mandelbrot(blend_ratio=MAX_BLEND_RATIO / 2)

        elif chromosome is Chromosome_Enum.LinearGradient:
            return Chromosome_LinearGradient(blend_ratio=MAX_BLEND_RATIO / 2)
        elif chromosome is Chromosome_Enum.RadialGradient:
            return Chromosome_RadialGradient(blend_ratio=MAX_BLEND_RATIO / 2)
        # default
        return Chromosome_Empty()

    def from_json(self, json):
        chro_type = json["Chromosome"]
        if chro_type == "Mandelbrot":
            result = Chromosome_Mandelbrot()
            result.from_json(json)
            return result
        if chro_type == "RadialGradient":
            result = Chromosome_RadialGradient()
            result.from_json(json)
            return result
        if chro_type == "LinearGradient":
            result = Chromosome_LinearGradient()
            result.from_json(json)
            return result
        if chro_type == "Noise":
            result = Chromosome_Noise()
            result.from_json(json)
            return result
        if chro_type == "Empty":
            result = Chromosome_Empty()
            result.from_json(json)
            return result
        raise ValueError(f"Unexpected Chromosome Type: {chro_type}")

class DNA_Factory():
    def shuffle(self, dna):
        new_dna = list(dna)
        random.shuffle(new_dna)
        return new_dna

    def crossover(self, dna_A, dna_B):
        dna_split_index = random.randint(1, MAX_DNA_LENGTH - 1)
        new_dna_A = dna_A[0:dna_split_index]
        new_dna_B = dna_B[dna_split_index:MAX_DNA_LENGTH]
        return new_dna_A + new_dna_B

    def mutate_one_(self, dna, mutate_index):
        mutate_index = int(clamp(mutate_index, 0, MAX_DNA_LENGTH - 1))
        old_chromosome: Chromosome = dna[mutate_index]
        new_chromosome = old_chromosome.random_mutate()
        dna[mutate_index] = new_chromosome
        return dna

    def mutate_one_random(self, dna):
        target_index = random.randint(0, MAX_DNA_LENGTH - 1)
        return self.mutate_one_(dna, target_index)

    def replace_one_(self, dna, replace_index):
        replace_index = int(clamp(replace_index, 0, MAX_DNA_LENGTH - 1))
        factory = ChromosomeFactory()
        new_chromosome = factory.random_chromosome()
        dna[replace_index] = new_chromosome
        return dna

    def replace_one_random(self, dna):
        target_index = random.randint(0, MAX_DNA_LENGTH - 1)
        return self.replace_one_(dna, target_index)

    def breed(self, dna_A, dna_B):
        new_dna = self.crossover(dna_A, dna_B)
        if random.random() <= 0.02:
            # 2% chance of shuffle
            new_dna = self.shuffle(new_dna)

        replace_random = random.random()
        if replace_random <= 0.05:
            # 5% chance of 1 replacement
            new_dna = self.replace_one_random(new_dna)
        if replace_random <= 0.075:
            # 2.5% chance of 2 replacement
            new_dna = self.replace_one_random(new_dna)
            new_dna = self.replace_one_random(new_dna)
        if replace_random <= 0.085:
            # 1% chance of 3 replacement
            new_dna = self.replace_one_random(new_dna)
            new_dna = self.replace_one_random(new_dna)
            new_dna = self.replace_one_random(new_dna)

        mutate_random = random.random()
        if mutate_random <= 0.20:
            # 20% chance of one mutation
            new_dna = self.mutate_one_random(new_dna)
        elif mutate_random <= 0.30:
            # 10% chance of two mutations
            new_dna = self.mutate_one_random(new_dna)
            new_dna = self.mutate_one_random(new_dna)
        elif mutate_random <= 0.35:
            # 5% chance of three mutations
            new_dna = self.mutate_one_random(new_dna)
            new_dna = self.mutate_one_random(new_dna)
            new_dna = self.mutate_one_random(new_dna)
        return new_dna


class Organism:

    def __init__(self, dna: List[Chromosome]) -> None:
        self.dna: List[Chromosome] = dna
        if len(self.dna) > MAX_DNA_LENGTH:
            self.dna = self.dna[0:MAX_DNA_LENGTH]

        while len(self.dna) < MAX_DNA_LENGTH:
            self.dna.append(Chromosome_Empty())

    def breed(self, other: "Organism") -> "Organism":
        factory = DNA_Factory()
        return Organism(factory.breed(self.dna, other.dna))

    def modify_image(self, image: Image) -> Image:
        for chromosome in self.dna:
            image = chromosome.modify_image(image)
        return image

    @staticmethod
    def make_random() -> "Organism":
        factory = ChromosomeFactory()
        return Organism([
            factory.random_chromosome(),
            Chromosome_Empty(),
            factory.random_chromosome(),
            Chromosome_Empty(),
            factory.random_chromosome()
        ])

    def to_json(self):
        return {
            "DNA": [chromosome.to_json() for chromosome in self.dna]
        }

    def from_json(self, json_data):
        new_dna = []
        factory = ChromosomeFactory()
        for chro_json in json_data["DNA"]:
            new_chromosome = factory.from_json(chro_json)
            new_dna.append(new_chromosome)
        self.dna = new_dna

    def random_mutate(self) -> "Organism":
        new_dna = [chro.random_mutate() for chro in self.dna]
        return Organism(new_dna)


class GenerationFactory():
    @staticmethod
    def make_random(size=100):
        return Generation([Organism.make_random() for _ in range(size)])

    @staticmethod
    def breed_next_generation(parents):
        children: List[Organism] = []
        parent_asexual: List[Organism] = [parent.random_mutate() for parent in parents]
        parent_pairs: List[Organism] = [parent.breed(other) for parent in parents for other in parents]
        children = parent_asexual + parent_pairs  # + parents
        return Generation(children)


class Generation:

    def __init__(self, initial_organisms: List[Organism] = []) -> None:
        self.orgs_to_fitness: Dict[Organism, float] = {}
        self.fitness_tracker: Dict[Organism, Tuple[float, int]] = {}
        for org in initial_organisms:
            self.orgs_to_fitness[org] = 0
            self.fitness_tracker[org] = (0, 0)

    @staticmethod
    def make_random(size=100, max_blend_ratio = 0.4) -> "Generation":
        global MAX_BLEND_RATIO
        MAX_BLEND_RATIO = max_blend_ratio
        return GenerationFactory.make_random(size)

    def organisms(self) -> List[Organism]:
        return self.orgs_to_fitness.keys()

    def add_fitness_entry(self, organism, fitness_entry):
        (fitness_sum, count) = self.fitness_tracker[organism]
        self.fitness_tracker[organism] = (fitness_sum + fitness_entry, count + 1)

    def calculate_average_fitness(self):
        for (organism, (fitness_sum, count)) in self.fitness_tracker.items():
            count = max(1, count)  # Can't be 0 or negative
            average_fitness = fitness_sum / count
            self.orgs_to_fitness[organism] = average_fitness

    def get_best_k(self, k) -> List[tuple[Organism, float]]:
        self.calculate_average_fitness()
        sorted_orgs = sorted(self.orgs_to_fitness.items(), key=lambda item: item[1], reverse=True)
        # sorted_orgs = sorted(self.orgs_to_fitness.keys(), key=self.orgs_to_fitness.values())
        k = clamp(k, 0, len(sorted_orgs))
        return sorted_orgs[0:k]
