# 🗃️ External Clients - Cổng kết nối Ngoại vi / Service Adapters

**Mục đích / Purpose**: Thư mục này chứa các "Adapter" để kết nối hệ thống với các dịch vụ bên thứ ba (Redis, RabbitMQ, Payment Gateways). Mỗi client giúp chuyển đổi giao thức của bên ngoài thành ngôn ngữ mà ứng dụng của chúng ta hiểu được. / This directory contains "Adapters" that connect the system to third-party services (Redis, RabbitMQ, Payment Gateways). Each client translates external protocols into the language our application understands.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Adapter Pattern**: Thay vì dùng trực tiếp thư viện `redis-py` hay `aio-pika` trong Use Case, chúng ta bao bọc chúng lại. Điều này giúp ta dễ dàng thay đổi thư viện hoặc mock dữ liệu khi test.
- **Sự độc lập**: Tầng Application chỉ cần gọi `event_publisher.publish()` mà không quan tâm nó dùng RabbitMQ, Kafka hay AWS SQS.

### 🏛️ Ví dụ thực tế (Example)
- `redis_client.py`: Quản lý kết nối và thực hiện các thao tác Distributed Locking cho kho hàng.
- `rabbitmq_client.py`: Đảm nhận việc gửi tin nhắn ra các queue bất đồng bộ.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Adapter Pattern**: Instead of using libraries like `redis-py` or `aio-pika` directly in Use Cases, we wrap them. This makes it easy to switch libraries or mock data during testing.
- **Independence**: The Application layer simply calls `event_publisher.publish()` without caring whether it uses RabbitMQ, Kafka, or AWS SQS.

### 🏛️ Practical Example
- `redis_client.py`: Manages connections and performs Distributed Locking operations for inventory.
- `rabbitmq_client.py`: Handles sending messages to asynchronous queues.
