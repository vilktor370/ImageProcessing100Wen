import matplotlib.pyplot as plt
import numpy as np


def normalize(img, m0=128, s0=52):
    m = img.mean()
    s = img.std()
    out = s0 / s * (img - m) + m0
    out[out < 0] = 0
    out[out > 255] = 255
    return out.astype(np.uint8)


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori_dark.jpg')
    normalize_img = normalize(img)
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12), facecolor='white')
    ax1.hist(img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax2.hist(normalize_img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax3.imshow(img)
    ax4.imshow(normalize_img)
    plt.savefig('output/q22.png')
    plt.show()


if __name__ == '__main__':
    main()
