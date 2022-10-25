import cv2 as c 

cap = c.VideoCapture(2)
contador = 0
while True:
    _, frame = cap.read()
    
    k = c.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('t'):
        image_path = 'Frame_{}.jpg'.format(contador)  
        c.imwrite(image_path, frame)

        contador += 1

    c.imshow('frame', frame)
    
frame.release()
c.destroyAllWindows()
