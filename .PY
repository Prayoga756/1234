import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    blur = False

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark

        index_up = lm[8].y < lm[6].y
        middle_up = lm[12].y < lm[10].y
        ring_down = lm[16].y > lm[14].y
        pinky_down = lm[20].y > lm[18].y

        if index_up and middle_up and ring_down and pinky_down:
            blur = True

    if blur:
        frame = cv2.GaussianBlur(frame, (61, 61), 0)

    cv2.imshow("Foto Kita Blur", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()