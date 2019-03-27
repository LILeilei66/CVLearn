import cv2

if __name__ == '__main__':
    img_path = 'data/000000.png'
    img_path = 'data/000026.png'
    img = cv2.imread(img_path)

    hog = cv2.HOGDescriptor()
    kp = hog.compute(img)
    print(img.shape)
    print(kp)
    print(len(kp))
    img = cv2.drawKeypoints(img, kp, img)
    cv2.imshow(img)
    cv2.waitKey()
