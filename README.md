# LeetCode Tracker

A lightweight backend built with **FastAPI** and **PostgreSQL** (using `databases` and raw SQL, no ORM) to track completed LeetCode problems.  

The app also serves a simple **Jinja2-based UI** for browsing, searching and managing your problem history. 

A cool feature is a randomizer that can randomly give you problems from your databse to re-solve, because that's an important way to get better. 

## Features

- ✅ Track completed LeetCode problems
- 📝 Store:
  - Problem name & link
  - Difficulty (Easy / Medium / Hard)
  - Category (Array, Linked List, Dynamic Programming, etc.)
  - Approach used (Two Pointer, Sliding Window, Binary Search, etc.)
  - Pseudocode for your solution
- 🔄 Full CRUD support
  - Create, Read, Update, Delete problems
- 🌐 FastAPI backend with clean SQL queries
- 🎨 Jinja2 UI for easy interaction

## Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Database:** PostgreSQL with [`databases`](https://www.encode.io/databases/) library  
- **Templating:** Jinja2  
- **SQL:** Raw queries (no ORM)

## Setup

### Prerequisites
- Python 3.10+
- PostgreSQL running locally or in Docker

### Installation
```bash
git clone https://github.com/yourusername/leetcode-tracker.git
cd leetcode-tracker
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
```

### Database
1. Create a PostgreSQL database:
   ```bash
   createdb leetcode_tracker
   ```
2. Run the schema SQL (provided in `app/sql/tables.sql`):
   ```bash
   psql leetcode_tracker < app/sql/tables.sql
   ```

### Run the Server
```bash
uvicorn app.main:app --reload
```

Visit: [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)
