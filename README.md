# Django Blog Project

A responsive and feature-rich blog application built with the Django framework. This project provides a robust platform for creating and managing blog posts, complete with a tagging system and search functionality.

---

## Features

* **Responsive Design:** The front-end is built using Bootstrap, ensuring the blog is fully responsive and looks great on any device, from desktops to mobile phones.
* **Post Creation:** Easily create, edit, and publish new blog posts through the Django administration panel.
* **Tags System:** Categorize your posts with a flexible tagging system, allowing users to discover related content.
* **Search Functionality:** A powerful search feature enables users to find specific posts based on keywords in the title or content.

---

## Getting Started

Follow these steps to get a local copy of the project up and running.

### Prerequisites

* Python (3.8 or higher)
* pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```
    git clone [https://github.com/ShayanHosseinzadeh/Django_blog_project.git]
    cd Django_blog_project
    ```

2.  **Create a virtual environment:**

    ```
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    * On macOS/Linux:

        ```
        source venv/bin/activate
        ```

    * On Windows:

        ```
        venv\Scripts\activate
        ```

4.  **Install dependencies:** The `requirements.txt` file is already in the repository.

    ```
    pip install -r requirements.txt
    ```

5.  **Run database migrations:**

    ```
    python manage.py migrate
    ```

6.  **Create a superuser:** This will allow you to access the Django admin panel to create blog posts.

    ```
    python manage.py createsuperuser
    ```

    Follow the prompts to create your superuser account.

7.  **Run the development server:**

    ```
    python manage.py runserver
    ```

8.  Open your browser and navigate to `http://127.0.0.1:8000/` to view the blog. You can access the admin panel at `http://127.0.0.1:8000/admin/` to create new posts.

---

## Usage

### Creating a New Post

1.  Log in to the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser account you created.
2.  Navigate to the `Posts` section and click "Add Post."
3.  Fill in the post details, add tags, and publish your content.

---

## Technologies Used

* **Django:** The core web framework.
* **Python:** The programming language.
* **Bootstrap:** For a responsive and modern front-end.
* **SQLite:** The database backend.

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
