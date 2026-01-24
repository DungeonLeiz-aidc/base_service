# 📣 Messaging - Giao tiếp Bất đồng bộ / Resilient Messaging Hub

**Mục đích / Purpose**: Messaging cho phép các dịch vụ giao tiếp bất đồng bộ, giúp hệ thống phản hồi nhanh hơn và tăng khả năng chịu lỗi. / Messaging enables asynchronous communication, improving responsiveness and system fault tolerance.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Giao tiếp Bất đồng bộ**: API trả kết quả ngay, các tác vụ nặng sẽ được xử lý ngầm.
2. **Đảm bảo Độ tin cậy**: Ngăn chặn mất mát tin nhắn khi hệ thống gặp sự cố.
3. **Nới lỏng Phụ thuộc**: Dịch vụ chỉ cần quan tâm đến Sự kiện (Event), không cần biết ai xử lý chúng.
4. **Xử lý Lỗi & Thử lại**: Tự động thử lại khi consumer lỗi và quản lý hàng đợi lỗi (DLQ).
5. **Phân phối Sự kiện (Broadcasting)**: Một sự kiện có thể kích hoạt nhiều hành động ở các module khác nhau.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong Microservices, một hành động (Vd: "Đặt hàng") có thể kéo theo chuỗi hệ quả (Gửi email, Tạo hóa đơn, Trừ kho). Nếu làm đồng bộ (Synchronous), người dùng sẽ phải chờ rất lâu.
- **Why RabbitMQ?**: RabbitMQ cung cấp độ tin cậy cực cao với các cơ chế Xác nhận (Acknowledge) và Persistence, đảm bảo nghiệp vụ không bao giờ bị bỏ lỡ.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Idempotency**: Mọi Consumer phải có khả năng xử lý cùng một tin nhắn nhiều lần mà không gây ra lỗi dữ liệu.
- **Fire-and-forget**: Producer không nên chờ đợi kết quả xử lý từ Consumer.
- **Payload tối giản**: Chỉ gửi các ID và thông tin thay đổi trọng yếu, không gửi toàn bộ object khổng lồ qua message.

### 🏛️ Ví dụ thực tế (Examples)
- **Publisher**: [rabbitmq_publisher.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) thực hiện việc gửi `OrderPlaced` event.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Asynchronous Communication**: Enables instant API responses while offloading heavy tasks.
2. **Message Durability**: Prevents message loss during system or consumer failures.
3. **Service Decoupling**: Services interact via Events without direct technical coupling.
4. **Retry & DLQ Management**: Automates recovery flows and handles unprocessable messages.
5. **Event Broadcasting**: Enables a single event to trigger multiple downstream workflows.

### 💡 Context & Why
- **Context**: In microservices, one action (e.g., "Place Order") triggers a cascade of effects. Synchronous processing would cause unacceptable user latency.
- **Why RabbitMQ?**: Provides superior reliability via Acknowledgement and Persistence mechanisms, ensuring vital business events are never lost.

### ⚠️ Process & Constraints (CCE Template)
- **Idempotency**: Consumers must handle duplicate messages without side-effect corruption.
- **Fire-and-forget**: Producers should not expect immediate feedback from consumers.
- **Minimal Payload**: Send only core IDs and state changes; avoid transmitting bloated objects.

### 🏛️ Practical Examples
- **Publisher**: [rabbitmq_publisher.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/messaging/rabbitmq_publisher.py) dispatching the `OrderPlaced` event.
