import matplotlib.pyplot as plt
import numpy as np
import cv2


def nearest_neighbor_interpolation(img, ratio=15):
    H, W = img.shape[0], img.shape[1]
    new_H, new_W = int(H * ratio), int(W * ratio)
    out = np.zeros((new_H, new_W, 3), dtype=img.dtype)
    for v in range(H):
        for u in range(W):
            for c in range(3):
                out[int(v * ratio):int((v + 1) * ratio), int(u * ratio):int((u + 1) * ratio), c] = img[v, u, c]

    out = out.astype(np.uint8)
    return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori.jpg')
    out = nearest_neighbor_interpolation(img)
    plt.imsave('output/q_25_resized.png', out)
    plt.imsave('output/q_25_original.png', img)
    # f, (ax1, ax2) = plt.subplots(1, 2, facecolor='white')
    # ax1.imshow(img)
    # ax1.set_title('original', fontsize=10)
    # ax2.set_title('nearest neighbor interpolation', fontsize=10)
    # ax2.imshow(out)
    # plt.savefig('output/q25.png')
    # plt.show()


if __name__ == '__main__':
    main()
