import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


# [k_means_colorization] takes in an image path [image_path], a number of colors [num_colors], and two optional
# arguments [color_1] and [color_2]. It sorts the rgb data of the image using the k-means clustering algorithm, and
# recolors the image using interpolations between [color_1] and [color_2] before displaying the image.
def k_means_colorization(image_path, num_colors, color_1=None, color_2=None):

    # Try to get the image; if it doesn't exist, return
    try:
        image = Image.open(image_path)
    except IOError:
        print('Could not find image file.')
        return

    # Setting width and height of image
    width, height = image.size

    # Initializing new image and its pixel array
    new_image = Image.new('RGB', (width, height), 'white')
    new_image_pixels = new_image.load()

    # Assign two colors if they weren't given as an input
    if color_1 is None:
        color_1 = np.array([255, 255, 255])
    if color_2 is None:
        color_2 = np.array([0, 0, 0])

    # Turn image into a numpy array to manipulate
    image = np.asarray(image)

    # Get the (r, g, b) arrays from the image
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    # Flatten the arrays so we can use their values as coordinates and pass it into a new vector [coordinates]
    coordinates = np.dstack((r.flatten('F'), g.flatten('F'), b.flatten('F')))[0].astype('float')

    # Call k-means algorithm using [num_colors] clusters on our vector [coordinates]
    k_means = KMeans(n_clusters=num_colors, random_state=0).fit(coordinates)

    # Get the label for each data point
    labels = k_means.labels_

    # Initialize our vector of colors
    colors = np.zeros((width*height, 3))

    # Initialize dictionary of color mappings
    color_dict = {}

    # Taking each label and turning it into its respective color using memoization
    for idx, num in enumerate(labels):
        # If num isn't in the color dictionary, add it using linear interpolation for color
        if num not in color_dict:
            temp = num * (color_2 - color_1) / float(num_colors-1) + color_1
            color_dict[num] = temp.astype('uint8')

        colors[idx] = color_dict[num]

    # Initialize our counter
    idx = 0

    # Loop through our pixels and assign color
    for i in range(width):
        for j in range(height):
            new_image_pixels[i, j] = tuple(map(lambda x: x.astype('uint8'), colors[idx]))
            idx += 1

    # Show the new image
    new_image.show()

    return new_image
