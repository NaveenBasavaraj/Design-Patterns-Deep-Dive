from abc import ABC, abstractmethod

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self):
        pass
    
class ZipCompression(CompressionStrategy):
    def compress(self, file_path):
        return f"{file_path}.zip"

class RarCompression(CompressionStrategy):
    def compress(self, file_path):
        return f"{file_path}.rar"

class GzipCompression(CompressionStrategy):
    def compress(self, file_path):
        return f"{file_path}.gz"

class FileCompressor:
    def __init__(self, strategy: CompressionStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy: CompressionStrategy):
        self.strategy = strategy
    
    def compress_file(self, file_path):
        result = self.strategy.compress(file_path)
        print(f"Compressed: {result}")


if __name__ == "__main__":
    user_preference = "gzip"
    strategies = {
        "zip": ZipCompression(),
        "rar": RarCompression(),
        "gzip": GzipCompression()
    }

    compressor = FileCompressor(strategies[user_preference])
    compressor.compress_file("report.txt")
        
    
