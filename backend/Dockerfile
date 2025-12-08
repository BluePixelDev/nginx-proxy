FROM python

WORKDIR /backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--debug"]