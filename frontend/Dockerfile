# Dockerfile for Frontend
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy HTML, CSS, and JS files to the Nginx web root
COPY templates /usr/share/nginx/html
# COPY static /usr/share/nginx/html/static
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
