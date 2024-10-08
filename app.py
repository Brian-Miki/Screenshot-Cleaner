from flask import Flask, jsonify
import os
import shutil

app = Flask(__name__)

# Path to desktop (source) and screenshot folder (destination)
desktopFolder = os.path.join(os.path.join(os.path.expanduser('~')),'Desktop')
screenshotFolder = os.path.expanduser("~/Documents/Screenshots")

def move_screenshots():
    if not os.path.exists(screenshotFolder):
        os.makedirs(screenshotFolder)


    movedFiles = []

    # Move the files over
    for screenshot in os.listdir(desktopFolder):
        if screenshot.startswith("Screenshot") and screenshot.endswith(".png"):
            sourcePath = os.path.join(desktopFolder, screenshot)
            destinationPath = os.path.join(screenshotFolder, screenshot)
            shutil.move(sourcePath, destinationPath)
            movedFiles.append(screenshot)
    return movedFiles
    
@app.route('/clean_screenshots', methods = ['POST'])
def clean_screenshots():
    moved_files = move_screenshots()
    if moved_files:
        return jsonify({"status": "success", "moved_files": moved_files}),200
    else:
        return jsonify({"status": "no_files_found"}), 200

if __name__ == '__main__':
    app.run(debug=True)