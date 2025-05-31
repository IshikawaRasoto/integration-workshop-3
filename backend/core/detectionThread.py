import cv2
import time
import os
from note_detection.note_detection import analisar_cores_com_mascaras
from note_detection.calibration import Calibration

class NoteDetection:

    def __init__(self):
        self.notes_detected = None #This variable is extremely important!
        self.running = True
        self.cam = cv2.VideoCapture(2) #TODO change this value to 0 later 

        self.calibration = Calibration()
        self.calibration.points = [(255, 59), (290, 966), (1348, 1041), (1361, 95)]

        desired_width = 1920
        desired_height = 1080

        # Attempt to set the frame width
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
        # Attempt to set the frame height
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

        self.run = 0
    
    def detect_note_loop(self):
        while self.running:
            ret, frame = self.cam.read()
            if ret:
                # Salva o frame capturado
                cv2.imwrite("board.jpg", frame)
                if os.path.exists("board.jpg"):
                    frame = cv2.rotate(frame, cv2.ROTATE_180)
                    frame = frame[:-10, 180:-240]
                    frame = self.calibration.apply_calibration(frame)
                    self.notes_detected = analisar_cores_com_mascaras(frame, True)
                    print("Notas detectadas: ")
                    print(self.notes_detected)
                else:
                    print ("Falha ao acessar o frame")
            else:
                pass
                # print("Erro ao acessar a câmera.")
            time.sleep(0.1)
        
    def get_notes_detected(self):
        return self.notes_detected
    
    def stop_note_detection_thread(self):
        self.running = False

