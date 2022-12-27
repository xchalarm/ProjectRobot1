# This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Hand = "None"
F1 = "1fold"
F2 = "2fold"
F3 = "3fold"
F4 = "4fold"
F5 = "5fold"

cap = cv2.VideoCapture(0)

# Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                if id == 9:
                    id9 = int(id)
                    cx9 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy

            if cx5 > cx9:
                Hand = "Right Hand"


                if cx4 > cx3:
                    F1 = "1 up"
                else:
                    F1 = "1 Fold"
                if cy6 > cy8:
                    F2 = "2 up"
                else:
                    F2 = "2 Fold"
                if cy10 > cy12:
                    F3 = "3 up"
                else:
                    F3 = "3 Fold"
                if cy14 > cy16:
                    F4 = "4 up"
                else:
                    F4 = "4 Fold"
                if cy18 > cy20:
                    F5 = "5 up"
                else:
                    F5 = "5 Fold"

            else:
                Hand = "Left Hand"
                if cx4 < cx3:
                    F1 = "1 up"
                else:
                    F1 = "1 Fold"
                if cy6 > cy8:
                    F = "2 up"
                else:
                    F = "2 Fold"
                if cy10 > cy12:
                    F3 = "3 up"
                else:
                    F3 = "3 Fold"
                if cy14 > cy16:
                    F4 = "4 up"
                else:
                    F4 = "4 Fold"
                if cy18 > cy20:
                    F5 = "5 up"
                else:
                    F5 = "5 Fold"

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            cv2.putText(img, str(Hand), (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            cv2.putText(img, str(F1), (10, 100), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)
            cv2.putText(img, str(F2), (10, 130), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)
            cv2.putText(img, str(F3), (10, 160), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)
            cv2.putText(img, str(F4), (10, 190), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)
            cv2.putText(img, str(F5), (10, 220), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 255), 2)
            cv2.imshow("Image", img)

            if cv2.waitKey(1) & 0xFF == ord("e"):
                break