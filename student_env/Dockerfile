FROM ubuntu:22.04

# Install OpenSSH and create a user
RUN apt-get update && \
    apt-get install -y openssh-server sudo make gcc python3 python3-pip && \
    useradd -ms /bin/bash student && \
    echo 'student:temp' | chpasswd && \
    mkdir /var/run/sshd

# Allow password authentication
RUN sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/^PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

COPY . /home/student

ENV ADMIN_PASS="temp_pass"

WORKDIR /home/student
RUN pip install --no-cache-dir -r requirements.txt

# Start SSH
CMD ["/usr/sbin/sshd", "-D"]

