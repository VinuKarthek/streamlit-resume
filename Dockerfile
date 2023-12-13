# Use Python 3.9 base image
FROM python:3.9

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Streamlit Python file
COPY resume_app.py .

# Define an environment variable for the start command (default is streamlit command)
ENV STREAMLIT_SERVER_PORT = "8001"
ENV START_COMMAND="streamlit run resume_app.py --server.port $STREAMLIT_SERVER_PORT"

# Set the command to start the Streamlit app using the environment variable
CMD ["/bin/sh", "-c", "$START_COMMAND"]