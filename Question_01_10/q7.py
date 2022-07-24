import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    img = plt.imread('imori.jpg')
    H, W, C = img.shape
    out = img.copy()
    K = 8
    for c in range(C):
        for v in range(H // K):
            for u in range(W // K):
                out[K * v: K * (v + 1), K * u:K * (u + 1), c] = img[K * v: K * (v + 1), K * u:K * (u + 1), c].mean()
    assert out.shape == img.shape
    plt.imshow(out)
    plt.show()


if __name__ == '__main__':
    main()
