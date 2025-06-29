import numpy as np
import cv2

def get_limits(color, color_space='BGR', delta_hue=10, lower_saturation=100, lower_value=100, upper_saturation=255, upper_value=255):
    """
    Get lower and upper limits for a color in a specified color space.

    Args:
        color (tuple/list): The color value (e.g., (B, G, R) or (H, S, V)).
        color_space (str): The color space of the input color ('BGR', 'HSV', etc.).
        delta_hue (int): Range for hue channel.
        lower_saturation (int): Lower bound for saturation.
        lower_value (int): Lower bound for value.
        upper_saturation (int): Upper bound for saturation.
        upper_value (int): Upper bound for value.

    Returns:
        tuple: lower and upper limits as numpy arrays.
    """
    c = np.uint8([[color]])
    if color_space.upper() == 'BGR':
        hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    elif color_space.upper() == 'RGB':
        hsv_color = cv2.cvtColor(c, cv2.COLOR_RGB2HSV)
    elif color_space.upper() == 'HSV':
        hsv_color = c
    else:
        raise ValueError("Unsupported color space: {}".format(color_space))

    h = hsv_color[0][0][0]
    lower_limit = np.array([max(h - delta_hue, 0), lower_saturation, lower_value], dtype=np.uint8)
    upper_limit = np.array([min(h + delta_hue, 179), upper_saturation, upper_value], dtype=np.uint8)
    return lower_limit, upper_limit