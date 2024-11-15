import cv2
from abc import ABC


# an abstract class for Decoder
class QRDecoder(ABC):
    """
    this class will detect the qrcode and return str of data
    """
    def detect()-> str:
        """
        this method will detect the QRcode & return the data.

        Parameters: None.
        
        Return:
        str (string) it will return the data as string.
        """



# concreate class
class QrDecoder(QRDecoder):
    def detect(self):

        # start video capturing
        cap = cv2.VideoCapture(0)
        #set the width and height, and UNSUCCESSFULLY set the exposure time
        cap.set(3, 640) # 3 is the index for width
        cap.set(4, 640) # 4 is the index for hieght

        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        while True:
            # Read a frame from the camera
            ret, frame = cap.read()
            # flping the frame
            frame = cv2.flip(frame, 1)
            # Display the frame
            cv2.imshow('frame', frame)

            data, bbox, _ = detector.detectAndDecode(frame)

            # check if there is a QRCode in the image
            if bbox is not None:
                if data:
                    print("[+] QR Code detected, data:", data)



            # Check for key press and exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()





# examples
if __name__ == "__main__":
    qrdecoder = QrDecoder()
    qrdecoder.detect()