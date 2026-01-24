# 📣 Domain Events - Tiếng nói của Nghiệp vụ / The Voice of the Domain

**Mục đích / Purpose**: Domain Events là cách hệ thống ghi lại và thông báo về một điều gì đó quan trọng vừa xảy ra trong nghiệp vụ. Nó giúp các phần khác nhau của hệ thống giao tiếp với nhau mà không cần biết quá nhiều về nhau (Decoupling). / Domain Events are how the system records and announces significant business occurrences. They allow different parts of the system to communicate without tight coupling.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Sức mạnh bất biến**: Sự kiện là những gì "đã xảy ra" trong quá khứ (Past Tense). Một khi đã xảy ra, nó không bao giờ thay đổi.
- **Tính lây lan (Propagation)**: Khi một sự kiện như `OrderPlaced` nổ ra, nó có thể kích hoạt một chuỗi các hành động khác như: Gửi email xác nhận, Trừ tồn kho, Sinh hóa đơn.
- **Event-Driven Architecture**: Giúp hệ thống mở rộng dễ dàng. Bạn có thể thêm một dịch vụ "Khuyến mãi" mới lắng nghe sự kiện `OrderPlaced` mà không cần sửa code của tầng `Order`.

### 🏛️ Ví dụ thực tế (Example)
Trong dự án này:
- `order_events.py`: Định nghĩa các class như `OrderPlaced` chứa thông tin về `order_id` và danh sách sản phẩm. Đây là gói thông tin được gửi đi khắp hệ thống.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Immutability**: Events represent something that has "already happened" (Past Tense). Once they occur, they never change.
- **Propagation**: When an event like `OrderPlaced` is fired, it can trigger a chain of subsequent actions: sending confirmation emails, deducting inventory, or generating invoices.
- **Event-Driven Architecture**: Enhances scalability. You can add a new "Promotion" service that listens for the `OrderPlaced` event without modifying the `Order` layer's code.

### 🏛️ Practical Example
In this project:
- `order_events.py`: Defines classes like `OrderPlaced` containing `order_id` and item lists. This is the data package distributed throughout the system.
