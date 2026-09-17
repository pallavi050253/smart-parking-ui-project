import json
import os

import cv2
import numpy as np


def polygon_mask(shape, points):
    mask = np.zeros(shape[:2], dtype=np.uint8)

    # Convert flat coordinates:
    # [x1,y1,x2,y2,...]
    # into OpenCV format:
    # [[x1,y1],[x2,y2],...]
    points = np.array(points, dtype=np.int32).reshape(-1, 2)

    cv2.fillPoly(mask, [points], 255)
    return mask


def analyze_image(input_path, config_path, result_dir):
    image = cv2.imread(input_path)

    if image is None:
        raise ValueError("The uploaded file is not a valid image.")

    with open(config_path, encoding="utf-8") as f:
        spaces = json.load(f)["spaces"]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    annotated = image.copy()

    occupied = 0
    details = []

    # Occupancy threshold
    threshold = 0.22

    for space in spaces:
        # Convert coordinates into OpenCV polygon format
        pts = np.array(
            space["points"],
            dtype=np.int32
        ).reshape(-1, 2)

        # Create mask for this parking space
        mask = polygon_mask(image.shape, space["points"])

        # Get grayscale pixels inside parking space
        pixels = gray[mask > 0]

        # Calculate percentage of dark pixels
        dark_ratio = (
            float(np.mean(pixels < 100))
            if len(pixels)
            else 0.0
        )

        # Determine occupancy
        is_occupied = dark_ratio > threshold

        if is_occupied:
            occupied += 1

        status = "OCCUPIED" if is_occupied else "VACANT"

        # Red = occupied
        # Green = vacant
        box_color = (
            (0, 0, 255)
            if is_occupied
            else (0, 180, 0)
        )

        # Draw parking-space boundary
        cv2.polylines(
            annotated,
            [pts],
            True,
            box_color,
            3
        )

        # Calculate label position
        x, y = pts[0]

        cv2.putText(
            annotated,
            f"{space['id']}: {status}",
            (int(x), int(y) - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            box_color,
            2
        )

        details.append({
            "id": space["id"],
            "status": status,
            "dark_ratio": round(dark_ratio, 3)
        })

    total = len(spaces)
    vacant = total - occupied
    occupancy = (
        (occupied / total) * 100
        if total > 0
        else 0
    )

    # Add summary to image
    summary = (
        f"Occupied: {occupied} | "
        f"Vacant: {vacant} | "
        f"Occupancy: {occupancy:.1f}%"
    )

    cv2.rectangle(
        annotated,
        (10, 10),
        (490, 50),
        (30, 30, 30),
        -1
    )

    cv2.putText(
        annotated,
        summary,
        (20, 38),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # Create result directory
    os.makedirs(result_dir, exist_ok=True)

    result_path = os.path.join(
        result_dir,
        "parking_result.jpg"
    )

    cv2.imwrite(result_path, annotated)

    return {
        "total": total,
        "occupied": occupied,
        "vacant": vacant,
        "occupancy": round(occupancy, 1),
        "details": details,
        "result_path": result_path
    }