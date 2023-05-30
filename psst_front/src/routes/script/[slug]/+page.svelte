<script lang="ts">
  import type { PageData } from './$types';

  export let data: PageData;
</script>

<svelte:head>
  <title>PSSt Script</title>
  <meta name="description" content="PSc Studio Script" />
</svelte:head>

<h1>PSc Studio Script</h1>

<p>title: {data.title}</p>
<p>plot: {data.plot}</p>
