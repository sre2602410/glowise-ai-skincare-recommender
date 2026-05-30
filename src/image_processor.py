import cv2
import numpy as np
from PIL import Image

def analyze_skin_image(image_bytes):
    """
    Analyzes a skin image to detect potential concerns like redness, 
    dark spots, and texture issues.
    """
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        return None
        
    # Convert to RGB for analysis
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 1. Redness Detection (Acne/Sensitivity)
    # Skin is usually in a specific range, we look for 'extra' red
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    red_mask = mask1 + mask2
    redness_score = np.sum(red_mask > 0) / (img.shape[0] * img.shape[1])
    
    # 2. Dark Spot Detection (Pigmentation)
    # Look for dark areas that are not hair/eyes (simplified)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply a threshold to find dark spots
    _, dark_mask = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
    dark_spots_score = np.sum(dark_mask > 0) / (img.shape[0] * img.shape[1])
    
    # 3. Texture/Pores (Edge density)
    edges = cv2.Canny(gray, 100, 200)
    texture_score = np.sum(edges > 0) / (img.shape[0] * img.shape[1])
    
    # Map scores to concerns
    concerns = []
    if redness_score > 0.05:
        concerns.append("sensitivity")
        concerns.append("acne")
    if dark_spots_score > 0.1:
        concerns.append("brightening")
    if texture_score > 0.02:
        concerns.append("texture")
    if redness_score < 0.02 and texture_score < 0.01:
        concerns.append("hydration") # Fallback for clear but maybe dry skin
        
    return {
        "detected_concerns": list(set(concerns)),
        "scores": {
            "redness": round(float(redness_score), 4),
            "dark_spots": round(float(dark_spots_score), 4),
            "texture": round(float(texture_score), 4)
        }
    }
