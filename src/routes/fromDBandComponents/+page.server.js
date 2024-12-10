
import sql from '$lib/server/database';

export async function load() {
    const rows = sql`
    SELECT
        containernumber,
        nameofship,
        containersize,
        datecontainershipped
    FROM
        containers`;

    console.log({rows});

    return { containers: rows };
}

