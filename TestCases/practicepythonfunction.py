from PIL import Image, ImageDraw
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver

def highlight_assert_in_screenshot(screenshot_path, assert_coords):
    """
    Highlights the assert area in a screenshot.
    :param screenshot_path: Path to the original screenshot.
    :param assert_coords: Tuple (x, y, width, height) of the assert area.
    """
    img = Image.open(screenshot_path)
    draw = ImageDraw.Draw(img)

    # Draw a red rectangle with a 3-pixel border
    draw.rectangle(assert_coords, outline="red", width=3)

    highlighted_screenshot_path = screenshot_path.replace(".png", "_highlighted.png")
    img.save(highlighted_screenshot_path)
    print(f"Highlighted screenshot saved: {highlighted_screenshot_path}")

# Example usage (after capturing the screenshot)
# Replace with actual coordinates of your assert statement
#assert_area_coordinates = (100, 200, 300, 50) # x, y, width, height
# highlight_assert_in_screenshot("failure_screenshot_my_test_20250912_081400.png", assert_area_coordinates)

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.implicitly_wait(30)
act_title = driver.find_element(By.XPATH, "//div[@class='page-title']").text
act_titleimg=driver.find_element(By.XPATH, "//div[@class='page-title']")
location = act_titleimg.location
size = act_titleimg.size
x1 = location['x']
y1 = location['y']
x2 = x1 + size['width']
y2 = y1 + size['height']

print(act_title)
exp_title = "nopCommerce demo store. -Login"
#draw = ImageDraw.Draw(img)
if act_title == exp_title:
    assert True
    driver.close()
else:
    driver.save_screenshot("test_title_verification1.png")
    img = Image.open("test_title_verification1.png")
    draw = ImageDraw.Draw(img)
    draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=3)
    highlighted_screenshot_path = "test_title_verification1.png".replace(".png", "_highlighted.png")
    img.save(highlighted_screenshot_path)
    driver.close()
    assert False