import matplotlib.pyplot as plt
import numpy as np


def my_convolve(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    H, W, C = img.shape
    k = kernel.shape[0]

    pad = k // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float64)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float64)
    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = (tmp[y: y + k, x: x + k, c] * kernel).sum()

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out


def main():
    img = plt.imread('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/imori.jpg')
    kernel = np.ones((3, 3)) / 9  # average filter
    out = my_convolve(img, kernel)
    plt.imshow(out)
    plt.imsave('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/my_output/11.png', out)
    plt.show()


if __name__ == '__main__':
    main()
