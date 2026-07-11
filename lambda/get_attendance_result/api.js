import axios from "axios";

const API =
  "https://bf106xk058.execute-api.us-east-1.amazonaws.com/prod";

export async function uploadImage(image) {
  const response = await axios.post(`${API}/upload-url`);

  const { uploadUrl, key } = response.data;

  const blob = await (await fetch(image)).blob();

  await axios.put(uploadUrl, blob, {
    headers: {
      "Content-Type": "image/jpeg",
    },
  });

  return key;
}

export async function getAttendance() {
  const response = await axios.get(`${API}/attendance`);
  return response.data;
}
