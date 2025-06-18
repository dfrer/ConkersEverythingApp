import { useEffect, useState } from 'react';

export default function Notes() {
  const [notes, setNotes] = useState<string[]>([]);
  const [text, setText] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/notes')
      .then(res => res.json())
      .then(setNotes)
      .catch(() => setNotes([]));
  }, []);

  const addNote = async () => {
    await fetch('http://localhost:8000/notes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    setText('');
    const res = await fetch('http://localhost:8000/notes');
    setNotes(await res.json());
  };

  return (
    <div>
      <h2>Notes</h2>
      <ul>
        {notes.map((n, i) => (
          <li key={i}>{n}</li>
        ))}
      </ul>
      <input
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="Write a note"
      />
      <button onClick={addNote}>Add</button>
    </div>
  );
}
