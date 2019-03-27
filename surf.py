import cv2

if __name__ == '__main__':
    img_path = 'data/000000.png'
    img_path = 'data/000026.png'
    img = cv2.imread(img_path)

    surf = cv2.xfeatures2d.SURF_create(600)
    kp, des = surf.detectAndCompute(img, None)
    p = kp[0]
    print(p.pt)

    img = cv2.drawKeypoints(img, kp, img)
    cv2.imshow('img', img)
    cv2.waitKey()
    print(len(kp))