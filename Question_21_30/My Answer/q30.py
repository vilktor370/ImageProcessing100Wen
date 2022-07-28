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
    A = 30
    theta = -np.pi * A / 180
    affine_mtx = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return affine_mtx


def affie_transform(img, tx=30, ty=-30, new_x_ratio=1.3, new_y_ratio=0.8):
    H, W, C = img.shape

    # create xy index array of the old image coordinates
    y = np.arange(H).repeat(W)[:, None]
    x = np.tile(np.arange(H), W)[:, None]
    xy_homo = np.hstack([x, y, np.ones((x.shape[0], 1))])

    # get affine transform matrix
    affine_mtx = get_affine_transform_mtx(tx, ty)

    # apply transform
    new_xy_homo = affine_mtx.dot(xy_homo.T)

    # split xy_homo array into x,y
    new_xy = new_xy_homo.T[:, :2].astype(np.uint8)
    new_x, new_y = new_xy[:, 0][:, None], new_xy[:, 1][:, None]

    # take care of corner cases
    new_x[new_x > (W - 1)] = W - 1
    new_y[new_y > (H - 1)] = H - 1

    # copy old pixel value to the new image
    out = np.zeros_like(img)
    out[new_y, new_x, :] = img[y, x, :]
    return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori.jpg')
    mine = affie_transform(img, new_x_ratio=1.3, new_y_ratio=0.8, tx=30, ty=-30)

    # opencv check
    A = 30
    theta = -np.pi * A / 180
    affine_mtx = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0]])
    H, W, C = img.shape

    out = cv2.warpAffine(img.astype(np.float64), affine_mtx.astype(np.float64), (H, W))
    out = out.astype(np.uint8)
    plt.imsave('output/q_30_resized.png', mine)
    plt.imsave('output/q_30_original.png', img)
    plt.imsave('output/q_30_opencv.png', out)


if __name__ == '__main__':
    main()
