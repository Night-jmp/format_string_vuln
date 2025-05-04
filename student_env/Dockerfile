FROM ubuntu:22.04

# Install OpenSSH and create a user
RUN apt-get update && \
    apt-get install -y openssh-server sudo make gcc python3 python3-pip net-tools vim && \
    useradd -ms /bin/bash student && \
    echo 'student:l!f3_l0ng_l34rn3r' | chpasswd && \
    mkdir /var/run/sshd

# Allow password authentication
RUN sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/^PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

COPY . /home/student

RUN echo 'export ADMIN_PASS=temp_pass' >> /etc/profile.d/admin_env.sh

WORKDIR /home/student
RUN chown -R student:student /home/student
RUN chmod +x exploit_read.py

RUN pip install --no-cache-dir -r requirements.txt
RUN make
# Start SSH
CMD ["/usr/sbin/sshd", "-D"]

