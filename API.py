from fastapi import FastAPI
from pydantic import BaseModel
from siqber import SIQBERPredictor

app = FastAPI(title="SI-QBER v2.1 API")
predictor = SIQBERPredictor()

class Path(BaseModel):
    storage_cycles: float
    observed_qber: float

@app.post("/correct")
def correct_qber(path: Path):
    corrected = predictor.correct_path(path.storage_cycles, path.observed_qber)
    return {
        "corrected_qber": float(corrected),
        "viable_path": corrected < 0.11,
        "smra_score": 1.0 / (1 + corrected)
    }
