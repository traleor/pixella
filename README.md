# Pixella

This is an Image Processing tool written in Python. Th initial functionality for this tool is an efficient compression algorithm that can be used to compress images.

## Functionalites

- [x] Image Compression
- [x] Image Resize

## Setup Instructions

- Download and Install the latest Python 3 on your computer. [Install Now](https://www.python.org/downloads/)
- Create a virtual environment where all packages will be installed.

```bash
# Windows
py -3 -m venv env
# Linux and Mac
python3 -m venv env
```

- Activate the virtual environment.

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```

- Install all the required packages.

```bash
pip install -r requirements.txt
```

- Run main.py

```bash
<!-- test main algorithm -->
python main.py
<!-- run django app -->
python manage.py runserver
<!-- visit http://localhost:8000/ on your browser -->
```

## Resources

- [Image Compression using Machine Learning](https://towardsdatascience.com/image-compression-using-k-means-clustering-aa0c91bb0eeb)
- [AI Image Compression](https://towardsdatascience.com/ai-based-image-compression-the-state-of-the-art-fb5aa6042bfa)
- [Introduction to Image Processing with Python](https://towardsdatascience.com/introduction-to-image-processing-with-python-representation-of-images-for-beginners-b95725b523ca)
- [Numpy Docs - compress](https://numpy.org/doc/stable/reference/generated/numpy.compress.html)
