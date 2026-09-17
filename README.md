# Smart Parking Space Analyzer — UI Based

A Computer Vision project using Python, Flask and OpenCV. The browser UI accepts a parking image and displays occupancy statistics and an annotated result.

## Run on Windows
```powershell
py -m pip install -r requirements.txt
py -m pytest -q
py app.py
```
Then open **http://127.0.0.1:5000** in your browser.

## Structure
`app.py` — Flask UI and upload handling  
`src/parking_analyzer.py` — OpenCV occupancy logic  
`templates/index.html` — web interface  
`static/style.css` — interface styling  
`data/config/parking_spaces.json` — parking-space polygons  
`results/` — generated annotated images  
`tests/` — tests

## Note
The baseline detector uses a configurable dark-pixel ratio. For a real parking-lot camera, calibrate the polygons and threshold using representative images. Do not claim accuracy metrics unless you measure them yourself.
