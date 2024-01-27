# Use the official GCC image as the base image
FROM gcc:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the source code and cxxopts header into the container
COPY lasercuttersubmarine.cpp /app/
COPY cxxopts.hpp /usr/include/

# Compile the C++ code and create the executable
RUN g++ -I/usr/include/ lasercuttersubmarine.cpp -o lasercuttersubmarine

# CMD specifies the command to run on container startup
CMD ["./lasercuttersubmarine"]
