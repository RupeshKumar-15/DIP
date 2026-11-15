# 1. Perform the following:
# a. Read and display image.
# b. Resize a given image.
# c. Convert a given color image into a corresponding gray-scale image.
# d. Convert a given color/gray-scale image into black & white image f. Draw the image 
# profile.
# e. Separate a given color image into three R G & B planes.
# f.
# Create a color image using separate three R, G and B planes.
# g. Write given 2-D data in image file.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("xray2.jpg")

# Check whether image was read
if img is None:
    print("Image not found!")
    exit()

# a. Display image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()

# b. Resize
print("Original dimensions:", img.shape)
resized = cv2.resize(img, (300, 200))
plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
plt.title("Resized Image")
plt.axis("off")
plt.show()
print("Resized dimensions:", resized.shape)
# c. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# d. Convert to black and white
_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

plt.imshow(bw, cmap="gray")
plt.title("Black and White Image")
plt.axis("off")
plt.show()

# e. Separate R, G and B planes
B, G, R = cv2.split(img)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap="gray")
plt.title("Red Plane")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(G, cmap="gray")
plt.title("Green Plane")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(B, cmap="gray")
plt.title("Blue Plane")
plt.axis("off")

plt.show()

# f. Create color image from R, G and B planes
reconstructed = cv2.merge([B, G, R])

plt.imshow(cv2.cvtColor(reconstructed, cv2.COLOR_BGR2RGB))
plt.title("Reconstructed Color Image")
plt.axis("off")
plt.show()

# g. Write 2-D data into image file
data = np.array([
    [0, 50, 100, 150, 200, 255],
    [50, 100, 150, 200, 255, 0],
    [100, 150, 200, 255, 0, 50],
    [150, 200, 255, 0, 50, 100],
    [200, 255, 0, 50, 100, 150]
], dtype=np.uint8)

cv2.imwrite("2D_data.png", data)

print("All operations completed successfully.")

import os

path = os.path.abspath("2D_data.png")

cv2.imwrite(path, data)

print("2D image saved at:")
print(path)


# 2.  To write and execute image processing programs using point processing method:
# a. Obtain Negative image 
# b. Obtain Flip image
# c. Thresholding
# d. Contrast stretching


import cv2
import numpy as np
import sys

# Read the image
img = cv2.imread("xray.jpg", 0)

# Check if image is loaded
if img is None:
    print("Error: xray.jpg not found!")
    sys.exit()

# 1. Negative Image
negative = 255 - img

# 2. horizontal Flip
fliph = img[:, ::-1]
# vertical flip
flipv = img[::-1, :]

# 3. Thresholding
a = 127

thresholdwb = np.where(img <= a, 0, 255).astype(np.uint8)
thresholdb=np.where(img<=a, img, 255).astype(np.uint8)

# 4. Contrast Stretching
min_val = np.min(img)
max_val = np.max(img)

if max_val != min_val:
    contrast = ((img - min_val) * 255 / (max_val - min_val)).astype(np.float32)
else:
    contrast = img

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Negative Image", negative)
cv2.imshow("horizontal Flip Image", fliph)
cv2.imshow("vertical Flip Image", flipv)
cv2.imshow("Threshold Image(without bg)", thresholdwb)
cv2.imshow("Threshold Image(with bg)", thresholdb)
cv2.imshow("Contrast Stretched Image", contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. To write and execute programs for image arithmetic operations:
# a. Addition of two images 
# b. Subtract one image from other image
# c. Calculate mean value of image
# d. Different Brightness by changing mean value

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('wb.jpg')
img2 = cv2.imread('gl.jpg')

import os

print(os.getcwd())
img1 = cv2.imread(r'D:\sem 5\br-554.jpg')
img2 = cv2.imread(r'D:\sem 5\gl-554.jpg')
# Convert BGR to RGB for displaying with Matplotlib
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Add two images
addition = cv2.add(img1, img2)

plt.imshow(addition)
plt.title('Image Addition')
plt.axis('off')
plt.show()

subtraction = cv2.subtract(img1, img2)

plt.imshow(subtraction)
plt.title('Image Subtraction')
plt.axis('off')
plt.show()

# Read image as grayscale
gray = cv2.imread(r'D:\sem 5\gl-554.jpg', 0)

# Calculate mean intensity
mean_value = np.mean(gray)

print("Mean intensity:", mean_value)

# Increase brightness
bright = cv2.convertScaleAbs(gray, alpha=1, beta=50)

# Decrease brightness
dark = cv2.convertScaleAbs(gray, alpha=1, beta=-50)

# Display all three images
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(bright, cmap='gray')
plt.title('Increased Brightness')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dark, cmap='gray')
plt.title('Decreased Brightness')
plt.axis('off')

plt.show()

print("Original mean:", np.mean(gray))
print("Bright image mean:", np.mean(bright))
print("Dark image mean:", np.mean(dark))

# 4. To write and execute programs for image logical operations:
# a. AND operation between two images
# b. OR operation between two images
# c. Calculate intersection of two images
# d. Water Marking using X-OR operation 
# e. NOT operation (Negative image)


import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("br.jpg")
img2 = cv2.imread("gl.jpg")

and_img = cv2.bitwise_and(img1, img2)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(and_img, cv2.COLOR_BGR2RGB))
plt.title("AND Operation")
plt.axis("off")
plt.show()

or_img = cv2.bitwise_or(img1, img2)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(or_img, cv2.COLOR_BGR2RGB))
plt.title("OR Operation")
plt.axis("off")

plt.show()

intersection = cv2.bitwise_and(img1, img2)

plt.imshow(cv2.cvtColor(intersection, cv2.COLOR_BGR2RGB))
plt.title("Intersection of Two Images")
plt.axis("off")
plt.show()

image = cv2.imread("gl.jpg")
watermark = cv2.imread("wm.jpg")

# Resize watermark to the same size as the image
watermark = cv2.resize(watermark, (image.shape[1], image.shape[0]))

xor_img = cv2.bitwise_xor(image, watermark)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(watermark, cv2.COLOR_BGR2RGB))
plt.title("Watermark")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(xor_img, cv2.COLOR_BGR2RGB))
plt.title("XOR Watermarked Image")
plt.axis("off")
plt.show()

img = cv2.imread("gl.jpg")

negative = 255 - img

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative, cv2.COLOR_BGR2RGB))
plt.title("Negative Image")
plt.axis("off")

plt.show()


# 5. To write and execute a program for histogram calculation and equalization:
# a.Using inbuilt function
# b.Without using inbuilt function


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("xray2.jpg", cv2.IMREAD_GRAYSCALE)

# Calculate histogram using OpenCV
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogram equalization
equalized = cv2.equalizeHist(img)

# Display original and equalized images
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")
plt.axis("off")

# Original histogram
plt.subplot(2, 2, 3)
plt.plot(hist)
plt.title("Original Histogram")
plt.xlim([0, 256])

# Equalized histogram
hist_eq = cv2.calcHist([equalized], [0], None, [256], [0, 256])
plt.subplot(2, 2, 4)
plt.plot(hist_eq)
plt.title("Equalized Histogram")
plt.xlim([0, 256])

plt.tight_layout()
plt.show()

# 2nd method

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:19:46 2026

@author: kriti
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("xray2.jpg", cv2.IMREAD_GRAYSCALE)

# Create histogram with 256 intensity levels
hist = np.zeros(256, dtype=int)

# Calculate histogram manually
for pixel in img.flatten():
    hist[pixel] += 1

# Display histogram
plt.plot(hist)
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.show()

# Number of intensity levels
L = 256

# Step 1: Calculate histogram manually
hist = np.zeros(L, dtype=int)

for pixel in img.flatten():
    hist[pixel] += 1

# Step 2: Calculate cumulative histogram (CDF)
cdf = np.zeros(L, dtype=int)
cdf[0] = hist[0]

for i in range(1, L):
    cdf[i] = cdf[i - 1] + hist[i]

# Step 3: Find minimum non-zero CDF
cdf_min = cdf[np.nonzero(cdf)][0]

# Total number of pixels
total_pixels = img.size

# Step 4: Create transformation table
mapping = np.zeros(L, dtype=np.uint8)

for i in range(L):
    mapping[i] = round(
        ((cdf[i] - cdf_min) / (total_pixels - cdf_min)) * (L - 1)
    )

# Step 5: Apply transformation
equalized = mapping[img]

# Display images
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.plot(hist)
plt.title("Original Histogram")

# Calculate equalized histogram manually
hist_eq = np.zeros(L, dtype=int)

for pixel in equalized.flatten():
    hist_eq[pixel] += 1

plt.subplot(2, 2, 4)
plt.plot(hist_eq)
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()


# 6. To write and execute a program performing the following geometric transformations on 
# an image:
# a.Translation 
# b.Scaling 
# c.Rotation 
# d.Shrinking 
# e.Zooming 

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\sem 5\xray2.jpg")

rows, cols = img.shape[:2]
#translation
tx = 100
ty = 50

M = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

translated = cv2.warpAffine(img, M, (cols, rows))

plt.imshow(cv2.cvtColor(translated, cv2.COLOR_BGR2RGB))
plt.title("Translated Image")
plt.axis("off")
plt.show()

#scaling
scaled = cv2.resize(
    img,
    None,
    fx=4,
    fy=4,
    interpolation=cv2.INTER_LINEAR
)

plt.imshow(cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB))
plt.title("Scaled Image")
plt.axis("off")
plt.show()

#rotation
rows, cols = img.shape[:2]

center = (cols // 2, rows // 2)

M = cv2.getRotationMatrix2D(
    center,
    45,
    1
)

rotated = cv2.warpAffine(
    img,
    M,
    (cols, rows)
)

plt.imshow(cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB))
plt.title("Rotated Image")
plt.axis("off")
plt.show()

#shrunking

shrunk = cv2.resize(
    img,
    None,
    fx=0.2,
    fy=0.2,
    interpolation=cv2.INTER_AREA
)

plt.imshow(cv2.cvtColor(shrunk, cv2.COLOR_BGR2RGB))
plt.title("Shrunk Image")
plt.axis("off")
plt.show()

#zooming
zoomed = cv2.resize(
    img,
    None,
    fx=8,
    fy=8,
    interpolation=cv2.INTER_CUBIC
)

plt.imshow(cv2.cvtColor(zoomed, cv2.COLOR_BGR2RGB))
plt.title("Zoomed Image")
plt.axis("off")
plt.show()


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f"Original: {img.shape[1]} × {img.shape[0]}")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB))
plt.title(f"Scaled: {scaled.shape[1]} × {scaled.shape[0]}")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(shrunk, cv2.COLOR_BGR2RGB))
plt.title(f"Shrunk: {shrunk.shape[1]} × {shrunk.shape[0]}")
plt.axis("off")

plt.tight_layout()
plt.show()

#  7. To understand various image noise models and to write programs for:
# a. Image restoration 
# b. Remove Salt and Pepper Noise
# c. Minimize Gaussian noise
# d. Median filter and Weiner filter


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
img = cv2.imread(r'D:\sem 5\gl-554.jpg', 0)

# Check image
if img is None:
    raise FileNotFoundError("Image not found. Check the path.")

# Add salt and pepper noise
noisy = img.copy()

prob = 0.05
random = np.random.random(img.shape)

noisy[random < prob/2] = 0
noisy[random > 1-prob/2] = 255

# Apply median filter
restored = cv2.medianBlur(noisy, 3)

# Display
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(noisy, cmap='gray')
plt.title('Salt and Pepper Noise')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(restored, cmap='gray')
plt.title('Median Filter')
plt.axis('off')

plt.show()

# Convert to float
img_float = img.astype(np.float32)

# Generate Gaussian noise
mean = 0
sigma = 20

noise = np.random.normal(mean, sigma, img.shape)

# Add noise
noisy = img_float + noise

# Clip values to 0-255
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# Apply Gaussian filter
restored = cv2.GaussianBlur(noisy, (5,5), 1.0)

# Display
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(noisy, cmap='gray')
plt.title('Gaussian Noise')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(restored, cmap='gray')
plt.title('Gaussian Filter')
plt.axis('off')

plt.show()

pip install scipy
from scipy.signal import wiener
# Add Gaussian noise
sigma = 20
noise = np.random.normal(0, sigma, img.shape)

noisy = img.astype(np.float32) + noise
noisy = np.clip(noisy, 0, 255)

# Apply Wiener filter
restored = wiener(noisy, mysize=(5,5), noise=sigma**2)

# Clip output
restored = np.clip(restored, 0, 255).astype(np.uint8)

# Display
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(noisy, cmap='gray')
plt.title('Noisy Image')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(restored, cmap='gray')
plt.title('Wiener Filter')
plt.axis('off')

plt.show()

# 8. Write and execute programs to remove noise from images using spatial filtering.
# a. Understand 1-D and 2-D convolution process
# b. Use 3x3 Mask for low pass filter and high pass filter

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 18:35:40 2026

@author: kriti
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the image in grayscale
img = cv2.imread(r'D:\sem 5\gl-554.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found. Check the image path.")

# 2. Add Gaussian noise
gaussian_noise = np.random.normal(0, 20, img.shape)
gaussian_noisy = np.clip(
    img.astype(np.float32) + gaussian_noise, 0, 255
).astype(np.uint8)

# 3. Add salt-and-pepper noise
sp_noisy = img.copy()

# Randomly select pixels
random_values = np.random.random(img.shape)

# Salt: white pixels
sp_noisy[random_values < 0.02] = 255

# Pepper: black pixels
sp_noisy[random_values > 0.98] = 0

# 4. Define a 3x3 low-pass averaging mask
low_pass = np.ones((3, 3), dtype=np.float32) / 9

# Apply low-pass filter to Gaussian noisy image
low_pass_result = cv2.filter2D(
    gaussian_noisy, -1, low_pass
)

# 5. Define a 3x3 high-pass mask
high_pass = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

# Apply high-pass filter
high_pass_result = cv2.filter2D(
    img, cv2.CV_32F, high_pass
)

# Convert response to a displayable image
high_pass_display = cv2.convertScaleAbs(high_pass_result)

# 6. Apply median filter to remove salt-and-pepper noise
median_result = cv2.medianBlur(sp_noisy, 3)

# 7. Apply Gaussian smoothing
gaussian_result = cv2.GaussianBlur(
    gaussian_noisy, (3, 3), 0
)

# 8. Display all results
images = [
    img,
    gaussian_noisy,
    low_pass_result,
    gaussian_result,
    sp_noisy,
    median_result,
    high_pass_display
]

titles = [
    "Original Image",
    "Gaussian Noisy Image",
    "Low-Pass Filter",
    "Gaussian Filter",
    "Salt-and-Pepper Noise",
    "Median Filter",
    "High-Pass Filter"
]

plt.figure(figsize=(14, 9))

for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()


import numpy as np

# Input signal
signal = np.array([1, 2, 3, 4, 5])

# 1-D averaging kernel
kernel = np.array([1/3, 1/3, 1/3])

# Perform convolution
result = np.convolve(signal, kernel, mode="valid")

print("Input signal:", signal)
print("Kernel:", kernel)
print("Convolution output:", result)

# 9. Write and execute programs for image frequency domain filtering.
# a. Apply FFT on given image 
# b. Perform low pass and high pass filtering in frequency domain 
# c. Apply IFFT to reconstruct image



import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the image in grayscale
img = cv2.imread(r"D:\sem 5\gl-554.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found. Check the image path.")

# 2. Apply 2-D FFT
fft = np.fft.fft2(img)

# 3. Shift zero frequency to the centre
fft_shift = np.fft.fftshift(fft)

# 4. Calculate magnitude spectrum
magnitude = 20 * np.log(1 + np.abs(fft_shift))

# 5. Create circular low-pass and high-pass masks
rows, cols = img.shape

crow = rows // 2
ccol = cols // 2

# Calculate distance of every frequency from the centre
x, y = np.ogrid[:rows, :cols]
distance = np.sqrt((x - crow)**2 + (y - ccol)**2)

# Cutoff frequency
D0 = 40

# Low-pass mask
low_mask = (distance <= D0).astype(np.float32)

# High-pass mask
high_mask = (distance > D0).astype(np.float32)

# 6. Apply masks to the shifted Fourier transform
low_pass_fft = fft_shift * low_mask
high_pass_fft = fft_shift * high_mask

# 7. Apply inverse FFT to reconstruct images

# Low-pass reconstruction
low_ifft_shift = np.fft.ifftshift(low_pass_fft)
low_reconstructed = np.fft.ifft2(low_ifft_shift)
low_reconstructed = np.abs(low_reconstructed)

# High-pass reconstruction
high_ifft_shift = np.fft.ifftshift(high_pass_fft)
high_reconstructed = np.fft.ifft2(high_ifft_shift)
high_reconstructed = np.abs(high_reconstructed)

# 8. Normalize reconstructed images for display
low_display = np.clip(low_reconstructed, 0, 255).astype(np.uint8)

high_display = cv2.normalize(
    high_reconstructed,
    None,
    0,
    255,
    cv2.NORM_MINMAX
).astype(np.uint8)

# 9. Display results
plt.figure(figsize=(14, 10))

plt.subplot(3, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(3, 3, 2)
plt.imshow(magnitude, cmap="gray")
plt.title("FFT Magnitude Spectrum")
plt.axis("off")

plt.subplot(3, 3, 3)
plt.imshow(low_mask, cmap="gray")
plt.title("Low-Pass Mask")
plt.axis("off")

plt.subplot(3, 3, 4)
plt.imshow(high_mask, cmap="gray")
plt.title("High-Pass Mask")
plt.axis("off")

plt.subplot(3, 3, 5)
plt.imshow(low_display, cmap="gray")
plt.title("Low-Pass Filtered Image")
plt.axis("off")

plt.subplot(3, 3, 6)
plt.imshow(high_display, cmap="gray")
plt.title("High-Pass Filtered Image")
plt.axis("off")

plt.subplot(3, 3, 7)
plt.imshow(20 * np.log(1 + np.abs(low_pass_fft)), cmap="gray")
plt.title("Low-Pass Frequency Spectrum")
plt.axis("off")

plt.subplot(3, 3, 8)
plt.imshow(20 * np.log(1 + np.abs(high_pass_fft)), cmap="gray")
plt.title("High-Pass Frequency Spectrum")
plt.axis("off")

plt.tight_layout()
plt.show()

#    10. Write and execute a program for edge detection using different edge detection mask.


import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read image in grayscale
img = cv2.imread(r"D:\sem 5\gl-554.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found. Check the image path.")

# Convert image to float32
img_float = img.astype(np.float32)


# 2. Define Roberts masks (2x2)
roberts_x = np.array([
    [1, 0],
    [0, -1]
], dtype=np.float32)

roberts_y = np.array([
    [0, 1],
    [-1, 0]
], dtype=np.float32)

# Apply Roberts masks
rx = cv2.filter2D(img_float, cv2.CV_32F, roberts_x)
ry = cv2.filter2D(img_float, cv2.CV_32F, roberts_y)

# Calculate Roberts edge magnitude
roberts = np.sqrt(rx**2 + ry**2)


# 3. Define Prewitt masks (3x3)
prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

prewitt_y = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=np.float32)

# Apply Prewitt masks
px = cv2.filter2D(img_float, cv2.CV_32F, prewitt_x)
py = cv2.filter2D(img_float, cv2.CV_32F, prewitt_y)

# Calculate Prewitt edge magnitude
prewitt = np.sqrt(px**2 + py**2)


# 4. Define Sobel masks (3x3)
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.float32)

sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
], dtype=np.float32)

# Apply Sobel masks
sx = cv2.filter2D(img_float, cv2.CV_32F, sobel_x)
sy = cv2.filter2D(img_float, cv2.CV_32F, sobel_y)

# Calculate Sobel edge magnitude
sobel = np.sqrt(sx**2 + sy**2)


# 5. Define Laplacian mask (3x3)
laplacian_mask = np.array([
    [ 0,  1,  0],
    [ 1, -4,  1],
    [ 0,  1,  0]
], dtype=np.float32)

# Apply Laplacian mask
laplacian = cv2.filter2D(
    img_float, cv2.CV_32F, laplacian_mask
)

# Take absolute value for display
laplacian = np.abs(laplacian)


# 6. Normalize results for display
def normalize_image(image):
    return cv2.normalize(
        image, None, 0, 255, cv2.NORM_MINMAX
    ).astype(np.uint8)


roberts_display = normalize_image(roberts)
prewitt_display = normalize_image(prewitt)
sobel_display = normalize_image(sobel)
laplacian_display = normalize_image(laplacian)


# 7. Display results
images = [
    img,
    roberts_display,
    prewitt_display,
    sobel_display,
    laplacian_display
]

titles = [
    "Original Image",
    "Roberts Edge Detection",
    "Prewitt Edge Detection",
    "Sobel Edge Detection",
    "Laplacian Edge Detection"
]

plt.figure(figsize=(12, 8))

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()


# 11. Write and execute a program for image morphological operations erosion and dilation


import cv2
import numpy as np

img = np.zeros((9, 9), dtype=np.uint8)
img[2:7, 2:7] = 1  
img[1, 1] = 1      

kernel = np.ones((3, 3), dtype=np.uint8)

eroded = cv2.erode(img, kernel, iterations=1)
dilated = cv2.dilate(img, kernel, iterations=1)

print("Original Image (9x9):\n", img)
print("\nErosion (3x3 kernel):\n", eroded)
print("\nDilation(3x3 kernel):\n", dilated)
print("\nForeground pixel count -> Original:", np.sum(img), 
      "| Eroded:", np.sum(eroded), 
      "| Dilated:", np.sum(dilated))