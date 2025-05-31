import cv2
import time

class NoteDetection:

    def __init__(self):
        self.notes_detected = None #This variable is extremely important!
        self.running = True
        self.cam = cv2.VideoCapture(2) #TODO change this value to 0 later 

        self.run = 0
    
    def detect_note_loop(self):
        #while self.running:
        #    ret, frame = self.cam.read()
        #    if ret:
        #        # Salva o frame capturado
        #        cv2.imwrite("foto.jpg", frame)
        #        print("Foto tirada com sucesso!")
        #    else:
        #        print("Erro ao acessar a câmera.")
        #
        #    self.running = False

        while self.run < 10:
            ret, frame = self.cam.read()
            if ret:
                # Salva o frame capturado
                cv2.imwrite(f"foto{self.run}.jpg", frame)
                print("Foto tirada com sucesso!")
            else:
                print("Erro ao acessar a câmera.")

            self.run = self.run + 1
            self.running = False
        
    def get_notes_detected(self):
        return self.notes_detected
    
    def stop_note_detection_thread(self):
        self.running = False