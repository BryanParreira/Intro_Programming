class LLM:
    def __init__(self, name, token_limit):
        self.name = name
        self.token_limit = token_limit

    def get_token_limit(self):
        return self.token_limit

    def set_token_limit(self, token_limit):
        self.token_limit = token_limit

    def __str__(self):
        return f"{self.name} (token limit: {self.token_limit})"


class AICompany:
    def __init__(self, company_name, founding_year):
        self.company_name = company_name
        self.founding_year = founding_year
        self.headquarters = ""  # set later with set_headquarters
        self.llms = []

    def get_headquarters(self):
        return self.headquarters

    def set_headquarters(self, headquarters):
        self.headquarters = headquarters

    def add_llm(self, llm):
        self.llms.append(llm)

    def display_models(self):
        for llm in self.llms:
            print(llm)

    def __str__(self):
        return f"{self.company_name} (founded {self.founding_year}, {len(self.llms)} models)"


company = AICompany("Anthropic", 2021)
company.set_headquarters("San Francisco")
company.add_llm(LLM("Claude Sonnet", 200000))
company.add_llm(LLM("Claude Haiku", 100000))
print(company)
company.display_models()
