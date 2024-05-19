# LLM Parametrizer

A Python script to generate parametrized variations of prompts and get results from API calls to LLMs.


Currently only support for OpenAI’s ChatGPT is available.


## Rationale

LLM respones are unpredictable and multiple tries are required to achieve the desired results when experimenting with prompts. This is a tedious process and difficult to document if done haphazardly.

This script aims at easing the process of experimenting with prompts. More importantly it aims at automatically documenting the process, making it easy to keep track of which prompts have which effects. All this while speeding up the process by parametrization and asynchrous API calls.


## Dependencies

* openai
* python-dotenv


## Features

* Test an API call with various parametrized values:
  * Prompts
  * Roles
  * Models
  * Temperatures
* Save as CSV to view en google sheets or similar


Parameters not yet implemented include:

* Seeds
* Frequency penalties
* Presence penalties
* Top p


## Usage

First, initialize `LLM_Parametrizer`:

```python
from llm_parametrizer import GPT_MODEL, LLMParametrizer

prmtrzr = LLMParametrizer()
```



Make sure you have a .env file with the OPEN_AI_API_KEY variable pointing to your OpenAI API key:

```python
OPEN_AI_API_KEY=sk-proj-<your API key here>
prmtrzr.initialize_OpenAI()
```


Alternatively, pass your OpenAI key when initializing.

```python
prmtrzr.initialize_OpenAI("sk-proj-<your API key here>")
```


You can then add prompts, models, and temperatures:

```python
prmtrzr.add_prompts("Write a single letter of your choice")
prmtrzr.add_models(GPT_MODEL.GPT_4o.value, GPT_MODEL.GPT_3_5_T.value)
prmtrzr.add_temperatures(0.5, 1.0, 2)
```


The above code would generate 6 prompts (2 models times 3 temperatures).


With `prmtrzr.show_parameters()` you can print the parameters that have been so far added:


> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 0.5
> Model: gpt-4o
>
> \
> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 1.0
> Model: gpt-4o
>
> \
> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 2
> Model: gpt-4o
>
> \
> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 0.5
> Model: gpt-3.5-turbo
>
> \
> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 1.0
> Model: gpt-3.5-turbo
>
> \
> Prompt user: 'Write a single letter of your choice'
> Prompt system: 'You are a helpful assistant.'
> Temperature: 2
> Model: gpt-3.5-turbo
>
> \


Use `prmtrzr.show_parameters(show_raw=True)` to output the full JSON that would be passed to the OpenAI API call. Use `prmtrzr.return_parameters()` or `prmtrzr.return_parameters(return_raw=True)` to return the values instead of printing them.



Finally, you can run the parameterized API calls with:


```python
results = prmtrzr.run()
```


The `run` method returns a prettyfied string which includes the responses. So printing `results` with `print(results)` looks like this:


> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 0.5
> Model: gpt-4o
> Date: 2024-05-18-19-59-01
> Response: A
>
> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 1.0
> Model: gpt-4o
> Date: 2024-05-18-19-59-01
> Response: A
>
> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 2
> Model: gpt-4o
> Date: 2024-05-18-19-59-01
> Response: L
>
> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 0.5
> Model: gpt-3.5-turbo
> Date: 2024-05-18-19-59-01
> Response: A
>
> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 1.0
> Model: gpt-3.5-turbo
> Date: 2024-05-18-19-59-01
> Response: G
>
> \
> Prompt: 'Write a single letter of your choice'
> Temperature: 2
> Model: gpt-3.5-turbo
> Date: 2024-05-18-19-59-01
> Response: E
>
> \


To get the raw data use:

```python
results = prmtrzr.run(return_raw=True)
```


To output a csv file (viewable in google sheets for example) use:

```python
results = prmtrzr.run(output_csv=True)
```


This will save a csv file viewable in google sheets or similar software:


> Prompt,Temperature,Model,Time,Response
> Write a single letter of your choice,0.5,gpt-4o,2024-05-18-19-59-01,A
> Write a single letter of your choice,1.0,gpt-4o,2024-05-18-19-59-01,A
> Write a single letter of your choice,2,gpt-4o,2024-05-18-19-59-01,L
> Write a single letter of your choice,0.5,gpt-3.5-turbo,2024-05-18-19-59-01,A
> Write a single letter of your choice,1.0,gpt-3.5-turbo,2024-05-18-19-59-01,G
> Write a single letter of your choice,2,gpt-3.5-turbo,2024-05-18-19-59-01,E


## License

This project is licensed under the terms of the MIT license.

## Todo

* Add parameters:
  * Seeds
  * Frequency penalties
  * Presence penalties
  * Top p
* Implement APIs for other services other than OpenAI
* Implement JSON mode and function calling.
* DeepEval integration: <https://github.com/confident-ai/deepeval>


