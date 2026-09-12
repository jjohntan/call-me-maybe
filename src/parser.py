import json
import argparse
import sys
from typing import Any


def load_json_file(file_path: str) -> Any:
    """
    Load and parse a JSON file with proper error handling.

    Args:
        file_path: Path to the JSON file to read.

    Returns:
        The decoded JSON data (typically list or dict).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:  #"r": read only
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        print(f"Error: Invalid JSON format in '{file_path}': {exc}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading '{file_path}'", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        print(f"Error: Unexpected error reading '{file_path}': {exc}", file=sys.stderr)
        sys.exit(1)


def parse_args() -> argparse.Namespace:
    """
      Parse command line arguments

      return:
        parse_args: runs the parser and places the extracted data in a argparse.Namespace object
    """
    parser = argparse.ArgumentParser(
        description="Call Me Maybe: Function calling using constrained decoding with a small LLM model."
    )
    parser.add_argument(
        "--functions_definition",  # option
        type=str,  # type of value after option
        default="data/input/functions_definition.json",
        help="Path to the JSON file containing available function definitions (default: data/input/functions_definition.json)",
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/input/function_calling_tests.json",
        help="Path to the JSON file containing test prompts (default: data/input/function_calling_tests.json)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/output/function_calling_results.json",
        help="Path to the output JSON file to save results (default: data/output/function_calling_results.json)",
    )
    return parser.parse_args()
