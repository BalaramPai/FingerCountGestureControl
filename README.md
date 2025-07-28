Finger Count Detection using OpenCV & MediaPipe

This project uses OpenCV and MediaPipe to implement real-time finger counting through a webcam. It detects hand gestures
and displays the corresponding finger count using overlay images.

## Description

* Works with the right hand only, with the palm facing the camera.
* Uses MediaPipe's hand landmark model to detect and track hand keypoints.
* The logic is based on comparing the positions of specific finger landmarks to determine whether each finger is open or closed.
* Displays a relevant image (1.png, 2.png, etc.) from the `FingerImages` folder based on the number of fingers shown.

## Requirements

* Python 3.x
* OpenCV
* MediaPipe
* Webcam (Laptop camera or USB cam)

##  Logic Overview

Landmarks Used: Tips of fingers - `4, 8, 12, 16, 20`

Thumb Detection**: Since the thumb opens sideways (not upward like other fingers), we compare **x-coordinates**:

  ```python
  if lmList[4][1] < lmList[2][1]:
      thumb = open
  ```

Other Fingers** (Index to Little): Compared based on **y-coordinates, since open fingers have tips above their
respective lower joints:

  ```python
  if lmList[finger_tip][2] < lmList[finger_tip - 2][2]:
      finger = open
  ```

Overlay Image Handling:

  * Finger count `total` is calculated by summing open fingers.
  * We display the corresponding overlay using:

    ```python
    overlayImage = overLayList[total - 1]
    ```

    This is because the list is zero-indexed (i.e., 1 finger corresponds to image at index 0).

Image Overlay

* Overlay images (like `1.png`, `2.png`...) must be stored in a folder named `FingerImages`.
* Each overlay is drawn on the webcam feed at the top-left corner.

##  Output

* A live video feed with:

  * Drawn hand landmarks
  * Displayed finger count
  * Overlay image corresponding to finger count
  * FPS (Frames Per Second) indicator

## 💡 Note

* Designed specifically for **right hand** and **forward-facing palm**.
* For left-hand or different orientations, logic must be adapted.

## 🧑‍💻 Author

Made By Balaram Pai H
Reference : FreeCodeCampOrg
