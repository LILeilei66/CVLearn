import cv2

if __name__ == '__main__':
    img_path = 'data/000000.png'
    img_path = 'data/000026.png'
    img = cv2.imread(img_path)

    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(img, None)

    img= cv2.drawKeypoints(img, kp, img)
    cv2.imshow('img', img)
    cv2.waitKey()