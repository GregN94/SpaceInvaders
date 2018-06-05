import pygame


def load_and_scale(image, scale):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image,
                                   [int(dimension / scale) for dimension in image.get_size()])
    return image
