import Webcam from "react-webcam";
import { useRef, useState } from "react";
import { uploadImage } from "../services/api";

export default function Camera() {
  const webcamRef = useRef(null);
  const [image, setImage] = useState(null);

  const capture = async () => {
    if (!webcamRef.current) {
      alert("Webcam not ready");
      return;
    }

    const screenshot = webcamRef.current.getScreenshot();

    if (!screenshot) {
      alert("Capture Failed");
      return;
    }

    setImage(screenshot);

    try {
      const key = await uploadImage(screenshot);
      console.log("Uploaded:", key);
      alert("Uploaded Successfully");
    } catch (err) {
      console.error(err);
      alert("Upload Failed");
    }
  };

  return (
    <div style={{ textAlign: "center" }}>
      <Webcam
        ref={webcamRef}
        audio={false}
        screenshotFormat="image/jpeg"
        width={500}
      />

      <br /><br />

      <button onClick={capture}>
        Capture Face
      </button>

      {image && (
        <>
          <h3>Captured Image</h3>
          <img src={image} width="300" alt="Captured" />
        </>
      )}
    </div>
  );
}

