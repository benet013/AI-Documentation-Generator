import { useState } from "react";
import api from "../api.js";

function Form() {
    const [inputValue, setInputValue] = useState("");

    const postUrl = async (url) => {
        try {
            const response = await api.post('/api/requests/', { url });
            console.log("Response:", response.data);
        }
        catch (error) {
            console.error("Error posting URL:", error);
        }
    }

    const validateUrl = (url) => {
        const urlPattern = /^(https?:\/\/)?(www\.)?(github\.com|gitlab\.com)\/.+$/i;
        return urlPattern.test(url);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if (inputValue.trim() === "") return;
        if (!validateUrl(inputValue)) {
            alert("Please enter a valid GitHub or GitLab repository URL.");
            return;
        }
        
        postUrl(inputValue);
        setInputValue("");
        console.log("Form submitted", inputValue);
    }

    return (
        <div className="form-container">
            <form onSubmit={handleSubmit}>
                <h2>Generate Your README.md</h2>
                    <input type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} placeholder="Enter your Repository Url"/>
                    <button type="submit">Generate</button>
            </form>
        </div>
    )
}

export default Form;