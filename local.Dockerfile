# First stage: Install dependencies
FROM python:3.12.0-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --user -r requirements.txt
ENV PATH=/root/.local/bin:$PATH
