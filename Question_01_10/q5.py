import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    img = plt.imread('imori.jpg')
    gray = (0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]).astype(np.uint8)
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    max_channel = img.max(axis=2)
    min_channel = img.min(axis=2)

    S = max_channel - min_channel
    V = max_channel

    H = None
    if (min_channel == max_channel).all():
        H = 0
    elif (min_channel == B).all():
        H = 60 * ((G - R) / S) + 60
    elif (min_channel == R).all():
        H = 60 * ((B - G) / S) + 180
    else:
        H = 60 * ((R - B) / S) + 300

    hsv = np.dstack([H, S, V])

    rgb = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
    ax1.imshow(gray, cmap='gray')
    ax2.set_title("original")
    ax1.set_title("hsv")
    ax2.imshow(V, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
