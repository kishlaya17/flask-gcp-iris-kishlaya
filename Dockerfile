FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (for caching)
COPY requirementss.txt .
RUN pip install --no-cache-dir -r requirementss.txt

# Copy entire project
COPY . .

EXPOSE 5050

CMD ["gunicorn", "-b", "0.0.0.0:5050", "app.main:app"]
