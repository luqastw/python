import sys
from gpt4all import GPT4All

def main():
    if len(sys.argv) < 2:
        print("Uso: python note2.py <pergunta>")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])

    model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    resposta = model.generate(prompt)
    print(resposta)

if __name__ == "__main__":
    main()
