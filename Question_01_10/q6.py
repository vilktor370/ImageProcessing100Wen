import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    img = plt.imread('imori.jpg')
    out = img.copy()
    out = out // 64 * 64 + 32

    plt.imshow(out)
    plt.show()


if __name__ == '__main__':
    main()
