from imgfilters.file_io import read_image
from imgfilters.filters import pixelate
from imgfilters.metrics import mean_squared_error


def test_pixelation():
    image = read_image("data/astronaut.jpg")

    image_pixelated = pixelate(image, scale=0.05, num_colors=8)
    image_reference = read_image("tests/reference/astronaut-pixelated.jpg")

    assert mean_squared_error(image_pixelated, image_reference) < 1e-3
