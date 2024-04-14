import os


def screenshot(driver, name):
    current_dir = os.getcwd()
    the_dir = os.path.abspath(os.path.join(current_dir, 'screenshots'))
    driver.save_screenshot(f'{the_dir}/{name}.png')
