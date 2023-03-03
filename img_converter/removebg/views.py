from django.shortcuts import render
from .utils import Remove
from django.http import FileResponse, HttpResponse, JsonResponse
# Create your views here.

def index(request):
    """This function renders the index.html file
        It also removes the background image of a picture
        and return the path new image name and the original
        image name.
    """
    if request.method == "POST":
        # Gets the image(s) from the POST request
        image = request.FILES["image"]

        # Instantiates the Remove class from utils.py
        transform = Remove(image, "png")

        # Removes the background image
        file = transform.removeBackgroundImage()

        # Gets the original name of the image
        filename = image.name.split(".")[0] + "." + "png"

        # Sends the new image name and the original image name
        data = {"file": file.split("/")[-1], "filename": filename}

        return JsonResponse(data, safe=False)

    return render(request, "remove-bg/index.html")


def download_file(request, file, filename):
    """This function finds the file and sends it to the user"""

    img = open(f"img_converter/removebg/download/{file}", "rb")
    response = FileResponse(img, as_attachment=True, filename=filename)
    return response

