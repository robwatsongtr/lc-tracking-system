
# 📘 psql Cheat Sheet

## 🔹 Connecting

### From Docker:
```bash
docker exec -it <container> psql -U <user> -d <database>
```

### From Host Machine (if Postgres is exposed):
```bash
psql -h localhost -U <user> -d <database>
```

---

## 🔹 Meta-Commands (inside `psql`)

| Command      | Description                           |
|--------------|---------------------------------------|
| `\q`         | Quit `psql`                           |
| `\c <db>`    | Connect to another database           |
| `\l`         | List all databases                    |
| `\dt`        | List all tables                       |
| `\d <table>` | Describe a table                      |
| `\du`        | List users and roles                  |
| `\dn`        | List schemas                          |
| `\df`        | List functions                        |
| `\x`         | Toggle expanded output                |
| `\?`         | Help on `psql` commands               |
| `\h <cmd>`   | SQL syntax help (e.g., `\h CREATE`) |

---

## 🔹 SQL Basics

```sql
-- Create table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- Insert rows
INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com'),
       ('Bob', 'bob@example.com');

-- Query
SELECT * FROM users;

-- Delete
DELETE FROM users WHERE name = 'Bob';

-- Drop table
DROP TABLE users;
```

---

## 🔹 Import / Export

### Run SQL from File:
```bash
psql -U <user> -d <db> -f seed.sql
```

### Export to CSV (inside `psql`):
```sql
\copy (SELECT * FROM users) TO 'users.csv' CSV HEADER;
```

### Import CSV:
```sql
\copy users(name, email) FROM 'users.csv' CSV HEADER;
```

---

## 🔹 Navigation Tips

- Use `↑ ↓` to navigate history.
- Use `Tab` for autocompletion.
