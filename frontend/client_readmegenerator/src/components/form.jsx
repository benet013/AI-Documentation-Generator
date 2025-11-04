import { useState } from "react";
import api from "../api.js";

function Form() {
    const [inputValue, setInputValue] = useState("");
    const [selectedFile, setSelectedFile] = useState(null)

    const postData = async (data, isFile = false) => {
        try {
            const response = await api.post(
                '/api/requests/',
                isFile ? data : { data },
                isFile
                    ? { headers: { "Content-Type": "multipart/form-data" } }
                    : {}
            );
            console.log("Response:", response.data);
        } catch (error) {
            console.error("Error posting data:", error);
        }
    };
    const validateUrl = (url) => {
        const urlPattern = /^(https?:\/\/)?(www\.)?(github\.com|gitlab\.com)\/.+$/i;
        return urlPattern.test(url);
    }

    const handleUpload = (e) => {
        e.preventDefault()
        if (selectedFile) {
            const formData = new FormData();
            formData.append('zip_file', selectedFile);

            postData(formData, true)
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        if (inputValue.trim() === "") return;
        if (!validateUrl(inputValue)) {
            alert("Please enter a valid GitHub or GitLab repository URL.");
            return;
        }

        postData(inputValue);
        setInputValue("");
        console.log("Form submitted", inputValue);
    }

    return (
        <div className="form-container">
            <form onSubmit={selectedFile === null ? handleSubmit : handleUpload}>
                <h2>Generate Your README.md</h2>
                <input type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} placeholder="Enter your Repository Url" />
                <input type="file" accept=".zip" onChange={(e) => setSelectedFile(e.target.files[0])} />

                <button type="submit">Generate</button>
            </form>
        </div>
    )
}

export default Form;