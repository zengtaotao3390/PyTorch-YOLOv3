import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from utils.utils import *


def getBoxes():
    boxes = []
    with open('label.txt') as labelFile:
        for line in labelFile.readlines():
            attribures = line.split()
            boxes.append(float(attribures[1]))
            boxes.append(float(attribures[2]))
            boxes.append(float(attribures[3]))
            boxes.append(float(attribures[4]))
    return np.reshape(boxes, (int(len(boxes) / 4), 4))


def rescale_boxes(boxes, original_shape):
    """ Rescales bounding boxes to the original shape """
    print(boxes)
    orig_h, orig_w = original_shape
    boxes[:, 0] = (2 *  boxes[:, 0] - boxes[:, 2]) / 2 * orig_w
    boxes[:, 1] = (2 *  boxes[:, 1] - boxes[:, 3]) / 2 * orig_h
    boxes[:, 2] = boxes[:, 2] * orig_w
    boxes[:, 3] = boxes[:, 3] * orig_h

    return boxes


if __name__ == '__main__':
    boxes = getBoxes()
    img = np.array(Image.open('image.jpg'))
    plt.figure()
    fig, ax = plt.subplots(1)
    ax.imshow(img)
    boxes = rescale_boxes(boxes, img.shape[:2])
    for x1, y1, boxW, boxH in boxes:
        bbox = patches.Rectangle((x1, y1), boxW, boxH, linewidth=2, edgecolor='red', facecolor="none")
        print(bbox)
        ax.add_patch(bbox)
    plt.show()

