import matplotlib.pyplot as plt
import numpy as np
import cv2


def get_affine_transform_mtx(tx=30, ty=-30, new_x_ratio=1.3, new_y_ratio=0.8) -> np.ndarray:
    """
    Affine transform matrix:
    ⌈ a  b  tx ⌉
    | c  d  ty |
    ⌊ 0  0  1  ⌋


    :param tx:
    :param ty:
    :return:
    """
    affine_mtx = np.eye(3)
    affine_mtx[0, -1] = tx
    affine_mtx[1, -1] = ty
    affine_mtx[0, 0] = new_x_ratio
    affine_mtx[1, 1] = new_y_ratio
    return affine_mtx


def affie_transform(img, tx=30, ty=-30, new_x_ratio=1.3, new_y_ratio=0.8):
    H, W, C = img.shape
    new_H = int(H * new_y_ratio)
    new_W = int(W * new_x_ratio)
    out = np.zeros((new_H, new_W, C), dtype=img.dtype)
    for y in range(H):
        for x in range(W):
            for c in range(C):
                new_x = int(new_x_ratio * x + tx)
                new_y = int(new_y_ratio * y + ty)
                if new_x >= new_W or new_x < 0:
                    continue
                if new_y >= new_H or new_y < 0:
                    continue
                out[new_y, new_x, c] = img[y, x, c]

    out = out.astype(np.uint8)
    return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori.jpg')
    mine = affie_transform(img, new_x_ratio=1.3, new_y_ratio=0.8, tx=30, ty=-30)

    # opencv check
    affine_mtx = np.array([[1.3, 0, 30], [0, 0.8, -30]])
    H, W, C = img.shape
    new_H = int(H * 1.3)
    new_W = int(W * 0.8)

    out = cv2.warpAffine(img.astype(np.float64), affine_mtx.astype(np.float64), (new_H, new_W))
    out = out.astype(np.uint8)
    plt.imsave('output/q_29_resized.png', mine)
    plt.imsave('output/q_29_original.png', img)
    plt.imsave('output/q_29_opencv.png', out)


if __name__ == '__main__':
    main()
