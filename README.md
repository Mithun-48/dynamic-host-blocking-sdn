# Dynamic Host Blocking System using SDN (POX)

## Project Overview

Dynamic Host Blocking System is a Software Defined Networking (SDN) based security solution built using the POX controller and Mininet.

It demonstrates core networking concepts including:

* Centralized network control using SDN
* Dynamic traffic monitoring and analysis
* Flow-based blocking using OpenFlow rules

This project provides a practical understanding of SDN architecture, controller-based decision making, and real-time network security enforcement.

---

## Features

### Network Topology

* Custom network topology built using Mininet
* Multiple hosts and switches connected
* Traffic flows managed through a centralized controller

### Dynamic Host Blocking

* Controller monitors incoming packets
* Detects suspicious or unwanted hosts
* Dynamically installs flow rules to block traffic

### Controller Logic

* Implemented using POX controller
* Handles packet-in events from switches
* Applies decision logic for blocking hosts

---

## Project Structure

```
dynamic-host-blocking-sdn/
│── dynamic_block_pox.py
│── topology/
│    └── topo.py
│── generate_topology_pdf.py
│── topology.pdf
│── README.md
```

---

## Build, Load & Set Instructions

###  Start POX Controller

```
cd pox
./pox.py misc.dynamic_block_pox
```

####  Output:
<img width="893" height="737" alt="WhatsApp Image 2026-04-22 at 10 00 01 AM" src="https://github.com/user-attachments/assets/843a44d1-ac25-4a30-b389-4c14c90ea067" />


---

### Run Mininet Topology

```
sudo python topology/topo.py
```

#### Output:

<img width="644" height="461" alt="WhatsApp Image 2026-04-22 at 10 02 01 AM" src="https://github.com/user-attachments/assets/f8b1fcf3-4604-461d-a11f-a7ab31df1581" />


---


## Test Network

* Use ping between hosts
* Observe traffic flow
* Controller logs packet counts
* Host gets blocked after threshold

---

## Engineering Analysis

### Packet Processing

Switches forward packets to controller when no rule exists.
Controller analyzes packets and decides actions.

### Flow Rule Installation

Controller installs rules into switches to:

* Allow traffic
* Block specific hosts

### Dynamic Blocking Logic

* Each IP is monitored
* Packet count increases
* When threshold exceeds → host is blocked

---

## Experiments and Results

* Real-time packet monitoring
* Increasing packet count per host
* Automatic blocking of malicious host
* Verified blocking through logs

---

## Technologies Used

* Python
* Mininet
* POX Controller
* OpenFlow Protocol

---

## Conclusion

This project demonstrates how SDN can dynamically monitor and secure networks by blocking malicious hosts in real-time using centralized control.

---

## Author

Mithun P Naik

---

## Notes

* Run commands using sudo where required
* Ensure POX controller is installed
* Tested on Ubuntu Linux
