import os
from skimage import io
from sklearn.cluster import KMeans
import numpy as np
from skimage.transform import resize


def KMeanCompression(img, k):
    """Compress an image using K-means clustering."""
    # Dimension of the original image
    # io.imshow(img)
    # io.show()
    # if k argument is not provided, use the default value 8
    if k is None:
        print("k is not provided, using default value 8")
        k = 8
    rows = img.shape[0]
    cols = img.shape[1]

    # Flatten the image
    img = img.reshape(rows * cols, 3)

    # Implement k-means clustering to form k clusters
    # size a liitle bit bigger with random_state=0
    # kmeans = KMeans(n_clusters=8, random_state=0).fit(image)
    kmeans = KMeans(n_clusters=k).fit(img)

    # Replace each pixel value with its nearby centroid
    compressed_image = kmeans.cluster_centers_[kmeans.labels_]
    compressed_image = np.clip(compressed_image.astype("uint8"), 0, 255)

    # Reshape the image to original dimension
    compressed_image = compressed_image.reshape(rows, cols, 3)

    # Save and display output image
    return compressed_image


def ResizeCompression(img, resize_factor):
    # resize image
    compressed_image = resize(
        img,
        (img.shape[0] // resize_factor, img.shape[1] // resize_factor),
        anti_aliasing=True,
    )
    # compressed_image = rescale(img, 0.25, anti_aliasing=True)
    return compressed_image
