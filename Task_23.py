from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Start a WebDriver session
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element_by_css_selector("iframe.demo-frame"))

# Locate the draggable element
draggable_element = driver.find_element_by_id("draggable")

# Locate the droppable element
droppable_element = driver.find_element_by_id("droppable")

# Perform drag and drop operation
action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable_element, droppable_element).perform()

# Wait for a moment to observe the result
import time
time.sleep(3)

# Close the browser
driver.quit()