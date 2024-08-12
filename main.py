import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)      #selecting the camera

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) #dedicate the face

screen_w, screen_h = pyautogui.size() # to get the screen sizes

while True:
    ret, frame = cam.read()   # to initiate the camera
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert the colors
    output = face_mesh.process(rgb_frame) # create an output using the face_mesh
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w = frame.shape[:2]
    print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]): #landmarks of one eye
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            print(x, y)
            cv2.circle(frame, (x, y), 1, (0, 255, 0), 2)
            if id == 1:
                screen_x = int(landmark.x * screen_w)
                screen_y = int(landmark.y * screen_h)

                pyautogui.moveTo(screen_x, screen_y) #move the mouse to x_screen and Y_screen
        lefteye = [landmarks[145], landmarks[159]] # landmarks of the left eye
        for landmark in lefteye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 1, (0, 255, 255), 2)
        if (lefteye[0].y - lefteye[1].y) < 0.004: #difference between the positions of left eyelids
            pyautogui.click() #initiate click
            pyautogui.sleep(1) #initiate sleep for 1 sec



    cv2.imshow('frame', frame)   # to show the camera footage
    cv2.waitKey(1)

