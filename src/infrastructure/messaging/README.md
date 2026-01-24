# 📣 Messaging - Giao tiếp Bất đồng bộ / Resilient Messaging Hub

**Mục đích / Purpose**: Messaging là cơ chế cho phép các dịch vụ "nói chuyện" với nhau mà không cần chờ đợi. Nó giúp hệ thống ổn định hơn (Resilient) ngay cả khi một vài thành phần gặp sự cố. / Messaging allows services to communicate asynchronously, enhancing system resilience even when certain components are temporarily unavailable.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao không gọi trực tiếp API gửi Mail? Vì nếu Mail Server chậm, API đặt hàng cũng sẽ chậm theo. Messaging giúp API đặt hàng trả kết quả ngay lập tức, còn việc gửi Mail sẽ được xử lý sau dướI nền.
- **Why RabbitMQ?**: RabbitMQ cung cấp cơ chế hàng đợi (Queue) tin cậy, đảm bảo tin nhắn không bị mất ngay cả khi hệ thống bị khởi động lại.

### ⚠️ Ràng buộc (Constraints)
1. **Idempotency**: Các Worker nhận tin nhắn phải có khả năng xử lý lặp lại (nếu tin nhắn bị gửi 2 lần) mà không gây sai lệch dữ liệu.
2. **Error Handling**: Phải có cơ chế Retry hoặc Dead Letter Exchange (DLX) cho các tin nhắn bị lỗi.

### 🏛️ Ví dụ thực tế (Examples)
- **EventPublisher**: [RabbitMQ implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) đẩy sự kiện sang các hệ thống khác xử lý.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why not call the Mail API directly? If the Mail Server is slow, the Order API becomes slow too. Messaging allows the Order API to respond immediately, delegating mail delivery to background workers.
- **Why RabbitMQ?**: RabbitMQ provides reliable queuing, ensuring messages are preserved even during system restarts.

### ⚠️ Constraints
1. **Idempotency**: Message consumers must handle duplicate messages gracefully without corrupting data.
2. **Error Handling**: Must implement retry mechanisms or Dead Letter Exchanges (DLX) for failed messages.

### 🏛️ Practical Examples
- **EventPublisher**: [RabbitMQ implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) broadcasts events to downstream consumers.
