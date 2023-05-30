import type { PageLoad } from './$types';

export const ssr = false; // ブラウザのみで実行

export const load = (async ({ params }) => {
	const res = await fetch('http://localhost:8000/scripts/1/');
	const data = res.json();
	console.log(data);
	return data;
}) satisfies PageLoad;
