import { useEffect, useState } from "react";
import axios from "axios";

const API = "https://bf106xk058.execute-api.us-east-1.amazonaws.com/prod";

export default function AdminDashboard() {
  const [attendance, setAttendance] = useState([]);

  useEffect(() => {
    loadAttendance();
  }, []);

  async function loadAttendance() {
    try {
      const response = await axios.get(`${API}/attendance/all`);
      setAttendance(response.data);
    } catch (err) {
      console.error(err);
      alert("Failed to load attendance");
    }
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>Admin Dashboard</h1>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Employee ID</th>
            <th>Date</th>
            <th>Clock In</th>
            <th>Clock Out</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {attendance.map((item, index) => (
            <tr key={index}>
              <td>{item.employee_id}</td>
              <td>{item.date}</td>
              <td>{item.clock_in}</td>
              <td>{item.clock_out}</td>
              <td>{item.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
