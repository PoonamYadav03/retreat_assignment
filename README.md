# retreat_assignment
Django Assignment for Retreat

# Step 1: Clone the Project (if not already done)
### If the Django project is not already on your local machine, clone it from the repository where it's hosted using Git:

#### git clone <repository_url>
#### Replace <repository_url> with the actual URL of your project repository.

# Step 2: Navigate to Project Directory
### Navigate into the project directory:

    1.cd <project_name>
    2.Replace <project_name> with the name of your Django project directory.

# Step 3: Create and Activate Virtual Environment (Optional but Recommended)
### If you prefer using a virtual environment, create and activate it using:
    1.python -m venv env

# Replace myenv with your preferred name for the virtual environment.
#### Activate the virtual environment:
    1.On macOS/Linux:source myenv/bin/activate
    2.On Windows:myenv\Scripts\activate

# Step 4: Install Project Dependencies
### Install the project dependencies listed in the requirements.txt file using pip:
    1.pip install -r requirements.txt
This command will install all the required packages specified in the requirements.txt file.


# Step 5: Run Migrations
### Apply database migrations to create necessary database tables: 
    1.python manage.py makemigration
    2.python manage.py migrate


# Step 6: Create a Superuser (Optional)
### If you need to access the Django admin interface, create a superuser: 
    1.python manage.py  createsuperuser
#### Follow the prompts to set a username, email, and password.

# Step 7: Run the Development Server
### Start the Django development server: 
    1.python manage.py runserver

#### Visit http://localhost:8000 in your web browser to see your Django project running.

# Step 8: Test the API Endpoints using Postman
    1.Create a Retreat
    2.Open Postman.
    3.Create a new request.
    4.Set the method to POST.
    5.Set the endpoint URL to /api/retreats/

# Step 9: Retrieve All Retreats with Search and Filters
    1.Set the method to GET.
    2.Set the endpoint URL to /api/retreats/

### Query Parameters: ###
    1.page: Page number for pagination (default: 1)
    2.items: Number of items per page (default: 10)
    3.location: Filter by location (optional)
    4.search: Search query for filtering retreats (optional)
    5.filter: Additional filter query (optional)
    6.Send the request and verify the response.

# Step 10: Create a Booking
    1.Set the method to POST.
    2.Set the endpoint URL to /api/bookings/

# Step 11: Retrieve All Bookings
    1.Set the method to GET.
    2.Set the endpoint URL to /api/bookings/.
    3.Send the request and verify the response.
