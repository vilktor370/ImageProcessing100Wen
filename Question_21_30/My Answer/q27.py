import matplotlib.pyplot as plt
import numpy as np
import cv2


def bicubic_interpolation(img, ratio=2):
    H, W = img.shape[0], img.shape[1]
    new_H, new_W = int(H * ratio), int(W * ratio)
    out = np.zeros((new_H, new_W, img.shape[2]), dtype=img.dtype)
    for k in range(3):
        for v in range(new_H):
            for u in range(new_W):

                old_u, old_v = int(u // ratio), int(v // ratio)
                if (old_v + 1) < H and (old_u + 1) < W:
                    du = u - old_u
                    dv = v - old_v
                    a = img[old_v, old_u, k]
                    b = img[old_v, old_u + 1, k]
                    c = img[old_v + 1, old_u, k]
                    d = img[old_v + 1, old_u + 1, k]

                    out[v, u, k] = a * (1 - dv) * (1 - du) + b * du * (1 - dv) + c * dv + (1 - du) + d * du * dv
        out = np.clip(out, 0, 255)
        out = out.astype(np.uint8)
        return out


def main():
    img = plt.imread(r'/home/haochen/Projects/ImageProcessing100Wen/Question_21_30/imori.jpg')
    # out = bilinear_interpolation(img)
    ratio = 10
    H, W, _ = img.shape
    H = int(H * ratio)
    W = int(W * ratio)
    out = cv2.resize(img, (H, W), cv2.INTER_CUBIC)
    plt.imsave('output/q_27_resized.png', out)
    plt.imsave('output/q_27_original.png', img)


if __name__ == '__main__':
    main()
