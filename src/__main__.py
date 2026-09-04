import json

with open('data/input/function_calling_tests.json') as f:
    data = json.load(f)
    print(data)

with open('data/input/functions_definition.json') as f:
    data = json.load(f)
    print(data)

def main() -> None:
    print("Hello")

if __name__ == "__main__":
    main()