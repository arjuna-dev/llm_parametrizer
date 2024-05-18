from enum import Enum

class GPT_MODEL(Enum):
    # GPT-4
    GPT_4_T = "gpt-4-turbo" # Points to a specific version of GPT-4 Turbo
    GPT_4_T_V = "gpt-4-turbo-2024-04-09" # SUpports vision and JSON mode
    GPT_4_T_P1 = "gpt-4-turbo-preview" # Points to a specific preview version of GPT-4 Turbo
    GPT_4_T_P2 = "gpt-4-0125-preview" # GPT-4 Turbo preview model intended to reduce cases of “laziness” where the model doesn’t complete a task.
    GPT_4_T_P3 = "gpt-4-1106-preview" # GPT-4 Turbo preview model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. 
    GPT_4_V = "gpt-4-vision-preview" # GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities.
    GPT_4_V_P = "gpt-4-1106-vision-preview" # GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. 
    GPT_4 = "gpt-4" # Points to a specific version of GPT-4
    GPT_4_1 = "gpt-4-0613" # Snapshot of gpt-4 from June 13th 2023 with improved function calling support
    GPT_4_32 = "gpt-4-32k" # Points to a specific version of GPT-4-32k
    GPT_4_32_1 = "gpt-4-32k-0613" # Snapshot of gpt-4-32k from June 13th 2023 with improved function calling support. This model was never rolled out widely in favor of GPT-4 Turbo
    # GPT-4o
    GPT_4o = "gpt-4o" # Points to a specific version of GPT-4o
    GPT_4o_1 = "gpt-4o-2024-05-13" # gpt-4o v1
    # GPT-3.5
    GPT_3_5_T_1 = "gpt-3.5-turbo-0125" # New Updated GPT 3.5 Turbo
    GPT_3_5_T = "gpt-3.5-turbo" # Points to a specific version of GPT-3.5 Turbo
    GPT_3_5_T_P1 = "gpt-3.5-turbo-1106" # GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling.
    GPT_3_5_T_I = "gpt-3.5-turbo-instruct" # Similar capabilities as GPT-3 era models. Compatible with legacy Completions endpoint and not Chat Completions.
    GPT_3_5_T_16 = "gpt-3.5-turbo-16k" # Legacy Currently points to gpt-3.5-turbo-16k-0613.
    GPT_3_5_T_16_1 = "gpt-3.5-turbo-0613" # Legacy Snapshot of gpt-3.5-turbo from June 13th 2023. Will be deprecated on June 13, 2024.
    GPT_3_5_T_16_2 = "gpt-3.5-turbo-16k-0613" # Legacy Snapshot of gpt-3.5-16k-turbo from June 13th 2023. Will be deprecated on June 13, 2024.
