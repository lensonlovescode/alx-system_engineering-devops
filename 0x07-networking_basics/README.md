0x07. Networking Basics #0
Overview
This directory covers the basics of networking as part of the DevOps foundations, focusing on key concepts essential for understanding network structure, communication, and protocols. By mastering these basics, you will build a strong foundation for more advanced networking topics used in system administration, network configuration, and development.

Topics Covered
1. OSI Model
The OSI (Open Systems Interconnection) model is a conceptual framework used to understand network interactions across seven layers:

Layer 1: Physical Layer - Deals with hardware and the physical connection.
Layer 2: Data Link Layer - Manages node-to-node data transfer and error handling.
Layer 3: Network Layer - Handles IP addressing and routing (e.g., IP, ARP).
Layer 4: Transport Layer - Manages end-to-end communication, flow control, and error checking (e.g., TCP, UDP).
Layer 5: Session Layer - Establishes, manages, and terminates sessions between applications.
Layer 6: Presentation Layer - Formats or translates data for the application layer.
Layer 7: Application Layer - Where network services and applications operate (e.g., HTTP, FTP).
2. IP Addresses and Types
IP addresses are unique identifiers assigned to devices on a network, crucial for routing and communication:

IPv4: 32-bit address written as four decimal numbers (e.g., 192.168.1.1).
IPv6: 128-bit address, written in hexadecimal (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
Types:
Public IP: Routable on the internet, unique globally.
Private IP: Used within local networks (e.g., 192.168.x.x, 10.x.x.x), non-routable on the internet.
Static IP: Manually assigned, remains fixed.
Dynamic IP: Assigned automatically by DHCP, may change.
3. Protocols
Networking relies on protocols to ensure data integrity and manage connections:

TCP (Transmission Control Protocol): Reliable, connection-oriented protocol used for data integrity and sequencing.
UDP (User Datagram Protocol): Faster, connectionless protocol used for real-time data, where speed is prioritized over reliability (e.g., video streaming).
ICMP (Internet Control Message Protocol): Used for sending error messages and diagnostic tools like ping and traceroute.
4. Ports and Sockets
Port Numbers: Logical endpoints for network applications on a device, ranging from 0 to 65535.
Common Ports: HTTP (80), HTTPS (443), SSH (22), FTP (21).
Socket: Combination of IP address and port number, creating a unique communication channel.
5. DNS (Domain Name System)
DNS translates domain names (like example.com) into IP addresses. This decentralized system allows devices to look up IP addresses associated with human-readable names, enabling easy access to resources on the internet.

6. Network Address Translation (NAT)
NAT allows multiple devices on a LAN to share a single public IP address for internet access, conserving IP addresses and providing a layer of security by hiding internal IPs from external networks.

7. DHCP (Dynamic Host Configuration Protocol)
DHCP automatically assigns IP addresses and network settings (e.g., subnet mask, gateway) to devices on a network, simplifying network management.

Key Commands and Tools
ping: Sends ICMP Echo Requests to check if a device is reachable on the network.
traceroute/tracert: Displays the path packets take to reach a destination.
netstat: Provides network statistics, such as active connections and listening ports.
ifconfig/ipconfig: Displays and configures network interface settings.
nslookup: Queries DNS servers to find IP address information for a domain.
curl: Fetches data from
