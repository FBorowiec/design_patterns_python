"""
Exposing several components through a single interface.
Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

- Balancing complexity and presentation/usability
- Typical code has:
    - Many subsystems
    - Complex internal structure
    - End user should not be exposed to interals
"""


class Buffer:
    def __init__(self, width=30, height=20):
        self.height = height
        self.width = width
        self.buffer = [" "] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    """Viewport Facade"""

    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("Hello!")
    ch = c.get_char_at(0)
