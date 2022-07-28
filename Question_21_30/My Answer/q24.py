import matplotlib.pyplot as plt
import numpy as np


def gamma_correction(img, c=1, g=2.2):
    out = (1 / c) * img ** (1 / g)
    return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori_gamma.jpg').astype(
        np.float64) / 255.0
    out = (gamma_correction(img) * 255).astype(np.uint8)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 12), facecolor='white')
    ax1.imshow(img)
    ax1.set_title('original', fontsize=20)
    ax2.set_title('gamma correction', fontsize=20)
    ax2.imshow(out)
    plt.savefig('output/q24.png')
    plt.show()


if __name__ == '__main__':
    main()
