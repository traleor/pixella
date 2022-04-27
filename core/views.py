import os
from skimage import io

from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError

from .utils import KMeanCompression, ResizeCompression
from django.core.files.storage import FileSystemStorage


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def index(request):
    message = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        image_size = round(os.path.getsize(path) / 1024, 2)
        # Read the image
        try:
            imageObj = io.imread(path)
        except Exception as e:
            print("File not found", e)
            return TemplateResponse(
                request,
                "index.html",
                {"message": "No Image Found, Try Again"},
            )

        # print("OBJECT: ", imageObj)
        image_dim = str(imageObj.shape[1]) + " x " + str(imageObj.shape[0])

        # delete _image
        print(message, image_url)

        k = 8
        try:
            compressed_image = KMeanCompression(imageObj, k)
            message = "Image successfully compressed: Lossless"
        except Exception as e:
            print("Exception", e)
            compressed_image = ResizeCompression(imageObj, 2)
            message = "Image successfully compressed: Lossy"

        io.imsave(
            str(settings.MEDIA_ROOT) + "/" + "output_" + image.name, compressed_image
        )
        compressed_image_url = fss.url("output_" + image.name)
        compressed_image_size = round(
            os.path.getsize(str(settings.MEDIA_ROOT) + "/" + "output_" + image.name)
            / 1024,
            2,
        )
        print("COMPRESSED", image_url)
        return TemplateResponse(
            request,
            "index.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "image_size": image_size,
                "image_dim": image_dim,
                "compressed_image_url": compressed_image_url,
                "compressed_image_size": compressed_image_size,
            },
        )
    except MultiValueDictKeyError:
        # is_private = False

        return TemplateResponse(
            request,
            "index.html",
            {"message": "No Image Selected"},
        )
