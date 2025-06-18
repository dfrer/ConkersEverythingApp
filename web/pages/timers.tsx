import Timer from '../components/Timer';
import Link from 'next/link';

export default function TimersPage() {
  return (
    <main style={{ padding: '2rem' }}>
      <Link href="/">Back</Link>
      <Timer />
    </main>
  );
}
