import cv2
import time
import os
from note_detection.note_detection import analisar_cores_com_mascaras

class NoteDetection:

    def __init__(self):
        self.notes_detected = None #This variable is extremely important!
        self.running = True
        self.cam = cv2.VideoCapture(2) #TODO change this value to 0 later 

        self.run = 0
    
    def detect_note_loop(self):
        while self.running:
            ret, frame = self.cam.read()
            if ret:
                # Salva o frame capturado
                cv2.imwrite("board.jpg", frame)
                if os.path.exists("board.jpg"):
                    self.notes_detected = analisar_cores_com_mascaras(frame)
                    print ("Notas detectadas: ")
                    print(self.notes_detected)
                else:
                    print ("Falha ao acessar o frame")
            else:
                pass
                print("Erro ao acessar a câmera.")
            time.sleep(0.1)
        
    def get_notes_detected(self):
        return self.notes_detected
    
    def stop_note_detection_thread(self):
        self.running = False

