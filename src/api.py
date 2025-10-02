from fastapi import FastAPI
from fitness.crew import Fitness
from fitness.prompt import FitnessPrompt
from fastapi.middleware.cors import CORSMiddleware    

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/fitness-plan")
def get_fitness_plan(request: FitnessPrompt):
    try:  
        
        inputs = {

            "topic": request
            .make_prompt(instruction="you are fitness expert, give me a diet plan and exercise plan to achieve my fitness goal. Be specific and detailed.Please return the output in strict Text format, no extra markdown or text."),
            
            }
        


        
        response = Fitness().crew().kickoff(inputs=inputs).raw
        
    
        return {"fitness_plan": response}
    except Exception as e:
        return {"error": str(e)}