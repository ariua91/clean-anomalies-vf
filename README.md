# clean-anomalies-vf
Using VF public API, look for wrong tags and duplicates and correct

## Usage

1. You need a VF PUBLIC API `client_id` & `client_secret` in secret_keys.py. 
2. Run via `python anomaly.py`

## Potential Bugs
 - If the users create a new task / cancel while we are extracting, things will go weird.
   To circumvent this bug, archiving is done very carefully.
