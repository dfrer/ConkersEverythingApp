import Notes from '../components/Notes';
import Link from 'next/link';

export default function NotesPage() {
  return (
    <main style={{ padding: '2rem' }}>
      <Link href="/">Back</Link>
      <Notes />
    </main>
  );
}
