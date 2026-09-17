import cv2, numpy as np
from src.parking_analyzer import analyze_image

def test_analyzer(tmp_path):
    img=np.full((300,500,3),220,dtype=np.uint8)
    p=tmp_path/"parking.jpg"; cv2.imwrite(str(p),img)
    r=analyze_image(str(p),"data/config/parking_spaces.json",str(tmp_path))
    assert r["total"]==8
    assert r["occupied"]==0
    assert r["vacant"]==8
