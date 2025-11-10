# Inventory Management System

Simple inventory management system with Python Flask, HTML/CSS, and JSON storage.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open browser and go to: `http://localhost:5000`

## Features

- Add new items (auto-generated ID)
- View all inventory items
- Update existing items
- Delete items
- Data stored in `inventory.json`

## Structure

- `app.py` - Flask backend with API endpoints
- `templates/index.html` - Frontend interface
- `inventory.json` - Data storage (auto-created)
