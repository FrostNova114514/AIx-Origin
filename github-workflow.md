# GitHub Collaboration Workflow

This project contains a Django backend, MySQL database, and Vue/Vite frontend.

## What Goes To GitHub

Commit these files:

- Django source code: `aixorigin/`, `website/`
- Vue source code: `frontend/src/`, `frontend/public/`
- Dependency files: `requirements.txt`, `frontend/package.json`, `frontend/package-lock.json`
- Database migrations: `website/migrations/*.py`
- Project docs: `README.md`, `docs/`
- Example environment file: `.env.example`

Do not commit these files:

- `.env`
- `.venv/`
- `frontend/node_modules/`
- `frontend/dist/`
- `db.sqlite3`
- `media/`
- `backups/`
- `.base` exports
- `.sql` or database backup files
- real participant data

## Recommended Repository Setup

Create the Git repository inside this project folder:

```bash
cd "/Users/frostnova/AIxOrigin Website"
git init
git add .
git commit -m "Initial AIx Origin website"
```

Use a private GitHub repository unless all sensitive data has been removed.

## Branch Rules

Use `main` as the stable branch.

Common branch names:

- `feature/application-form`
- `feature/admin-dashboard`
- `fix/application-submit`
- `content/update-sponsors`
- `deploy/server-config`

Avoid pushing directly to `main`. Each collaborator should create a branch, push it, and open a pull request.

## Daily Workflow

Before starting work:

```bash
git checkout main
git pull
git checkout -b feature/your-change
```

After making changes:

```bash
python manage.py check
cd frontend
npm run build
cd ..
git status
git add .
git commit -m "Describe the change"
git push origin feature/your-change
```

Then open a pull request on GitHub.

## Pull Request Checklist

Before merging:

- Django check passes
- Vue build passes
- No `.env` or password files are included
- No participant data is included
- Migrations are included when models change
- Application form still submits correctly
- Django admin `/admin/` still opens

## Deployment Flow

Recommended server update flow:

```bash
cd /www/wwwroot/aixorigin
git pull
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
cd frontend
npm install
npm run build
```

Then restart the Django service and reload Nginx from the server panel.

## Environment Variables

Each machine should have its own `.env`.

Keep `.env.example` updated with variable names, but never put real passwords inside it.

Example:

```bash
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,47.79.17.48,aixorigin.innoaixhku.top
CSRF_TRUSTED_ORIGINS=https://aixorigin.innoaixhku.top
MYSQL_DATABASE=aixorigin
MYSQL_USER=aixorigin
MYSQL_PASSWORD=change-me
MYSQL_SOCKET=/tmp/mysql.sock
```

## Data Policy

Participant data belongs in MySQL, not GitHub.

For backups, export database files to a private storage location. Do not commit `.sql`, `.base`, or uploaded resumes into the repository.
