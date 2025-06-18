import Link from 'next/link';

export default function Home() {
  return (
    <main style={{ padding: '2rem' }}>
      <h1>Conker\'s Everything App</h1>
      <ul>
        <li><Link href="/notes">Notes</Link></li>
        <li><Link href="/timers">Timers</Link></li>
      </ul>
    </main>
  );
}
