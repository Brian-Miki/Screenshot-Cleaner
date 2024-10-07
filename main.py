import os
import shutil

# Path to desktop (source) and screenshot folder (destination)
desktopFolder = os.path.join(os.path.join(os.path.expanduser('~')),'Desktop')
screenshotFolder = os.path.expanduser("~/Documents/Screenshots")

if not os.path.exists(screenshotFolder):
    os.makedirs(screenshotFolder)

# Move the files over
for screenshot in os.listdir(desktopFolder):
    if screenshot.startswith("Screenshot") and screenshot.endswith(".png"):
        sourcePath = os.path.join(desktopFolder, screenshot)
        destinationPath = os.path.join(screenshotFolder, screenshot)
        shutil.move(sourcePath, destinationPath)
        print(f"Moved {screenshot} from {sourcePath} into {destinationPath}")