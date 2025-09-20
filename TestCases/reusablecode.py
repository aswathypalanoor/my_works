from selenium.webdriver.common.by import By
from PIL import Image, ImageDraw
import time


def highlight_element_in_screenshot(driver, By, locator, screenshot_path="screenshot.png",
                                    output_path="highlighted.png", color="red", border_width=3):
    """
    Highlights a web element in a screenshot using Pillow.

    Parameters:
    - driver: Selenium WebDriver instance
    - by: Locator strategy (e.g., By.ID, By.XPATH)
    - locator: The actual locator string
    - screenshot_path: Path to save the raw screenshot
    - output_path: Path to save the highlighted image
    - color: Border color for highlighting
    - border_width: Thickness of the border
    """
    # Wait briefly to ensure element is rendered
    time.sleep(1)

    # Locate the element
    element = driver.find_element(By, locator)
    location = element.location
    size = element.size

    # Take screenshot
    driver.save_screenshot(screenshot_path)
    padding = 20

    # Calculate coordinates
    x1 = location['x']
    y1 = location['y']
    x2 = x1 + size['width'] + 2*padding
    y2 = y1 + size['height'] + 2*padding

    # Open image and draw rectangle
    img = Image.open(screenshot_path)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(x1, y1), (x2, y2)], outline=color, width=border_width)

    # Save the result
    img.save(output_path)





