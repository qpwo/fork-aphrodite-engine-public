from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:2242/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# model = '70b-base'
model = '/home/ubuntu/hff/8b-base'


def do_one(prompt: str, foo: int):
    print(f"Prompt:", prompt, "Completion:", sep='\n')
    res = client.completions.create(
        model=model,
        prompt=prompt,
        temperature=1.1,
        n=1,
        max_tokens=20,
        stream=True,
        extra_body={
            "min_p": 0.1,
            "frequency_penalty": 0.9,
            "passthru": {
                "foo": foo,
                "bar": "jsdkjdnf"
            }
        },
    )
    for msg in res:
        x = msg.choices[0].text
        print(x, end='', flush=True)
    print()

do_one("I remember when", 345678)

do_one("I remember how", 987543)
