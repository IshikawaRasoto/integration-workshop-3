
class NoteDetection:

    def __init__(self):
        self.notes_detected = None #This variable is extremely important!
        self.running = True

    
    def detect_note_loop(self):
        while self.running:
            # TODO: Do all the logic to detect the notes
            return # Delete this line when coding

        
    def get_notes_detected(self):
        return self.notes_detected
    
    def stop_note_detection_thread(self):
        self.running = False