# First stage: Install dependencies
FROM python:3.12.0-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Second stage: Copy installed packages and your code
FROM python:3.12.0-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure scripts in .local are callable
ENV PATH=/root/.local/bin:$PATH
