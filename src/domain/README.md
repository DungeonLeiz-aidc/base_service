# 📦 Domain Layer - Trái tim của Hệ thống / The Business Core

**Mục đích / Purpose**: Tầng Domain chứa đựng logic nghiệp vụ tinh khiết nhất (Entities, Events), là nơi quan trọng nhất để chuyển giao tri thức nghiệp vụ. / The Domain layer encapsulates pure business logic (Entities, Events) and serves as the definitive center for business knowledge transfer.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Lưu trữ Logic Nghiệp vụ**: Là nơi duy nhất chứa các quy tắc tính toán và xử lý nghiệp vụ cốt lõi.
2. **Định nghĩa Thực thể (Entities)**: Xây dựng các đối tượng có định danh và hành vi nghiệp vụ.
3. **Xây ngữ Ngôn ngữ Chung**: Phản ánh chính xác các thuật ngữ chuyên môn vào trong mã nguồn.
4. **Bảo vệ Tính thuần khiết**: Đảm bảo công nghệ bên ngoài CẤM xâm nhập vào lõi nghiệp vụ.
5. **Duy trì Bất biến**: Đảm bảo các thực thể luôn ở trạng thái đúng đắn ngay từ khi khởi tạo.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
domain/
├── entities/           # Đối tượng định danh và hành vi (Order, Product).
├── events/             # Sự kiện nghiệp vụ (OrderPlaced, OrderPaid).
├── exceptions.py       # Các ngoại lệ đặc thù của nghiệp vụ.
└── __init__.py         # Khởi tạo mô-đun Domain.
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tech stack thay đổi mỗi năm, nhưng quy trình "Đặt hàng -> Thanh toán" có thể tồn tại hàng chục năm.
- **Why Domain Purity?**: Việc tách biệt hoàn toàn khỏi Interfaces giúp Domain trở thành vùng "Bất khả xâm phạm" về kỹ thuật, dễ dàng kiểm thử và bảo trì.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Zero External Dependencies**: Cấm import bất kỳ thư viện nào từ Infrastructure hay Application.
- **Persistence Ignorant**: Domain không được biết về sự tồn tại của Database hay Network.
- **Rich Behavior**: Logic nghiệp vụ phải nằm trong Entities, tránh tạo ra "Dumb Data Classes".

### 🏛️ Ví dụ thực tế (Examples)
- **Hành vi**: Một Entity `Order` tự biết cách tính tổng tiền.
- **Events**: `OrderPlaced` sinh ra ngay khi logic đặt hàng hoàn tất.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Business Logic Hosting**: Exclusive home for core calculations and processing rules.
2. **Entity Definition**: Build objects with unique identity and rich business behavior.
3. **Ubiquitous Language**: Mirrors domain expertise within the source code.
4. **Logic Purity**: Strictly prohibits technical framework penetration into the core.
5. **Invariant Enforcement**: Guarantees entities maintain a valid logical state from creation.

### 📂 Directory Layout
```text
domain/
├── entities/           # Identity and behavior objects (Order, Product).
├── events/             # Business state change notices (OrderPlaced).
├── exceptions.py       # Domain-specific error types.
└── __init__.py         # Domain module initialization.
```

### 💡 Context & Why
- **Context**: Tech stacks evolve annually; "Order -> Payment" workflows survive decades.
- **Why Domain Purity?**: Complete isolation from Interfaces ensures the Domain remains a technical "Sanctuary", easily testable and maintainable.

### ⚠️ Process & Constraints (CCE Template)
- **Zero External Dependencies**: Strictly prohibits imports from infrastructure or application layers.
- **Persistence Ignorance**: Domain objects remain entirely unaware of storage or network details.
- **Rich Behavior**: Logic must reside within Entities, avoiding "Data-only" classes.

### 🏛️ Practical Examples
- **Behavior**: An `Order` entity autonomously calculates its own totals.
- **Events**: `OrderPlaced` emitted immediately upon successful core logic completion.
