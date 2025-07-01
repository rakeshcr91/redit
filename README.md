# Community Portal

This is a simple Reddit-style community portal built with Flask. Features include:

- User registration and login
- Create posts with optional links
- Upvote and downvote posts
- Posts ordered by score on the feed

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Initialize the database:

```bash
flask --app wsgi db init
flask --app wsgi db migrate -m "Initial"
flask --app wsgi db upgrade
```

3. Run the development server:

```bash
flask --app wsgi run
```

Tailwind CSS can be built using npm:

```bash
npm install
npm run build
```

## Environment Variables

Copy `.env.example` to `.env` and adjust as needed.

## License

MIT
