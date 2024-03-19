
import openai

openai.api_key = "sk-..."

response = openai.completions.create(
    model = "gpt-3.5-turbo-instruct",
    prompt = 'Decide si el sentimiento de un Tweet es positivo, neutral, o negativo \n\nTweet: PETER J. RICHERSON Biólogo. Autor/coautor de Culture and the evolutionary process (1985), Principles of human ecology (1996), Not by genes alone: How culture transformed human evolution (2005), Cultural evolution (2013) o A story of us: A new look at human evolution (2021).\"\nSentiment: ' ,
    temperature = 0,
    max_tokens = 60,
    top_p = 1,
    frequency_penalty = 0.5,
    presence_penalty = 0,
)