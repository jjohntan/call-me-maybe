from src.parser import parse_args, load_json_file
from llm_sdk.llm_sdk import Small_LLM_Model



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
def main() -> None:
    args = parse_args()
    # functions = load_json_file(args.functions_definition)
    # print(type(functions))
    # print(functions)
    
    # Prompt
    prompts = load_json_file(args.input)
    # print(type(prompts))
    # print(prompts)
    model = Small_LLM_Model("Qwen/Qwen3-0.6B")

    # Tokenization
    for prompt_item in prompts:
        input_ids = model.encode(prompt_item["prompt"])
        print(input_ids)




if __name__ == "__main__":
    main()
    