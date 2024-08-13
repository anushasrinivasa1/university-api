
# University API

This is a RESTful API for managing students and courses in a university. It allows you to create students, create courses, assign courses to students, and retrieve the courses a student has taken.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running with Docker](#running-with-docker)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized setup)
- Docker Compose (optional, for containerized setup)

### Without Docker

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/anushasrinivasa1/university-api.git
   cd university-api
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. **Start the Application:**

   ```bash
   python app.py
   ```

   The application will run on [http://localhost:5000](http://localhost:5000).

### API Endpoints

- **Home Endpoint**

  - **GET** `/`
  - Returns a welcome message.

- **Create Student**

  - **POST** `/students`
  - **Body:** JSON
    ```json
    {
      "first_name": "John",
      "last_name": "Doe"
    }
    ```
  - **Response:** Returns the created student with ID.

- **Create Course**

  - **POST** `/courses`
  - **Body:** JSON
    ```json
    {
      "course_name": "Introduction to Python",
      "course_code": "PY101",
      "description": "A beginner's course in Python."
    }
    ```
  - **Response:** Returns the created course with ID.

- **Assign Course to Student**

  - **POST** `/students/<student_id>/courses`
  - **Body:** JSON
    ```json
    {
      "course_id": 1
    }
    ```
  - **Response:** Confirmation message of course assignment.

- **Get Student Courses**

  - **GET** `/students/<student_id>/courses`
  - **Response:** List of courses assigned to the student.

## Running with Docker

1. **Build and Run the Docker Container:**

   ```bash
   docker-compose up --build
   ```

   The application will run on [http://localhost:5000](http://localhost:5000) inside the Docker container.

## Testing

You can test the API using tools like Postman or curl. Follow the instructions in the [API Endpoints](#api-endpoints) section to make requests and check responses.

## Contributing

Feel free to open issues or submit pull requests. Please follow the existing code style and add tests for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
