# Quizo

Quizo is a Django-based web application that provides an interactive and engaging quiz platform. Users can explore a variety of quizzes, test their knowledge across different topics, and enjoy a user-friendly interface with dynamically generated quiz content.

![image](https://github.com/user-attachments/assets/2c62e15e-109c-4ee0-a867-e558afafaed0)


Live Demo: [Quizo on Railway](https://quizo-production.up.railway.app/)

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Browse Quizzes**: Explore quizzes across multiple categories.
- **Interactive Questions**: Answer questions interactively and get immediate feedback.
- **User Progress Tracking**: Track your progress and review your scores.
- **Admin Dashboard**: Manage quizzes, questions, and categories (accessible by admins).
- **Responsive Design**: Enjoy a seamless experience on both desktop and mobile.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: Postgresql
- **Hosting**: Railway

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/quizo.git
   cd quizo
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database**:
   Update your database settings in `settings.py` to match your MySQL configuration.

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

Access the application at `http://127.0.0.1:8000`.

## Usage

1. **Explore Quizzes**: Visit the homepage to see available quizzes.
2. **Take a Quiz**: Start a quiz, answer the questions, and see your score.
3. **Admin Management**: As an admin, log in to manage quizzes, questions, and categories.

## Contributing

Contributions are welcome! If you'd like to improve Quizo, please fork the repository and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FeatureName`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/FeatureName`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
