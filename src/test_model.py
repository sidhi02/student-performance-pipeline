import os
import sys

sys.path.append("src")

from train import train_model

def test_training():
    score = train_model()
    assert score is not None

def test_performance():
    score = train_model()
    assert score > 0.0

def test_model_saved():
    train_model()
    assert os.path.exists("models/model.pkl")
