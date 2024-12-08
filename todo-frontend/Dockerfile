# Stage 1: Build
FROM node:20-alpine as builder

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install --legacy-peer-deps

# Copy source code and build
COPY . ./
RUN npm run build

# Stage 2: Serve
FROM nginx:stable-alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/out /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
