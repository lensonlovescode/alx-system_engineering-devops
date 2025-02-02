## 0x0F-load_balancer

This project involves setting up a redundant web infrastructure to improve
reliability and handle increased traffic. A load balancer will be used to distribute
requests between multiple web servers, ensuring high availability and failover support.

# Tasks

1. Configure an additional web server to serve requests.
2. Set up a load balancer to distribute traffic.
3. Automate the configuration using Bash scripts.

# Technologies Used

1. Ubuntu 16.04 LTS
2. HAProxy (for load balancing)
3. Bash scripting (for automation)

# Requirements

1. Scripts must configure a new Ubuntu server from scratch.
2. All Bash scripts must be executable and pass Shellcheck (v0.3.7) without errors.
3. The first line of each script must be #!/usr/bin/env bash.
4. All files must be interpreted on Ubuntu 16.04 LTS.
