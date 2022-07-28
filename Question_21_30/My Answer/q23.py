import matplotlib.pyplot as plt
import numpy as np


def normalize(img, Zmax=255):
    out = img.copy()
    S = len(out.flatten())
    sum_val = 0
    for i in range(0, 255, 1):
        idx = np.where(img == i)
        sum_val += len(img[idx])
        Zprime = Zmax / S * sum_val
        out[idx] = Zprime
    return out.astype(np.uint8)


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori_dark.jpg')
    normalize_img = normalize(img)
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12), facecolor='white')
    ax1.hist(img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax2.hist(normalize_img.flatten(), bins=range(0, 255), rwidth=0.8)
    ax3.imshow(img)
    ax4.imshow(normalize_img)
    plt.savefig('output/q23.png')
    plt.show()


if __name__ == '__main__':
    main()
