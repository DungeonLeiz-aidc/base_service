# 🔄 Application Layer - Tầng Điều Phối / Use Case Orchestration

**Mục đích / Purpose**: Tầng Application hiện thực hóa các kịch bản người dùng (Use Cases) bằng cách điều phối các thành phần Domain và Infrastructure thông qua các Interfaces tại tầng Interface. / The Application layer implements user scenarios (Use Cases) by coordinating Domain and Infrastructure components via protocols defined in the Interface layer.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Thực thi Use Case**: Vận hành luồng xử lý từ lúc bắt đầu đến khi trả về kết quả.
2. **Tiêu thụ Hợp đồng Interface**: Sử dụng các Protocols đã định nghĩa tại tầng Interface.
3. **Cách ly Môi trường**: Giúp nghiệp vụ không phụ thuộc vào việc client là Web, CLI hay Mobile.
4. **Thứ tự Công việc**: Sắp xếp các tác vụ đa bước đảm bảo đúng thứ tự ưu tiên.
5. **Đảm bảo Nguyên tử (Atomicity)**: Quản lý biên giao dịch để dữ liệu luôn nhất quán.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
application/
├── service/            # Logic thực thi Use Case (Nhạc trưởng).
├── dtos/               # Vật chứa dữ liệu truyền tải qua biên tầng.
└── utils/              # Các công cụ hỗ trợ xử lý nghiệp vụ chung.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tầng Application là nơi tập trung các kịch bản sử dụng. Nó không nên sở hữu các định nghĩa kỹ thuật, mà chỉ "tiêu thụ" chúng.
- **Why Orchestration?**: Tách biệt việc "điều phối" (Application) khỏi việc "định nghĩa bản hợp đồng" (Interface).

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Thin Layer**: Không chứa logic tính toán phức tạp (đẩy vào Domain).
- **Consumptive Only**: Chỉ sử dụng các Interfaces, không tự định nghĩa các giao thức hạ tầng.
- **DTO Driven**: Chỉ giao tiếp với Interface layer qua DTOs.

### 🏛️ Ví dụ thực tế (Examples)
- **Service**: [order_service.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Use Case Execution**: Drives the end-to-end lifecycle of business scenarios.
2. **Contract Consumption**: Invokes Protocols defined in the Interface layer.
3. **Environmental Isolation**: Decouples business logic from specific UI (Web/CLI/Mobile).
4. **Workflow Sequencing**: Manages the precise order of multi-step business actions.
5. **Atomicity Management**: Governs transaction boundaries to maintain system integrity.

### 📂 Directory Layout
```text
application/
├── service/            # Use Case orchestration logic (The Conductor).
├── dtos/               # Data containers for inter-layer transfer.
└── utils/              # Generic application-level helper functions.
```

### 💡 Context & Why
- **Context**: The Application layer is the home of use scenarios. It should remain a consumer of technical definitions rather than an owner.
- **Why Orchestration?**: Clearly separates "sequencing" (Application) from "contract definition" (Interface).

### ⚠️ Process & Constraints (CCE Template)
- **Thinness**: Delegate deep business rules to the Domain layer; keep this layer for flow control.
- **Purely Consumptive**: Utilize existing Interfaces only; avoid defining internal infrastructure protocols.
- **DTO Centric**: Always communicate with the Interface layer via DTOs to maintain boundaries.

### 🏛️ Practical Examples
- **Service**: [order_service.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py).
