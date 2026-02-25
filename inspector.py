import base64
import os
from datetime import datetime
import time

from api import post_inspection, post_telemetry


def _b64_from_file(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def run_inspection_cycle(api_base: str, sample_image_path: str, enable_telemetry: bool = True):
    inspection_id = f"insp_{int(time.time())}"
    timestamp = datetime.now().isoformat(timespec="seconds")

    # Optional telemetry (single update only)
    if enable_telemetry:
        try:
            post_telemetry(api_base, {
                "inspection_id": inspection_id,
                "inspection_stage": "completed",
                "progress_percent": 100,
                "timestamp": timestamp,
            })
        except Exception:
            pass

    if not os.path.exists(sample_image_path):
        raise FileNotFoundError(f"Image not found: {sample_image_path}")

    image_b64 = _b64_from_file(sample_image_path)

    # Fake static results for now
    payload = {
        "inspection_id": inspection_id,
        "timestamp": timestamp,
        "height_cm": 120,
        "has_crack": False,
        "confidence": 0.15,
        "image": image_b64,
    }

    response = post_inspection(api_base, payload)

    print(f"[OK] Inspection uploaded instantly: {inspection_id}")