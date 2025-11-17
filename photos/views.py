from django.shortcuts import render

def gallery(request):
    images = [
        "photos/images/pic1.jpg",
        "photos/images/pic2.jpg",
        "photos/images/pic3.jpg",
        "photos/images/pic4.jpg",
        "photos/images/pic5.jpg",
    ]
    return render(request, "photos/gallery.html", {"images": images})
