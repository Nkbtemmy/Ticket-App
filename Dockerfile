FROM python:3.12.0a3-bullseye

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file
# COPY Pipfile Pipfile.lock /app/

# # Install pipenv
# RUN pip install pipenv

# # Install dependencies
# RUN pipenv install 

# # Copy the application code
# COPY . /app

# # Run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the environment variable
ENV DJANGO_SETTINGS_MODULE=server.settings

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]