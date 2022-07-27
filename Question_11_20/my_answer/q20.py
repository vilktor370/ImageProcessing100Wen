import matplotlib.pyplot as plt
import numpy as np


def main():
    img = plt.imread('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/imori_dark.jpg').astype(np.float32)

    plt.hist(img.ravel(), bins=255, rwidth=0.9)
    plt.savefig('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/my_output/20_histogram.png')
    plt.show()


if __name__ == '__main__':
    main()
