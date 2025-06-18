import { useState } from 'react';

export default function Timer() {
  const [seconds, setSeconds] = useState(0);
  const [message, setMessage] = useState('');

  const start = async () => {
    await fetch('http://localhost:8000/timer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ seconds }),
    });
    setMessage(`Timer for ${seconds} seconds started.`);
    setSeconds(0);
  };

  return (
    <div>
      <h2>Start Timer</h2>
      <input
        type="number"
        value={seconds}
        onChange={e => setSeconds(parseInt(e.target.value))}
      />
      <button onClick={start}>Go</button>
      {message && <p>{message}</p>}
    </div>
  );
}
