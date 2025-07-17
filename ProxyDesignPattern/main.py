from Proxy.ImageProxy import HighResolutionImageProxy
from models.HighResolutionImage import HighResolutionImage

# image = HighResolutionImage('bike.jpg','10MB')
#
# #At this point i just need a file but still will loaded an image from Disk
# print(image.get_file_name())


# Now Will use HighResolution Proxy
high_proxy = HighResolutionImageProxy('car.jpg', '100MB')
print(high_proxy.get_file_name())
high_proxy.display()