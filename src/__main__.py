import json
from llm_sdk.llm_sdk import Small_LLM_Model

with open('data/input/function_calling_tests.json') as f:
    data = json.load(f)
    print(data)

with open('data/input/functions_definition.json') as f:
    data = json.load(f)
    print(data)

# instantiate an object
model = Small_LLM_Model("Qwen/Qwen3-0.6B")
# call encode method of the object
input_ids = model.encode("Hello")
print(input_ids)

def main() -> None:
    print("Hello")

if __name__ == "__main__":
    main()