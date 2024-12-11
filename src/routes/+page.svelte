<script>
    import { goto } from '$app/navigation';
    import { onMount } from 'svelte';

    let data = [];
    let loading = true;
    let error = null;

    // Fetch database data when the component is mounted
    onMount(async () => {
        try {
            // Replace with your actual API endpoint
            const response = await fetch('/api/data');
            if (!response.ok) throw new Error('Failed to fetch data');
            data = await response.json();
        } catch (err) {
            error = err.message;
        } finally {
            loading = false;
        }
    });

    // Navigate to other pages
    const goToDatabase = () => goto('/fromDB');
    const goToComponents = () => goto('/fromDBandComponents');
</script>

<h1>Welcome to the Simple Client/DB Site</h1>
<p>Bits and pieces to get started in Svelte and SvelteKit</p>
<p>SvelteKit using PostgreSQL for a database</p>

<p>Step 1: See how to use a PostgreSQL database</p>
<span class="note">(For this to work, you MUST create a file called `.env` at the project root with the parameter `PGCONNECT`)</span>
<br />
<button on:click={goToDatabase}>Use Database</button>

<p>Step 2: See how to create Svelte components</p>
<span class="note">(Uses database, so create the `.env` file as above)</span>
<br />
<button on:click={goToComponents}>Use Components</button>

<hr />

<h1>Database Data Table</h1>
{#if loading}
    <p>Loading...</p>
{:else if error}
    <p>Error: {error}</p>
{:else if data.length === 0}
    <p>No data found in the database.</p>
{:else}
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
            {#each data as row}
                <tr>
                    <td>{row.id}</td>
                    <td>{row.name}</td>
                    <td>{row.value}</td>
                </tr>
            {/each}
        </tbody>
    </table>
{/if}

<a href="/brucetest1">Check out the new page</a>

<style>
    .note {
        font-style: italic;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    tr:nth-child(even) {
        background-color: #f9f9f9;
    }

    tr:hover {
        background-color: #f1f1f1;
    }
</style>