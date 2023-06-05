import { PUBLIC_API_ROOT } from '$env/static/public';
import type { PageLoad } from './$types';

export const ssr = false; // ブラウザのみで実行

export const load = (async ({ params }) => {
	const res = await fetch(`${PUBLIC_API_ROOT}scripts/`);
	const data = await res.json();
	console.log(data);
	return data;
}) satisfies PageLoad;
