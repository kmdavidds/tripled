from fast_plate_ocr import ONNXPlateRecognizer

m = ONNXPlateRecognizer('argentinian-plates-cnn-model')
print(m.run("./plat.jpeg"))