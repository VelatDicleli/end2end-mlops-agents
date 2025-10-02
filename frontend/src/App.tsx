import { useState } from "react";
import "./App.css"; 

function App() {
  const [formData, setFormData] = useState({
    Sex: "",
    Age: "",
    Height: "",
    Weight: "",
    Hypertension: "",
    Diabetes: "",
    Fitness_Goal: "",
  });

  const [fitnessPlan, setFitnessPlan] = useState<string>("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch("http://98.64.238.1/api/fitness-plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();


      setFitnessPlan(data.fitness_plan);
      alert("Form başarıyla gönderildi!");
    } catch (error) {
      console.error("Error:", error);
      alert("Bir hata oluştu!");
    }
  };

  return (
    <div className="fitness-form-container">
      <h1>FitTrack</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="Sex">Sex:</label>
          <input
            type="text"
            id="Sex"
            name="Sex"
            value={formData.Sex}
            onChange={handleChange}
            placeholder="Enter your sex"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Age">Age:</label>
          <input
            type="number"
            id="Age"
            name="Age"
            value={formData.Age}
            onChange={handleChange}
            placeholder="Enter your age"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Height">Height (cm):</label>
          <input
            type="number"
            id="Height"
            name="Height"
            value={formData.Height}
            onChange={handleChange}
            placeholder="Enter your height"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Weight">Weight (kg):</label>
          <input
            type="number"
            id="Weight"
            name="Weight"
            value={formData.Weight}
            onChange={handleChange}
            placeholder="Enter your weight"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Hypertension">Hypertension:</label>
          <input
            type="text"
            id="Hypertension"
            name="Hypertension"
            value={formData.Hypertension}
            onChange={handleChange}
            placeholder="Yes/No"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Diabetes">Diabetes:</label>
          <input
            type="text"
            id="Diabetes"
            name="Diabetes"
            value={formData.Diabetes}
            onChange={handleChange}
            placeholder="Yes/No"
          />
        </div>

        <div className="form-group">
          <label htmlFor="Fitness_Goal">Fitness Goal:</label>
          <input
            type="text"
            id="Fitness_Goal"
            name="Fitness_Goal"
            value={formData.Fitness_Goal}
            onChange={handleChange}
            placeholder="Enter your fitness goal"
          />
        </div>

        <button type="submit">Gönder</button>
      </form>


      {fitnessPlan && (
        <div className="fitness-plan-output">
          <h2>Workout & Nutrition:</h2>
          <pre>{fitnessPlan}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
