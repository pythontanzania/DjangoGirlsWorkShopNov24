
# 💬 Django Real-Time Chat Application

A real-time chat application built with Django and WebSockets, enabling instant messaging between multiple users in different chat rooms.

## ✨ Features

- Real-time messaging using WebSockets
- Multiple chat rooms
- Clean and responsive UI
- User authentication
- Message history
- Room-based conversations

## 🛠️ Technologies Used

- Django 4.x
- Channels (WebSockets)
- Redis
- HTML/CSS
- JavaScript
- SQLite3

## 📋 Prerequisites

- Python 3.8+
- Redis Server
- Virtual Environment

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/django-chat-app.git
cd django-chat-app
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up Redis**
```bash
# On Ubuntu/Debian
sudo apt-get install redis-server

# On macOS
brew install redis
```

5. **Apply migrations**
```bash
python manage.py migrate
```

6. **Run the development server**
```bash
python manage.py runserver
```

## 📁 Project Structure
```
django-chat-app/
├── chat/                   # Main application directory
├── config/                 # Project configuration
├── static/                 # Static files (CSS, JS)
├── templates/             # HTML templates
└── manage.py              # Django management script
```

## 💻 Usage

1. Navigate to `http://localhost:8000`
2. Create an account or log in
3. Create a new chat room or join an existing one
4. Start chatting in real-time!

## 🔧 Configuration

Key settings can be found in `config/settings.py`:

```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Documentation

For more detailed information, please refer to the [Django Girls Workshop Guide](https://djangogirls.tz/workshop/django-workshop.pdf)

## 👥 Authors

- [Fuad Habib](https://github.com/AvicennaJr)

---
⭐️ Star this repository if you find it helpful!
