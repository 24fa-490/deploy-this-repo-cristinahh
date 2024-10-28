
import postgres from 'postgres'

// see env variables in .env
const PGCONNECT = process.env.PGCONNECT;

const sql = postgres(PGCONNECT, {} )

export default sql;
