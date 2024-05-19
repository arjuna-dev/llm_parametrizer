from llm_parametrizer.open_AI_models import GPT_MODEL
import json
import openai
import datetime
import os
import csv
import concurrent.futures
from dotenv import load_dotenv
from itertools import product
from datetime import datetime

class LLMParametrizer:
    def __init__(self, openai_key=None):
        self.all_parameters = []
        self.models = [GPT_MODEL.GPT_4o.value]
        self.roles = [{"role": "system", "content": "You are a helpful assistant."}]
        self.prompts = []
        self.messages = []
        self.temperatures = [1]
        self.seed = None # seed > -2,147,483,648 and seed < 2,147,483,647
        self.frequency_penalty = 0 # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
        self.n = 1
        self.presence_penalty = 0 # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
        self.response_format = { "type": "json_object" }
        self.top_p = 1 # Number between 0 and 1. An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
        self.tool_choice = "none"

    def initialize_OpenAI(self, openai_key=None):
        if openai_key:
            self.OPEN_AI_API_KEY = openai_key
        else:
            load_dotenv()
            self.OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
        self.client = openai.OpenAI(api_key=self.OPEN_AI_API_KEY)

    def add_prompts(self, *prompts):
        for prompt in prompts:
            self.prompts.append({"role": "user", "content": prompt})
        self.create_message()

    def add_roles(self, *roles):
        self.roles = []
        for role in roles:
            self.roles.append({"role": "system", "content": role})
        self.create_message()

    def create_message(self):
        combinations = product(self.roles, self.prompts)
        for role, prompt in combinations:
            self.messages.append([role, prompt])
        self.parametrize()

    def add_temperatures(self, *temperatures):
        self.temperatures = []
        for temperature in temperatures:
            self.temperatures.append(temperature)
        self.parametrize()

    def add_models(self, *models):
        self.models = []
        for model in models:
            self.models.append(model)
        self.parametrize()

    def add_tweaked_prompts(self, prompt_with_variables, values):
        keys = values.keys()
        values = values.values()

        combinations = list(product(*values))

        prompts = []
        for combination in combinations:
            temp_prompt = prompt_with_variables
            for key, value in zip(keys, combination):
                temp_prompt = temp_prompt.replace(f'{{{key}}}', value)
            prompts.append(temp_prompt)
        
        return prompts

    def return_parameters(self, return_raw=False):
        if return_raw:
            return self.all_parameters
        else:
            all_parameters = ""
            for parameters in self.all_parameters:
                prompt_system = parameters['messages'][0]['content']
                prompt_user = parameters['messages'][1]['content']
                temp = parameters['temperature']
                model = parameters['model']
                all_parameters += f"Prompt user: '{prompt_user}'\nPrompt system: '{prompt_system}'\nTemperature: {temp}\nModel: {model}\n\n"
            return all_parameters
    
    def show_parameters(self, show_raw=False):
        if show_raw:
            print(self.all_parameters)
        else:
            for parameters in self.all_parameters:
                prompt_system = parameters['messages'][0]['content']
                prompt_user = parameters['messages'][1]['content']
                temp = parameters['temperature']
                model = parameters['model']
                print(f"Prompt user: '{prompt_user}'\nPrompt system: '{prompt_system}'\nTemperature: {temp}\nModel: {model}\n")

    def chatGPT_API_call(self, parameters):

        completion = self.client.chat.completions.create(**parameters)

        response = completion.choices[0].message.content
        return response

    def run(self, return_raw=False, output_csv=False):
        assert self.prompts, "At least one prompt is required. use add_prompts() to add at least one prompt."
        date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for parameters in self.all_parameters:
                future = executor.submit(self.chatGPT_API_call, parameters)
                futures.append((parameters, future))

            results = {} if return_raw else ""
            csv_data = []
            for parameters, future in futures:
                try:
                    response = future.result()
                    prompt_system = parameters['messages'][0]['content']
                    prompt_user = parameters['messages'][1]['content']
                    temp = parameters['temperature']
                    model = parameters['model']
                    if return_raw:
                        results[str(parameters)] = future.result()
                    else:
                        results += f"Prompt user: '{prompt_user}'\nPrompt system: '{prompt_system}'\nTemperature: {temp}\nModel: {model}\nDate: {date}\nResponse: {response}\n\n"

                    if output_csv:
                        csv_data.append([prompt_user, prompt_system, temp, model, date, response])

                except Exception as e:
                    if return_raw:
                        results[str(parameters)] = f"Error: {str(e)}"
                    else:
                        results += f"Error: {str(e)}\n"
            if output_csv:
                with open(f"results_{date}.csv", mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Prompt User", "Prompt System", "Temperature", "Model", "Date", "Response"])
                    writer.writerows(csv_data)

            return results

    def parametrize(self):
        combinations = product(self.messages, self.models, self.temperatures)
        self.all_parameters = [{'messages':messages, 'model': model, "temperature": temperature} for messages, model, temperature in combinations]

