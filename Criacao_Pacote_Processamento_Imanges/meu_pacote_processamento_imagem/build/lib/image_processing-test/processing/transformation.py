from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 <= proportion <=1, "Especifique uma proporção válida entre 0 and 1."
    height = round(image.shape[0]*proportion)
    width = round(image.shape[1]*proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized