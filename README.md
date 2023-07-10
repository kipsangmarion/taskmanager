# TaskManager Django Project

TaskManager is a Django project that provides APIs for managing tasks, activities, comments, and user profiles. The project consists of two apps: `taskmaster` and `internals`. 

## Features

- CRUD operations for tasks, activities, comments, and user profiles.
- Integration with the default Django user model for user authentication.
- SQLite database for storing data.

## Installation

1. Clone the repository:

   ```shell
   https://github.com/kipsangmarion/taskmanager
   cd TaskManager
   ```

2. Set up a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate (Linux/Mac) OR venv\Scripts\activate (Windows)
   ```

3. Install the dependencies:

   ```shell
   pip install -r r.txt
   ```

4. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

5. Start the development server:

   ```shell
   python manage.py runserver
   ```

6. Access the project in your browser at `http://localhost:8000/`. You can also host the project and use it as a bankend to your applications.

## Apps

### TaskMaster

The `taskmaster` app contains the models, serializers, and APIs for managing tasks, activities, comments, and user profiles.

#### Models

- `Task`: Represents a task with fields such as `id`, `user`, `title`, `tag`, `desc`, `status`, `hours`, `created_at`, `updated_at`, `planned_start_date`, `planned_end_date`, `actual_start_date`, `actual_end_date`, and `content`.
- `Activity`: Represents an activity related to a task with fields like `id`, `task`, `title`, `desc`, `status`, `hours`, `created_at`, `updated_at`, and `content`.
- `Comment`: Represents a comment associated with a task or activity with fields such as `id`, `task`, `activity`, and `content`.
- `User`: This the default Django user model.
- `UserProfile`: Represents a user's additional data with fields such as `id`, `user`, `intro`, and `image`.

#### Serializers

- `TaskSerializer`: Serializes the `Task` model for API responses and requests.
- `ActivitySerializer`: Serializes the `Activity` model for API responses and requests.
- `CommentSerializer`: Serializes the `Comment` model for API responses and requests.
- `UserProfileSerializer`: Serializes the `UserProfile` model for API responses and requests.
- `RegisterSerializer` : Serializes the `User` model for registering API responses and requests.
- `ChangePasswordSerializer` : Serializes the `User` model for changing user password API responses and requests.

#### APIs

- `/tasks_view.py`: Provides endpoints for creating, retrieving, updating, and deleting tasks.
- `/activities_view.py`: Provides endpoints for creating, retrieving, updating, and deleting activities.
- `/comments_view.py`: Provides endpoints for creating, retrieving, updating, and deleting comments.
- `/user-profiles_view.py`: Provides endpoints for creating, retrieving, updating, and deleting user profiles.
- `/view.py` : Provides endpoints for registering users, changing password, logout and logout from all devices.

### Internals

The `internals` app contains pagination and renderers for the API responses.

#### Pagination

- `CustomPagination`: Custom pagination class for paginating API responses.

#### Renderers

- `CustomJSONRenderer`: Custom JSON renderer for API responses.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.
