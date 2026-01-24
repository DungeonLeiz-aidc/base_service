# ⚙️ Application Services - Thực thi Use Cases / Use Case Logic

**Mục đích / Purpose**: Danh mục này chứa các Service thực thi logic của các kịch bản người dùng, điều phối Entities và Infrastructure để hoàn thành Use Case. / This directory contains services implementing user scenarios, coordinating Entities and Infrastructure to fulfill Use Cases.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Điều phối Use Case**: Quản lý luồng công việc đa bước (Vd: Check -> Save -> Notify).
2. **Quản lý Biên Giao dịch**: Đảm bảo tất cả hành động trong một Use Case đều thành công hoặc thất bại cùng nhau.
3. **Phân phối Tác vụ phụ**: Kích hoạt việc gửi Email hoặc Publish sự kiện sau khi logic chính hoàn tất.
4. **Dịch lỗi (Error Translation)**: Biến lỗi kỹ thuật (DB sập) thành lỗi nghiệp vụ thân thiện.
5. **Kiểm soát Quyền**: Kiểm tra xem người dùng có được phép thực hiện hành động này hay không.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Code nghiệp vụ (Entity) không nên biết về Database, còn API Controller thì quá bận rộn với HTTP. Chúng ta cần một "vùng đệm" ở giữa để xử lý luồng (Flow).
- **Why Application Service?**: Giúp tái sử dụng logic nghiệp vụ. Một Service `OrderService` có thể phục vụ cho cả Web API, Mobile App và CLI mà không cần viết lại.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Không quy tắc nghiệp vụ**: Vd: Việc tính thuế phải nằm ở Domain, Service chỉ là người gọi hàm tính thuế đó.
- **Transactional**: Phải luôn được bao bọc trong một khối Transaction (thanh qua Unit of Work).
- **Trừu tượng**: Chỉ làm việc với các Repository Interfaces, không làm việc trực tiếp với SQLAlchemy sessions.

### 🏛️ Ví dụ thực tế (Examples)
- **Order Service**: [order_service.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py) phối hợp Inventory và Repositories.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Workflow Orchestration**: Manages multi-step sequences (e.g., Check -> Save -> Notify).
2. **Transaction Integrity**: Ensures either all steps succeed or none are committed.
3. **Side-effect Dispatching**: Triggers secondary tasks like Emails or Events post-execution.
4. **Exception Handling**: Translates technical failures into business-appropriate exceptions.
5. **Authorization Enforcement**: Validates caller permissions for specific actions.

### 💡 Context & Why
- **Context**: Business logic (Entities) should stay DB-agnostic, while API Controllers are tied to HTTP details. We need a "buffer zone" to manage the execution flow.
- **Why Application Services?**: Promotes reuse. An `OrderService` can support Web, Mobile, and CLI consumers without redundant logic.

### ⚠️ Process & Constraints (CCE Template)
- **Logic-Free**: Delegate core calculations (e.g., tax) to the Domain layer; the service only coordinates calls.
- **Atomic Execution**: Always wrap service methods in a Transaction (via Unit of Work).
- **Clean Persistence**: Interact exclusively with Repository Interfaces, never directly with SQL sessions.

### 🏛️ Practical Examples
- **Order Service**: [order_service.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/application/service/order_service.py) coordinating Inventory and DB Repositories.
