FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy only the requirements file, to leverage Docker cache
COPY requirements.txt ./

# Install Python dependencies without storing cache, to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Run the application when the container launches
CMD [ "python", "./pipeline.py" ]
