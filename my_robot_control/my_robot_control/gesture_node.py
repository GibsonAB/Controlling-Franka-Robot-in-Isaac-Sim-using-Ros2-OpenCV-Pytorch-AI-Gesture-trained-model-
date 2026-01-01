import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class GestureNode(Node):
    def __init__(self):
        super().__init__('gesture_node')
        self.publisher_ = self.create_publisher(Int32, 'gesture_id', 10)
        self.timer = self.create_timer(0.1, self.process_frame)

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.get_logger().error("Camera not opened")
            return

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        roi = frame[100:400, 100:400]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (35, 35), 0)
        _, thresh = cv2.threshold(blur, 0, 255,
                                   cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return

        cnt = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(cnt, returnPoints=False)

        if hull is None or len(hull) < 3:
            return

        defects = cv2.convexityDefects(cnt, hull)
        if defects is None:
            return

        finger_count = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            if d > 10000:
                finger_count += 1

        gesture = min(finger_count + 1, 5)

        msg = Int32()
        msg.data = gesture
        self.publisher_.publish(msg)

        cv2.putText(roi, f'Fingers: {gesture}',
                    (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

        cv2.imshow("Gesture", roi)
        cv2.imshow("Threshold", thresh)

        if cv2.waitKey(1) & 0xFF == 27:
            rclpy.shutdown()

def main():
    rclpy.init()
    node = GestureNode()
    rclpy.spin(node)
    node.cap.release()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
