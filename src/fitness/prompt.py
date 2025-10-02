from pydantic import BaseModel




alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
Sex: {Sex}
Age: {Age}
Height: {Height}
Weight: {Weight}
Hypertension: {Hypertension}
Diabetes: {Diabetes}
Fitness Goal: {Fitness_Goal}

### Response:
"""

 
   
    

class FitnessPrompt(BaseModel):
    Sex: str
    Age: int
    Height: float
    Weight: float
    Hypertension: str
    Diabetes: str
    Fitness_Goal: str

    def make_prompt(self, instruction: str) -> str:
        return alpaca_prompt.format(
            instruction=instruction,
            Sex=self.Sex,
            Age=self.Age,
            Height=self.Height,
            Weight=self.Weight,
            Hypertension=self.Hypertension,
            Diabetes=self.Diabetes,
            Fitness_Goal=self.Fitness_Goal,
        )





