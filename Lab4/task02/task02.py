import numpy as np

class Image:
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=None):
        """ Initialize the Image object header and data. """
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels if pixels is not None else np.zeros((rows, columns, 3), dtype=int)

    def __str__(self):
        """ Return the string representation of the image in PPM format. """
        header = f"{self.format}\n{self.columns} {self.rows}\n{self.max_value}\n"
        pixels_str = '\n'.join(' '.join(map(str, pixel)) for row in self.pixels for pixel in row)
        return header + pixels_str

    def sepia(self):
        """ Apply sepia filter to the image using NumPy for performance boost. """
        sepia_matrix = np.array([
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131]
        ])
        # Apply the sepia transformation using matrix multiplication
        sepia_pixels = np.dot(self.pixels, sepia_matrix.T)
        
        # Clip values to ensure they stay in [0,255] range and convert to integer
        self.pixels = np.clip(sepia_pixels, 0, 255).astype(int)

    def read(self, filename):
        """ Read PPM Image format from file. """
        with open(filename, 'r') as file:
            self.format = file.readline().strip()
            self.columns, self.rows = map(int, file.readline().split())
            self.max_value = int(file.readline().strip())

            # Read all pixel data and reshape it
            pixel_values = np.loadtxt(file, dtype=int).reshape(self.rows, self.columns, 3)
            self.pixels = pixel_values

    def write(self, filename):
        """ Write PPM Image format to file efficiently using NumPy. """
        with open(filename, 'w') as file:
            file.write(f"{self.format}\n{self.columns} {self.rows}\n{self.max_value}\n")
            np.savetxt(file, self.pixels.reshape(-1, 3), fmt='%d', delimiter=' ')
