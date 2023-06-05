<script lang="ts">
  import type { PageData } from './$types';

  export let data: PageData;
</script>

<svelte:head>
  <title>PSSt Home</title>
  <meta name="description" content="PSc Studio Home" />
</svelte:head>

<h1>PSc Studio Home</h1>

<ul>
{#each data.results as script}
  <li><a href="script/{script.id}/">{script.title}</a></li>
{/each}
</ul>
