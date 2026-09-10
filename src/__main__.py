import json
import argparse
from llm_sdk.llm_sdk import Small_LLM_Model

# with open('data/input/function_calling_tests.json') as f:
#     data = json.load(f)
#     print(data)

# with open('data/input/functions_definition.json') as f:
#     data = json.load(f)
#     print(data)


# instantiate an object
# model = Small_LLM_Model("Qwen/Qwen3-0.6B")
# call encode method of the object
# input_ids = model.encode("Hello World")
# print(input_ids)# tensor([[9707, 4337]])

# print(model.decode(input_ids))# ['Hello World']

# print(input_ids[0])# tensor([9707, 4337])

# print(input_ids[0].tolist())# [9707, 4337]

# logits = model.get_logits_from_input_ids(input_ids[0].tolist())
# print(type(logits))# <class 'list'>
# print(logits)
# print(len(logits))# 151936
# print(type(logits[0]))# <class 'float'>

# r = list(enumerate(logits))
# print(r)

# def argmax(pairs):
#     return max(pairs, key=lambda x: x[1])[0]

# hightest_logit = argmax(r)
# print(hightest_logit)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Call Me Maybe: Function calling using constrained decoding with a small LLM model."
    )
    parser.add_argument(
        "--functions_definition",
        type=str,
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


def main() -> None:
    args = parse_args()
    print(f"Functions definition file: {args.functions_definition}")
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")

if __name__ == "__main__":
    main()
    