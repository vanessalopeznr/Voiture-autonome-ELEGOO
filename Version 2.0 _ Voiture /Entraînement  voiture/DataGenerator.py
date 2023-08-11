import os
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator

# Total number of augmented images to generate
total_augmented_images = 30

# Create an ImageDataGenerator with desired augmentations
data_gen = ImageDataGenerator(rescale=1. / 255,
                              rotation_range=40,
                              width_shift_range=0.2,
                              height_shift_range=0.2,
                              shear_range=0.2,
                              zoom_range=0.2,
                              horizontal_flip=True,
                              fill_mode='nearest')

# Load the input image and convert it to a tensor
#for k in range(1, 6):

img = load_img("imgs/atras.jpeg", grayscale=False)
arr = img_to_array(img)
tensor_image = arr.reshape((1, ) + arr.shape)

# Generate augmented images and save them to the output directory
i = 0
for batch in data_gen.flow(x=tensor_image,
                        batch_size=1,
                        save_to_dir='ready',
                        save_prefix='augmented',
                        save_format='png'):
    i += 1
    if i >= total_augmented_images:
        break

print("Dataset generation complete.")
