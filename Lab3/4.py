class DefaultList(list):
    def __init__(self):
        super().__init__()
        self.default = 0


    def __getitem__(self, item):
        try:


