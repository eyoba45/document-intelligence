class AppState:
    def __init__(self):
        self.current_collection = None
        self.document_loaded = False

# Single instance shared across the whole app
app_state = AppState()