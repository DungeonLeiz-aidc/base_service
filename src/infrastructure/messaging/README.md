# 📣 Messaging - Giao tiếp Bất đồng bộ / Asynchronous Communication

**Mục đích / Purpose**: Messaging là cơ chế cho phép các dịch vụ nói chuyện với nhau mà không cần chờ đợi phản hồi ngay lập tức. Điều này giúp hệ thống phản hồi người dùng nhanh hơn và hoạt động ổn định hơn dù có một vài thành phần bị lỗi. / Messaging enables services to communicate without waiting for immediate responses. This leads to faster user responses and increased system resilience, even if some components go offline.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Producer / Consumer**: Một bên gửi tin nhắn (Producer) và một bên nhận tin nhắn (Consumer). Chúng không cần biết nhau ở đâu, chỉ cần qua một "Hộp thư" (Queue).
- **Fire and Forget**: Khi đơn hàng được đặt, API gửi một tin nhắn "Đã đặt hàng" vào Queue rồi trả kết quả cho khách luôn. Việc gửi mail hay sinh hóa đơn sẽ do các Worker xử lý sau đó.
- **Reliability**: Nếu server gửi mail đang bận, tin nhắn vẫn nằm an toàn trong Queue cho đến khi server đó sẵn sàng xử lý.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `rabbitmq_publisher.py`: Đóng vai trò là Producer, đẩy các sự kiện `OrderPlaced` lên RabbitMQ để các dịch vụ khác (như Email, Kho) có thể tiêu thụ.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Producer / Consumer**: One side sends messages (Producer) and the other receives them (Consumer). They don't need to know each other's location; they just use a shared "Mailbox" (Queue).
- **Fire and Forget**: When an order is placed, the API drops an "Order Placed" message into the Queue and immediately responds to the user. Background workers handle email or invoice generation later.
- **Reliability**: If the email server is busy, messages stay safe in the Queue until the server is ready to process them.

### 🏛️ Practical Example
In this project:
- `rabbitmq_publisher.py`: Acts as the Producer, pushing `OrderPlaced` events to RabbitMQ so other services (Email, Warehouse) can consume them.
