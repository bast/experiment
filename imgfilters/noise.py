from skimage import util


def add_noise(image, amount):
    noisy_image = util.random_noise(image, mode="s&p", amount=amount)
    return noisy_image
