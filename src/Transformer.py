from PIL import Image, ImageChops
import random
import os
from numpy import asarray
import numpy as np
from torch import norm


class Rotate:
    def __init__(self, direction=0) -> None:
        self.direction = direction

    def apply(self, image: Image) -> Image:
        return image.rotate(self.direction)


class Transformers:
    def __init__(self) -> None:
        pass

    def mandelbrot(self, image: Image, zoom_box=(-1.5, -1, 0.5, 1), quality=20, blend_ratio=0.2) -> Image:
        x0 = min(zoom_box[0], zoom_box[2])
        x1 = max(zoom_box[0], zoom_box[2])
        y0 = min(zoom_box[1], zoom_box[3])
        y1 = max(zoom_box[1], zoom_box[3])
        quality = max(2, int(quality))
        
        mandelbrot_img: Image = Image.effect_mandelbrot(image.size, (x0, y0, x1, y1), quality)
        mandelbrot_img = mandelbrot_img.convert('RGB')
        return Image.blend(image, mandelbrot_img, blend_ratio)

    def noise(self, image: Image, sigma=0.5, blend_ratio=0.2) -> Image:
        noise_img: Image = Image.effect_noise(image.size, sigma=sigma)
        noise_img = noise_img.convert('RGB')
        return Image.blend(image, noise_img, blend_ratio)

    def linear_gradient(self, image: Image, rotation=0, blend_ratio=0.2) -> Image:
        gradient: Image = Image.linear_gradient(mode="L").rotate(
            rotation, expand=False, fillcolor="grey").resize(image.size)
        gradient = gradient.convert('RGB')
        return Image.blend(image, gradient, blend_ratio)

    def radial_gradient(self, image: Image, blend_ratio=0.2) -> Image:
        gradient: Image = Image.radial_gradient(mode="L").resize(image.size)
        gradient = gradient.convert('RGB')
        return Image.blend(image, gradient, blend_ratio)

    # def crop(self, image: Image, box=(0, 0, 9999, 9999)) -> Image:
    #   width, height = image.size
    #   smallest_x = max(0, min(box[0], box[2]))
    #   largest_x = min(width, max(box[0], box[2]))
      
    #   smallest_y = max(0, min(box[1], box[3]))
    #   largest_y = min(height, max(box[1], box[3]))
    #   return Image.crop()


class Compare_Image:
    def __init__(self) -> None:
        pass

    def manhattan_distance(self, img1: Image, img2: Image) -> float:
        diff = asarray(img1) - asarray(img2)  # element wise pixel difference
        manhattan_distance = np.sum(abs(diff))  # Manhattan norm
        width, height = img1.size
        manhattan_average = manhattan_distance / max(width * height, 1)
        return manhattan_average

    def z_norm(self, img1: Image, img2: Image) -> float:
        diff = asarray(img1) - asarray(img2)  # element wise pixel difference
        z_norm = norm(diff.ravel(), 0)
        width, height = img1.size
        z_norm_average = z_norm / max(width * height, 1)
        return z_norm_average


if __name__ == "__main__":
    initial_cat: Image = Image.open("./TestImages/cat1.jpg")
    transformer = Transformers()
    compare = Compare_Image()

    # transformer.mandelbrot(initial_cat, zoom_box=(-1.5, -1, 0.5, 1), blend_ratio=0.3).show()
    # # transformer.mandelbrot(initial_cat, zoom_box=(0, -1, 0.5, 1), blend_ratio=0.3).show()
    img = transformer.mandelbrot(initial_cat, zoom_box=(
        random.uniform(-1.50, 1.50),
        random.uniform(-1.50, 1.50),
        random.uniform(-1.50, 1.50),
        random.uniform(-1.50, 1.50)), blend_ratio=0.4)
    img.show()

    # transformer.noise(initial_cat, sigma=100, blend_ratio=0.3).show()
    # transformer.noise(initial_cat, sigma=random.uniform(0, 250), blend_ratio=0.3).show()

    # transformer.linear_gradient(initial_cat, rotation=0, blend_ratio=0.3).show()
    # transformer.linear_gradient(initial_cat, rotation=random.uniform(0, 360), blend_ratio=0.3).show()

    # transformer.radial_gradient(initial_cat, blend_ratio=0.3).show()
    # transformer.radial_gradient(initial_cat, blend_ratio=0.3).show()
