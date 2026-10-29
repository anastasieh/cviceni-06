# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.io import imread
# from skimage.util import img_as_float
# from skimage.color import rgb2gray
# from scipy.io import loadmat
# from scipy.signal import convolve2d, medfilt2d
# from scipy.ndimage import gaussian_filter
# from skimage.util import random_noise
# from numpy.fft import fft2, fftshift
#
# plt.close('all')
#
# # Ukol 1
# # =============================================================================
# # Zobrazte si jasovy profil hrany ulozene v promenne "img" na libovolnem radku
# # Vytvorte 1. a 2. parcialni derivaci puvodniho obrazu a zobrazte je spolu s jasovymi profily
# # =============================================================================
# mat = loadmat('data/hrana.mat')
# img = mat.get('a')
#
# profile = ...
#
# plt.figure()
# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('Originalni obraz')
# plt.subplot(1, 2, 2)
# plt.plot(profile)
# plt.title('Jasovy profil')
# plt.show()
#
# first_h = np.array([[0, 0, 0], [0, 1, -1], [0, 0, 0]])
# filtered_by_1st = ...
# profile_1st = filtered_by_1st[50, :]
#
# second_h = np.array([[0, 0, 0], [1, -2, 1], [0, 0, 0]])
# filtered_by_2nd = ...
# profile_2nd = filtered_by_2nd[50, :]
#
# plt.figure()
# plt.subplot(2, 3, 1)
# plt.imshow(img, cmap='gray')
# plt.title('Originalni obraz')
# plt.subplot(2, 3, 4)
# plt.plot(profile)
# plt.title('Jasovy profil originalu')
# plt.subplot(2, 3, 2)
# plt.imshow(filtered_by_1st, cmap='gray')
# plt.title('Prvni derivace')
# plt.subplot(2, 3, 5)
# plt.plot(profile_1st)
# plt.title('Jasovy profil prvni derivace')
# plt.subplot(2, 3, 3)
# plt.imshow(filtered_by_2nd, cmap='gray')
# plt.title('Druha derivace')
# plt.subplot(2, 3, 6)
# plt.plot(profile_2nd)
# plt.title('Jasovy profil druhe derivace')
# plt.show()
#
#
# # Ukol 2
# # =============================================================================
# # Vyfiltrujte obraz ‘hrana.mat‘ pomoci vybraneho zostrujiciho operatoru
# # Prozkoumejte funkci GetProfileWidth
# # Overte funkcnost filtrace jak zobrazenim vyfiltrovanych obrazu a odpovidajicich jasovych profilu, tak vypoctenim a porovnanim sirek profilu hran
# # Mente parametr K nebo alfa a pozorujte, jak se s vysledny obraz a jasove profily hrany meni
# # Nactete obraz ‘MRI_brain.jpg’ a filtrujte jej pomoci Laplaceova operatoru. Zobrazte vyslednou aproximaci Laplacianu
# # Zostrete obraz MRI s vyuzitim ziskaneho Laplacianu.
# # =============================================================================
# img = rgb2gray(img_as_float(imread('data/MRI_brain.jpg')))
#
# def GetProfileWidth(edge_profile):
#     max_intensity = np.max(edge_profile)
#     bottom = max_intensity * 0.1
#     top = max_intensity * 0.9
#     bottom_position = (np.abs(edge_profile - bottom)).argmin()
#     top_position = (np.abs(edge_profile - top)).argmin()
#     profile_width = top_position - bottom_position
#     return (profile_width)
#
#
# K = 0.2
# F = np.zeros((3, 3))
# F[1, 1] = K
#
# L = np.ones((3, 3))
# L[1, 1] = -8
#
# sharpening_operator = (F + (-L)) / K
# sharpened_by_2nd = ...
#
# # Overte funkcnost filtrace jak zobrazenim vyfiltrovanych obrazu a odpovidajicich jasovych profilu, tak vypoctenim a porovnanim sirek profilu hran
# profile_sharpened_2nd = ...
# width_2nd = GetProfileWidth(profile_sharpened_2nd)
# width_orig = GetProfileWidth(profile)
#
# print(['Sirka originalu:', width_orig, 'Sirka po filtraci s vyuzitim druhe derivace:', width_2nd])
#
# plt.figure()
# plt.subplot(2, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('Originalni obraz')
# plt.subplot(2, 2, 3)
# plt.plot(profile)
# plt.title('Jasovy profil originalu')
#
# plt.subplot(2, 2, 2)
# plt.imshow(sharpened_by_2nd, cmap='gray')
# plt.title('Zostreny obraz')
# plt.subplot(2, 2, 4)
# plt.plot(profile_sharpened_2nd)
# plt.title('Jasovy profil zostreneho obrazu')
# plt.show()
#
# L = np.ones((3, 3))
# L[1, 1] = -8
# laplacian = ...
#
# sharpened_img = ...
#
# plt.figure()
# plt.subplot(1, 3, 1)
# plt.imshow(img, vmin=0, vmax=1, cmap='gray')
# plt.title('Original')
# plt.subplot(1, 3, 2)
# plt.imshow(laplacian, vmin=-1, vmax=1, cmap='gray')
# plt.title('Laplacian')
# plt.subplot(1, 3, 3)
# plt.imshow(sharpened_img, vmin=0, vmax=1, cmap='gray')
# plt.title('Zostreny Laplaceovym operatorem')
# plt.show()
#
# # Ukol 3
# # =============================================================================
# # Načtěte obraz ‘ugly_quidditch.jpg’
# # Zobrazte si obraz spolu s jeho histogramem a spektrem
# # Aplikutje na obraz vhodnou filtraci na odstranění přítomného šumu
# # Na vyfiltrovaný obraz použijte vhodnou transformaci kontrastu
# # Na vyfiltrovaný obraz po transformaci kontrastu použijte vhodný operátor a zvýrazněte hrany v obraze
# # =============================================================================
#
# # Načtěte obraz ‘ugly_quidditch.jpg’
# img = img_as_float(imread('data/ugly_quidditch.png'))
#
#
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.util import img_as_float
from skimage.color import rgb2gray
from scipy.io import loadmat
from scipy.signal import convolve2d, medfilt2d
from scipy.ndimage import gaussian_filter
from skimage.util import random_noise
from numpy.fft import fft2, fftshift

plt.close('all')

# Ukol 1
# =============================================================================
# Zobrazte si jasovy profil hrany ulozene v promenne "img" na libovolnem radku
# Vytvorte 1. a 2. parcialni derivaci puvodniho obrazu a zobrazte je spolu s jasovymi profily
# =============================================================================
mat = loadmat('data/hrana.mat')
img = mat.get('a')

profile = img[50, :]

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Originalni obraz')
plt.subplot(1, 2, 2)
plt.plot(profile)
plt.title('Jasovy profil')
plt.show()

first_h = np.array([[0, 0, 0], [0, 1, -1], [0, 0, 0]])
filtered_by_1st = convolve2d(img, first_h, mode='same')
profile_1st = filtered_by_1st[50, :]

second_h = np.array([[0, 0, 0], [1, -2, 1], [0, 0, 0]])
filtered_by_2nd = convolve2d(img, second_h, mode='same')
profile_2nd = filtered_by_2nd[50, :]

plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Originalni obraz')
plt.subplot(2, 3, 4)
plt.plot(profile)
plt.title('Jasovy profil originalu')
plt.subplot(2, 3, 2)
plt.imshow(filtered_by_1st, cmap='gray')
plt.title('Prvni derivace')
plt.subplot(2, 3, 5)
plt.plot(profile_1st)
plt.title('Jasovy profil prvni derivace')
plt.subplot(2, 3, 3)
plt.imshow(filtered_by_2nd, cmap='gray')
plt.title('Druha derivace')
plt.subplot(2, 3, 6)
plt.plot(profile_2nd)
plt.title('Jasovy profil druhe derivace')
plt.show()


# Ukol 2
# =============================================================================
# Vyfiltrujte obraz ‘hrana.mat‘ pomoci vybraneho zostrujiciho operatoru
# Prozkoumejte funkci GetProfileWidth
# Overte funkcnost filtrace jak zobrazenim vyfiltrovanych obrazu a odpovidajicich jasovych profilu, tak vypoctenim a porovnanim sirek profilu hran
# Mente parametr K nebo alfa a pozorujte, jak se s vysledny obraz a jasove profily hrany meni
# Nactete obraz ‘MRI_brain.jpg’ a filtrujte jej pomoci Laplaceova operatoru. Zobrazte vyslednou aproximaci Laplacianu
# Zostrete obraz MRI s vyuzitim ziskaneho Laplacianu.
# =============================================================================
img = rgb2gray(img_as_float(imread('data/MRI_brain.jpg')))

def GetProfileWidth(edge_profile):
    max_intensity = np.max(edge_profile)
    bottom = max_intensity * 0.1
    top = max_intensity * 0.9
    bottom_position = (np.abs(edge_profile - bottom)).argmin()
    top_position = (np.abs(edge_profile - top)).argmin()
    profile_width = top_position - bottom_position
    return profile_width


K = 0.2
F = np.zeros((3, 3))
F[1, 1] = K

L = np.ones((3, 3))
L[1, 1] = -8

sharpening_operator = (F + (-L)) / K
sharpened_by_2nd = convolve2d(img, sharpening_operator, mode='same')

profile_sharpened_2nd = sharpened_by_2nd[50, :]
profile_orig = img[50, :]

width_2nd = GetProfileWidth(profile_sharpened_2nd)
width_orig = GetProfileWidth(profile_orig)

print(['Sirka originalu:', width_orig,
       'Sirka po filtraci s vyuzitim druhe derivace:', width_2nd])

plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Originalni obraz')
plt.subplot(2, 2, 3)
plt.plot(profile_orig)
plt.title('Jasovy profil originalu')

plt.subplot(2, 2, 2)
plt.imshow(sharpened_by_2nd, cmap='gray')
plt.title('Zostreny obraz')
plt.subplot(2, 2, 4)
plt.plot(profile_sharpened_2nd)
plt.title('Jasovy profil zostreneho obrazu')
plt.show()

L = np.ones((3, 3))
L[1, 1] = -8
laplacian = convolve2d(img, L, mode='same')

sharpened_img = img - laplacian

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(img, vmin=0, vmax=1, cmap='gray')
plt.title('Original')
plt.subplot(1, 3, 2)
plt.imshow(laplacian, vmin=-1, vmax=1, cmap='gray')
plt.title('Laplacian')
plt.subplot(1, 3, 3)
plt.imshow(sharpened_img, vmin=0, vmax=1, cmap='gray')
plt.title('Zostreny Laplaceovym operatorem')
plt.show()


# Ukol 3
# =============================================================================
# Načtěte obraz ‘ugly_quidditch.jpg’
# Zobrazte si obraz spolu s jeho histogramem a spektrem
# Aplikutje na obraz vhodnou filtraci na odstranění přítomného šumu
# Na vyfiltrovaný obraz použijte vhodnou transformaci kontrastu
# Na vyfiltrovaný obraz po transformaci kontrastu použijte vhodný operátor a zvýrazněte hrany v obraze
# =============================================================================

img = img_as_float(imread('data/ugly_quidditch.png'))
gray = img

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Originalni obraz')
plt.subplot(1, 3, 2)
plt.hist(gray.ravel(), bins=256)
plt.title('Histogram')
plt.subplot(1, 3, 3)
spectrum = np.log(1 + np.abs(fftshift(fft2(gray))))
plt.imshow(spectrum, cmap='gray')
plt.title('Spektrum')
plt.show()

filtered_img = medfilt2d(gray, kernel_size=3)

contrast_img = (filtered_img - np.min(filtered_img)) / (
    np.max(filtered_img) - np.min(filtered_img))

edge_operator = np.array([[0, -1, 0],
                          [-1, 4, -1],
                          [0, -1, 0]])

edges = convolve2d(contrast_img, edge_operator, mode='same')

plt.figure()
plt.subplot(1, 3, 1)
plt.imshow(filtered_img, cmap='gray')
plt.title('Vyfiltrovany obraz')
plt.subplot(1, 3, 2)
plt.imshow(contrast_img, cmap='gray')
plt.title('Transformace kontrastu')
plt.subplot(1, 3, 3)
plt.imshow(edges, cmap='gray')
plt.title('Zvyraznene hrany')
plt.show()
