import asyncio
import logging
import os

import joblib
import numpy
import pandas as pd

# -------- Add your dependencies here --------

# Logger setup
logger = logging.getLogger(__name__)


async def pre_process(
    model_files_path: str, request_id: str, input_data_frame: pd.DataFrame
) -> numpy.ndarray:
    # ----------------------------------------------
    # - Replace the following lines with your code -
    # ----------------------------------------------
    # Feature scaling: can be either manual (hardcoded) or loaded as a file
    # (e.g. if the StandardScaler was pickled from training) as follows
    standard_scaler = os.path.join(model_files_path, "example_standard_scaler.pkl")
    # Feature selection: can be either manual (hardcoded) or loaded as a file
    # (e.g. if the ordered list of feature names was pickled from training) as follows
    training_cols = os.path.join(model_files_path, "training_cols.pkl")

    # Scale the test data in the same way you scaled your training and validation data
    scaler = joblib.load(standard_scaler)  # load our scaler

    # Order cols in the same way you did in training
    training_cols = joblib.load(training_cols)  # load your ordered training cols
    # Transform the inputs for model execution.
    # Their shape should match exactly what your model expects for inference.
    return scaler.transform(input_data_frame[training_cols].values)


async def post_process(
    model_files_path: str, request_id: str, quantized_inference: float
) -> float:
    # ----------------------------------------------
    # - Replace the following lines with your code -
    # ----------------------------------------------
    return quantized_inference


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    model_files_path = os.path.join(os.path.curdir, "model_files")
    request_id = "some-request-id"
    data_frame_path = os.path.join(
        os.path.curdir, "assets", "sample-input-data-frame.parquet"
    )
    data_frame = pd.read_parquet(data_frame_path)
    scaled_inputs = loop.run_until_complete(
        pre_process(model_files_path, request_id, data_frame)
    )
    print("scaled inputs:", scaled_inputs)
    scaled_inference = loop.run_until_complete(
        post_process(model_files_path, request_id, 3.14159)
    )
    print("scaled inference:", scaled_inference)
    loop.close()
