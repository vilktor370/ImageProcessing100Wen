import matplotlib.pyplot as plt
import numpy as np


def normalize(img):
    a, b = 0, 255
    c, d = img.min(), img.max()
    out = (b - a) / (d - c) * (img - c) + a
    out[out < a] = a
    out[out > b] = b
    return out.astype(np.uint8)


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori_dark.jpg')
    normalize_img = normalize(img)
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12), facecolor='white')
    ax1.hist(img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax2.hist(normalize_img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax3.imshow(img)
    ax4.imshow(normalize_img)
    plt.savefig('output/q21.png')
    plt.show()


if __name__ == '__main__':
    main()
