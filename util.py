import os
import easyocr

# Initialize the OCR reader
reader = easyocr.Reader(['en'], gpu=False)

def getVideos():
    videos = os.listdir("./static/videos")
    return videos

def read_license_plate(license_plate_crop):
    """
    Read the license plate text from the given cropped image.

    Args:
        license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.

    Returns:
        tuple: Tuple containing the formatted license plate text and its confidence score.
    """

    detections = reader.readtext(license_plate_crop)

    for detection in detections:
        bbox, text, score = detection

        text = text.upper().replace(' ', '')

        # if license_complies_format(text):
        #     return format_license(text), score
    
        if len(text) >= 7:
            return text, score

    return None, None