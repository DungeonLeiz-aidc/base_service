# 📣 Messaging - Giao tiếp Bất đồng bộ / Resilient Messaging Hub

**Mục đích / Purpose**: Messaging là cơ chế cho phép các dịch vụ "nói chuyện" với nhau mà không cần chờ đợi. Nó giúp hệ thống ổn định hơn (Resilient) ngay cả khi một vài thành phần gặp sự cố. / Messaging allows services to communicate asynchronously, enhancing system resilience even when certain components are temporarily unavailable.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao không gọi trực tiếp API gửi Mail? Vì nếu Mail Server chậm, API đặt hàng cũng sẽ chậm theo. Messaging giúp API đặt hàng trả kết quả ngay lập tức, còn việc gửi Mail sẽ được xử lý sau dưới nền.
- **Why RabbitMQ?**: RabbitMQ cung cấp cơ chế hàng đợi (Queue) tin cậy, đảm bảo tin nhắn không bị mất ngay cả khi hệ thống bị khởi động lại.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Constraints**: 
    1. **Idempotency**: Worker phải có khả năng xử lý một tin nhắn nhiều lần mà không gây lỗi (Vd: không gửi 2 email cho 1 đơn hàng).
    2. **Circuit Breaker Aware**: Nếu Queue bị đầy, hệ thống cần có cơ chế ngắt hoặc lưu tạm tại Local.
- **Workflow**:
    1. **Publish**: Tầng Application bắn sự kiện `OrderPlaced` vào `Exchange`.
    2. **Routing**: RabbitMQ định tuyến tin nhắn vào các `Queues` (EmailQueue, ShippingQueue).
    3. **Consume**: Worker lấy tin nhắn ra và thực thi hành động thực tế.

### 🏛️ Ví dụ thực tế (Examples)
- **EventPublisher**: [RabbitMQ implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) đẩy sự kiện sang các hệ thống khác xử lý.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why not call a Mail API directly? If the Mail Server lags, the Order API lags. Messaging allows the Order API to respond instantly, letting background workers handle non-critical tasks.
- **Why RabbitMQ?**: RabbitMQ provides durable queuing, ensuring messages survive system reboots or transient crashes.

### ⚠️ Workflow & Constraints
- **Constraints**: 
    1. **Idempotency**: Consumers must handle duplicate messages without side effects (e.g., avoiding double-billing or duplicate emails).
    2. **Circuit Breaker Aware**: Handle full queues or publisher failures gracefully.
- **Workflow**:
    1. **Publish**: Application layer emits `OrderPlaced` to an `Exchange`.
    2. **Routing**: RabbitMQ routes the message to specific `Queues` (EmailQueue, ShippingQueue).
    3. **Consume**: Workers pull from the queue and execute the business logic.

### 🏛️ Practical Examples
- **EventPublisher**: [RabbitMQ implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) broadcasts events to the ecosystem.
