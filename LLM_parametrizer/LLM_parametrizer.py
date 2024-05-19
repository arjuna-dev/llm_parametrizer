from llm_parametrizer.open_AI_models import GPT_MODEL
class LLMParametrizer:
    def initialize_OpenAI(self, openai_key=None):
        if openai_key:
            self.OPEN_AI_API_KEY = openai_key
        else:
            load_dotenv()
            self.OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
        self.client = openai.OpenAI(api_key=self.OPEN_AI_API_KEY)

