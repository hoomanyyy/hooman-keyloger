# ⌨️ Educational Keylogger — Python

A small Python cybersecurity project built to explore **keyboard event monitoring, client-server communication, and FastAPI** in a controlled laboratory environment.

> ⚠️ **Educational Use Only**
>
> This project is intended only for systems you own or have explicit permission to test.
> Capturing keystrokes from another person's device without authorization can expose sensitive information and may be illegal.

## 🎯 Project Overview

This project demonstrates a simple client-server architecture:

```text
┌──────────────────────┐
│   Test Environment   │
│                      │
│     client.py        │
│  Keyboard Monitor    │
└──────────┬───────────┘
           │
           │ HTTP
           ▼
┌──────────────────────┐
│      server.py       │
│       FastAPI        │
│                      │
│   Receive Test Logs  │
└──────────────────────┘
```

The project was created as a learning exercise to understand how keyboard events can be handled in Python and how a client can communicate with a backend service.

## 📂 Project Structure

```text
hooman-keyloger/
│
├── client.py       # Keyboard-event monitoring client
├── server.py       # FastAPI backend
├── log.txt         # Example/local log output
└── README.md
```

## 🛠️ Technologies

* 🐍 Python
* ⌨️ `pynput`
* 🌐 Requests
* ⚡ FastAPI
* 🚀 Uvicorn
* 🔗 HTTP client-server communication

## 📚 What This Project Demonstrates

This project was created to practice:

* Python event handling
* Keyboard input monitoring
* HTTP requests
* REST-style backend communication
* FastAPI
* Client-server architecture
* Basic cybersecurity concepts
* Working with Python libraries

## 🔐 Security & Ethics

Keylogging software can potentially capture sensitive information such as:

* Passwords
* Private messages
* Personal information
* Authentication codes

For that reason, this project should **never** be deployed on another person's computer or used to collect information without explicit authorization.

Use it only in:

* Your own computer
* A virtual machine
* A dedicated cybersecurity lab
* Authorized security-testing environments

## ⚙️ Requirements

Install the Python dependencies:

```bash
pip install pynput requests fastapi uvicorn
```

> The exact dependencies may vary depending on the operating system and Python version.

## 🧪 Recommended Lab Environment

For safe experimentation, use an isolated environment such as:

```text
Your Computer
     │
     └── Virtual Machine
             │
             ├── Python Client
             │
             └── Local FastAPI Server
```

This keeps the experiment separated from personal data and other systems.

## 🚧 Project Status

**Educational / Experimental**

This is a small learning project rather than a production security tool.

Future improvements could include:

* Better error handling
* Structured logging
* Authentication between client and server
* Secure transport
* Improved project documentation
* Automated tests

## 🎓 Learning Outcome

Building this project helped me understand the relationship between:

```text
Python
  │
  ├── Event Handling
  │
  ├── Networking
  │
  ├── HTTP Requests
  │
  └── Backend APIs
          │
          ▼
       FastAPI
```

It also provided practical experience with designing a simple client-server system.

## 👨‍💻 Author

**Hooman Khodadadi**

GitHub: [@hoomanyyy](https://github.com/hoomanyyy)

---

⚠️ **Use responsibly. Only test on systems you own or have explicit authorization to test.**
