# 🔐 Firewall Rule Simulator

A Flask-based web application that simulates how a firewall filters network traffic using rule-based logic.

## 🚀 Overview
This project demonstrates how firewalls inspect incoming packets and decide whether to **ALLOW** or **DENY** traffic based on rules. It follows real-world concepts like CIDR-based IP matching, protocol filtering, and default deny (Zero Trust).

## 🛠️ Features
- Packet filtering based on:
  - Protocol (TCP / ANY)
  - Source IP (CIDR supported)
  - Destination IP
  - Port
- Rule-based decision system (first match wins)
- Default **DENY ALL** policy
- Displays matched rule
- Simple web interface using Flask

## 🧠 How It Works
1. User enters packet details (protocol, IP, port)
2. Rules are loaded from `rules.json`
3. Rules are checked top → bottom
4. First matching rule is applied (ALLOW / DENY)
5. If no rule matches → DENY

