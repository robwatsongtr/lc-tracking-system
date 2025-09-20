# Claude Code Configuration

## Project Overview
LeetCode Tracking System - FastAPI + PostgreSQL application for tracking completed LeetCode problems.

## Development Commands

### Running the Application
```bash
# Local development
uvicorn app.main:app --reload

# Docker development
docker-compose up --build
```

### Database
```bash
# Connect to PostgreSQL in Docker
docker exec -it lc-tracking-system-db-1 psql -U fastapi_user -d fastapi_db

# Run schema
psql leetcode_tracker < app/sql/tables.sql
```

## Code Standards

### API Route Handlers
- Use clean function names without "_handler" suffix
- JSON endpoints: `get_problems()`, `create_problem()`, etc.
- Template handlers: `create_problem_form()`, `show_problem_form()`, etc.

### Template Naming
- Use consistent plural naming: `problems_*.html`, `categories_*.html`
- Forms: `problems_create.html`, `problems_edit.html`
- Lists: `problems_list.html`, `categories_list.html`

### Service Layer
- Descriptive function names: `list_problems()`, `get_problem_by_id()`
- Raw SQL queries (no ORM)
- Async/await pattern

## Architecture
```
app/
├── main.py              # FastAPI app & router setup
├── db.py                # Database connection
├── models/              # Pydantic models
├── routes/              # API endpoints
├── services/            # Business logic & DB operations
├── templates/           # Jinja2 HTML templates
└── sql/                 # Database schema & queries
```