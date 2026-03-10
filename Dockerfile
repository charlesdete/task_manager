# syntax=docker/dockerfile:1

########################################
# Stage 1: Python (Django backend)
########################################
ARG PYTHON_VERSION=3.12.6
FROM python:${PYTHON_VERSION}-slim AS django

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# create directories Django expects
RUN mkdir -p /app/static /app/staticfiles /app/media

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000"]

########################################
# Stage 2: Node.js (React frontend build)
########################################
FROM node:20-alpine AS react-build

WORKDIR /app

COPY taskflow-manager/package*.json ./
RUN npm install

COPY taskflow-manager/ ./
RUN npm run build

########################################
# Stage 3: Nginx (Serve React)
########################################
FROM nginx:stable-alpine AS nginx

RUN apk update && apk upgrade --no-cache

COPY --from=react-build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

