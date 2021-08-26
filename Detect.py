import cv2
from datetime import datetime
import dropbox
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        cv2.imwrite(dt_string+'.jpg', img)
        dropbox_access_token = "sl.A3MM7_RO2md_rdM1SU0QOC_0k92NhgDScPJ8evDN3Ut46YW5FU6O3grcfLP2dbMcSEUaVlxqsu7yIeurx4fNpY_CCrIoU-NWuMKt8ttYhYnhe8IC4S9k4y3Z5jL0p7A2caKLs89Sc_9H"  # Enter your own access token
        dropbox_path = "/Test/"+dt_string+".jpg"
        #computer_path = "D:\Major_Project\pythonProject"+"\\"+dt_string+
        computer_path = 'D:/Major_Project/pythonProject/g.jpg'
        client = dropbox.Dropbox(dropbox_access_token)
        #print("[SUCCESS] dropbox account linked")
        client.files_upload(open("D:\Major_Project\pythonProject"+'\\'+dt_string+'.jpg', "rb").read(), dropbox_path)
        #print("[UPLOADED] {}".format(computer_path))



    # Display
    cv2.imshow('Detecting Face', img)


    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
