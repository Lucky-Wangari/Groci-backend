class Website:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def get_name(self):
        return f"{self.name}"

    def get_url(self):
        return f"{self.url}"

    def set_url(self, new_url):
        self.url = new_url
        return f"{self.url}"
        
    def print_details(self):
        print(f"{self.name}")
        print(f"{self.url}")
        
