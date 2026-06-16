
# register_model.py

from clean_score_code import clean_score_code
from extract_metadata import extract_metadata
from generate_json import generate_json

def main(score_path, pkl_path):

    # 1. Clean scoring code
    clean_score_code(score_path, pkl_path)

    # 2. Extract metadata
    features, output, function, algorithm = extract_metadata(
        "score.py", pkl_path
    )

    # 3. Generate JSON
    generate_json(features, output, function, algorithm)

    # 4. (optional) call API here

    print("✅ Model ready for Model Manager")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--score", required=True)
    parser.add_argument("--model", required=True)

    args = parser.parse_args()

    main(args.score, args.model)
