import { useState, useRef } from "react";
import api from "../api.js";

function Form() {
    const [selectedFile, setSelectedFile] = useState(null)
    const [downloadUrl, setDownloadUrl] = useState("")
    const fileInputRef = useRef(null);

    const postData = async (data) => {
        try {
            const response = await api.post(
                '/api/requests/', data,
                { headers: { "Content-Type": "multipart/form-data" } }
            );
            setDownloadUrl(response.data['download_url'])
            console.log("Response:", response.data);
        } catch (error) {
            console.error("Error posting data:", error);
        }
    };


    const handleUpload = (e) => {
        e.preventDefault()
        if (selectedFile) {
            const formData = new FormData();
            formData.append('zip_file', selectedFile);

            postData(formData)
            setSelectedFile(null)

            if (fileInputRef.current) {
                fileInputRef.current.value = null;
            }
        }
    }

    const isDownload = downloadUrl !== "";

    return (
        <div className="form-container">
            <div className="pop-up page">
                <form onSubmit={handleUpload}>
                    <h2>Generate Your README.md</h2>
                    <label htmlFor="">Upload .zip file for your code</label>
                    <input type="file" accept=".zip" ref={fileInputRef} onChange={(e) => setSelectedFile(e.target.files[0])} />
                    <button className={isDownload ? "download-btn" : "generate-btn"} type="submit">{isDownload ? <a href={downloadUrl} onClick={() => setDownloadUrl("")}>Download</a> : "Generate"}</button>
                </form>
            </div>
        </div>
    )
}

export default Form;