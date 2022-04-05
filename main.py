import os
from skimage import io
from sklearn.cluster import KMeans
import numpy as np


def KCompression(img, k):
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


def main():
    path = os.getcwd()
    image_name = input(
        "Enter the image name found in assets/images folder including its extension: "
    )
    print("Loading image...")
    print("\n")

    # Read the image
    try:
        image = io.imread(path + "/assets/images/" + image_name)
    except Exception as e:
        print("File not found", e)
        return

    # Compress the image
    # select compression method 1. Kcompression 2. Kmeans
    compression_method = int(input("Select compression method: 1. Kcompression 2. OtherCompression: "))
    print("\n")
    if compression_method == 1:
        # 1. Compress the image with KCompression
        compressed_image = KCompression(image, None)

    # Save and display output image
    io.imsave("out.png", compressed_image)


if __name__ == "__main__":
    main()
