import cv2 as c 

cap = c.VideoCapture(2)
contador = 0
while True:
    _, frame = cap.read()
    
    
    k = c.waitKey(1)
    if k == ord('q'):
        print('q was pressed - finishing...')
        break
    elif k == ord('t'):
        image_path = 'Frame_{}.jpg'.format(contador)  
        c.imwrite(image_path, frame)

        contador += 1

    c.imshow('frame', frame)
    
  
# After the loop release the cap object
frame.release()
# Destroy all the windows
c.destroyAllWindows()