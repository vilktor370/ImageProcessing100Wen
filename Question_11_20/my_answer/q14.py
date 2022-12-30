import matplotlib.pyplot as plt
import numpy as np


def my_convolve(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    H, W = img.shape
    k = kernel.shape[0]

    pad = k // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float64)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float64)
    tmp = out.copy()

    for y in range(H):
        for x in range(W):
            out[pad + y, pad + x] = (tmp[y: y + k, x: x + k] * kernel).sum()
    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    return out


def main():
    img = plt.imread('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/imori.jpg')
    gray = (0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]).astype(np.uint8)
    K_horizontal = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
    K_vertical = np.rot90(K_horizontal, k=3)
    Ix = my_convolve(gray, K_horizontal)
    Iy = my_convolve(gray, K_vertical)
    plt.imshow(Ix, cmap='gray')
    plt.imshow(Iy, cmap='gray')
    plt.imsave('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/my_output/14_ix.png', Ix, cmap='gray')
    plt.imsave('/home/haochen/Projects/ImageProcessing100Wen/Question_11_20/my_output/14_iy.png', Iy, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()