import cv2
import matplotlib.pyplot as plt

def show(img, code=cv2.COLOR_BGR2RGB):
    cv_rgb = cv2.cvtColor(img, code)
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.imshow(cv_rgb)
    fig.show()

img = cv2.imread('1.jpg')
show(img)

if __name__ == '__main__':
    img_path = 'data/shape.jpg'
    img = cv2.imread(img_path)
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 100, 200)

    edges, contours, hierarchy = cv2.findContours(edges, mode=cv2.RETR_TREE,
                                                method=cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    print(hierarchy.shape)
    print(len(contours))

    found = []

    for i in range(len(contours)):
        k = i
        c = 0
        print(i)
        while hierarchy[k][2] != -1:
            print(hierarchy[k])
            k = hierarchy[k][2]
            c += 1
            print('-1')
        if c >= 5:
            found.append(i)


    for i in found:
        img = cv2.drawContours(img, contours, i, (255, 0, 0), 1)  # 标记处编号为0的轮廓
        show(img)

    plt.imshow(img)
    plt.show()
    cv2.imshow('drawimg', img)
    cv2.waitKey()
    # plt.subplot(1,2,1), plt.imshow(img)
    # plt.subplot(1,2,2), plt.imshow(image)
    # plt.show()