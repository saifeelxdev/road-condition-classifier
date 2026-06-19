import { useState } from "react";

const API_URL = "https://road-condition-classifier-api.onrender.com/predict";
function App() {
  const [imageFile, setImageFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);

  const [prediction, setPrediction] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleImageChange = (event) => {
    const file = event.target.files[0];

    setError("");
    setPrediction(null);

    if (!file) return;

    if (!file.type.startsWith("image/")) {
      setError("Only image files are allowed.");
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      setError("Image size must be less than or equal to 10 MB.");
      return;
    }

    setImageFile(file);
    setPreviewUrl(URL.createObjectURL(file));
  };

  const handleAnalyze = async () => {
    if (!imageFile) {
      setError("Please select an image first.");
      return;
    }

    setLoading(true);
    setError("");
    setPrediction(null);

    try {
      const formData = new FormData();

      formData.append("image", imageFile);

      const response = await fetch(API_URL, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Backend request failed.");
      }

      const data = await response.json();

      setPrediction(data);
    } catch (error) {
      console.error(error);

      setError("Failed to connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#f5f5f5",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div
        style={{
          width: "550px",
          backgroundColor: "white",
          borderRadius: "12px",
          padding: "30px",
          boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
        }}
      >
        <h1
          style={{
            textAlign: "center",
            marginBottom: "10px",
          }}
        >
          Road Condition Analyzer
        </h1>

        <p
          style={{
            textAlign: "center",
            color: "#555",
          }}
        >
          Upload a road image and analyze its condition.
        </p>

        <input
          type="file"
          accept="image/*"
          onChange={handleImageChange}
          style={{
            marginTop: "20px",
            width: "100%",
          }}
        />

        {error && (
          <p
            style={{
              color: "red",
              marginTop: "15px",
            }}
          >
            {error}
          </p>
        )}

        {previewUrl && (
          <div style={{ marginTop: "20px" }}>
            <img
              src={previewUrl}
              alt="Preview"
              style={{
                width: "100%",
                borderRadius: "8px",
                border: "1px solid #ddd",
              }}
            />
          </div>
        )}

        <button
          onClick={handleAnalyze}
          disabled={loading}
          style={{
            marginTop: "20px",
            width: "100%",
            padding: "12px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
            fontSize: "16px",
          }}
        >
          {loading ? "Analyzing..." : "Analyze Road"}
        </button>

        {prediction && (
          <div
            style={{
              marginTop: "20px",
              padding: "15px",
              borderRadius: "8px",
              backgroundColor: "#f0f0f0",
            }}
          >
            <h3
              style={{
                color:
                  prediction.pred === "Road Appears Safe" ? "green" : "red",
              }}
            >
              {prediction.pred}
            </h3>

            <p>Confidence: {(prediction.confidence * 100).toFixed(1)}%</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
