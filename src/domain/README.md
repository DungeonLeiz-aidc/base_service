# 📦 Domain Layer - Trái tim của Hệ thống / The Business Core

**Mục đích / Purpose**: Tầng Domain chứa đựng các quy tắc nghiệp vụ bất biến (invariants) và logic cốt lõi. Đây là phần quý giá nhất của codebase, hoàn toàn tách biệt khỏi các yếu tố kỹ thuật. / The Domain layer encapsulates invariant business rules and core logic. It is the most valuable part of the project, strictly isolated from technical concerns.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tại sao cần Domain riêng? Để khi bạn đổi từ SQL sang NoSQL, hay từ REST sang GraphQL, trái tim của doanh nghiệp (cách đặt hàng, cách tính giá) vẫn không hề thay đổi.
- **Why Repository Interface?**: Chúng ta để Interface ở Domain để Domain có thể "yêu cầu" dữ liệu mà không cần biết dữ liệu đó đến từ Postgres hay một API bên thứ ba.

### ⚠️ Ràng buộc (Constraints)
1. **Zero External Dependencies**: Tuyệt đối không import từ `infrastructure`, `application` hay bất kỳ thư viện IO nào (SQLAlchemy, FastAPI).
2. **Persistence Ignorant**: Entities không nên biết chúng được lưu trữ như thế nào.

### 🏛️ Ví dụ thực tế (Examples)
- **Entities**: [Order](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/entities/order.py) quản lý trạng thái và tính toán tổng tiền.
- **Interfaces**: [IOrderRepository](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/interfaces/repositories.py) định nghĩa các bản hợp đồng lưu trữ.

---

## 🇺🇸 English Version

### 📄 Context & Rationale
- **Context**: Why isolate the Domain? So that when you switch from SQL to NoSQL, or REST to GraphQL, the business heart (how to order, how to price) remains untouched.
- **Why Repository Interface?**: We place the Interface in the Domain so the Domain can "request" data without needing to know if it comes from Postgres or an external API.

### ⚠️ Constraints
1. **Zero External Dependencies**: Strictly no imports from `infrastructure`, `application`, or any IO libraries (SQLAlchemy, FastAPI).
2. **Persistence Ignorant**: Entities should not be aware of how they are stored.

### 🏛️ Practical Examples
- **Entities**: [Order](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/entities/order.py) handles state transitions and totals.
- **Interfaces**: [IOrderRepository](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/domain/interfaces/repositories.py) defines persistence contracts.
