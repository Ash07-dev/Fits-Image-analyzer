from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astropy.visualization import ImageNormalize,LogStretch, ZScaleInterval

fits_file = fits.open("horsehead.fits") #Using the fits file
# print(fits_file)

image_data = fits_file[0].data   # Checking the data is it there
# print(image_data)

# Removes Noise
norm = ImageNormalize(image_data, interval=ZScaleInterval(), stretch=LogStretch())

plt.figure()
plt.imshow(image_data, origin="lower", norm = norm, cmap="copper")
plt.colorbar()
plt.savefig('main.png', dpi=150)
plt.close()

# To get a section in the image 
section1 = image_data[2000:2250, 1500:2500]

plt.figure()
plt.imshow(section1, origin="lower", norm = LogNorm(), cmap = "Greys")
plt.colorbar()
plt.savefig('main_section.png', dpi=150)
plt.close()