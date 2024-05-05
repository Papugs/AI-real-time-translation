import openai

api_key = "sk-proj-GXn89aJrbsBYXtLdydcsT3BlbkFJPdo1D76HpFf2kuU611XO"

def predict_sentence(text_so_far):
    # Set API key
    openai.api_key = api_key

    # Make the request to OpenAI API
    message = []
    message.append({"role": "user", "content": "Predict what I am going to say next: "+text_so_far})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=message
    )

    # strip away padding we dont need
    response = response.choices[0].message.content
    return text_so_far + response
