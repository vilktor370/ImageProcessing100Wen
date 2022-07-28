import matplotlib.pyplot as plt
import numpy as np
import cv2


def get_affine_transform_mtx(tx=30, ty=-30) -> np.ndarray:
    """
    Affine transform matrix:
    ⌈ a  b  tx ⌉
    | b  a  ty |
    ⌊ 0  0  1  ⌋


    :param tx:
    :param ty:
    :return:
    Only translation
    ⌈ 1  0  ty ⌉
    | 0  1  tx |
    ⌊ 0  0  1  ⌋
    """
    affine_mtx = np.eye(3)
    affine_mtx[0, -1] = ty
    affine_mtx[1, -1] = tx
    return affine_mtx


def affie_transform(img, tx=30, ty=-30):
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
    out[new_x, new_y, :] = img[x, y, :]

    return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori.jpg')
    out = affie_transform(img)
    plt.imsave('output/q_28_resized.png', out)
    plt.imsave('output/q_28_original.png', img)


if __name__ == '__main__':
    main()
