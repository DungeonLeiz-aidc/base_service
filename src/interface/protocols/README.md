# 🏗️ Technical Protocols - Các Bản hợp đồng Kỹ thuật / System Contracts

**Mục đích / Purpose**: Danh mục này định nghĩa các "hợp đồng" kỹ thuật (Protocols/ABCs) dùng chung cho toàn bộ hệ thống, đảm bảo tính nhất quán giữa các tầng và khả năng thay thế linh kiện. / This directory defines shared technical "contracts" (Protocols/ABCs) for the entire system, ensuring cross-layer consistency and component swappability.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Thiết lập Hợp đồng Kỹ thuật**: Định nghĩa các phương thức mà Repositories và Infrastructure Client phải thực thi.
2. **Trung tâm Giao tiếp nội bộ**: Đóng vai trò là "ngôn ngữ chung" kỹ thuật để các tầng Application và Infrastructure hiểu nhau.
3. **Mô phỏng Đảo ngược Phụ thuộc (IoC)**: Giúp các tầng nghiệp vụ bên trong làm chủ quy trình bằng cách ra lệnh cho tầng hạ tầng.
4. **Kích hoạt Khả năng Kiểm thử**: Cho phép tạo các Mocks/Fakes một cách tiêu chuẩn cho toàn bộ Test Suite.
5. **Cách ly Công nghệ**: Đảm bảo ranh giới giữa "Cái gì cần làm" (Interface) và "Làm như thế nào" (Infrastructure) luôn rõ ràng.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong Clean Architecture, mọi giao tiếp xuyên biên giới tầng phải thông qua các Port (Interface). Đặt chúng tại đây giúp tập trung hóa mọi định nghĩa "biên giới".
- **Why Protocols here?**: Việc dồn toàn bộ Interfaces (bao gồm cả Inbound và Outbound) vào tầng `interface` giúp đơn giản hóa việc tìm kiếm và quản lý các "bản hợp đồng" của hệ thống.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Zero Implementation**: Tuyệt đối không chứa bất kỳ logic xử lý thực tế nào. Chỉ có signatures.
- **Port-Oriented**: Mỗi file phải đại diện cho một Port cụ thể (Vd: Persistence Port, Messaging Port).
- **Type Safety**: Phải tuân thủ nghiêm ngặt việc sử dụng Type Hints cho mọi tham số và giá trị trả về.

### 🏛️ Ví dụ thực tế (Examples)
- **Repository Interface**: [repositories.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/repositories.py).
- **Infrastructure Interface**: [infrastructure.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/infrastructure.py).

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Technical Contract Definition**: Establishes the mandatory methods for Repositories and Infrastructure Clients.
2. **Internal Communication Hub**: Serves as the "common technical language" enabling synergy between Application and Infrastructure layers.
3. **Inversion of Control (IoC)**: Empowers internal business layers to dictate requirements to external infrastructure.
4. **Testability Empowerment**: Provides the foundation for standardized Mocking and Faking across the Test Suite.
5. **Technology Decoupling**: Maintains a definitive boundary between "What needs to be done" (Interface) and "How it is done" (Implementation).

### 💡 Context & Why
- **Context**: In Clean Architecture, cross-layer communication must occur via Ports (Interfaces). Centralizing them here provides a unified view of all system boundaries.
- **Why Protocols here?**: Consolidating all Interfaces (Inbound and Outbound) within the `interface` layer simplifies the discovery and management of system contracts.

### ⚠️ Process & Constraints (CCE Template)
- **Zero Implementation**: Strictly prohibited from containing executable logic; signatures only.
- **Port-Oriented**: Each file must represent a specific architectural Port (e.g., Persistence, Messaging).
- **Type Rigidity**: Mandatory use of PEP 484 Type Hints for all parameters and return types.

### 🏛️ Practical Examples
- **Repository Interface**: [repositories.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/repositories.py).
- **Infrastructure Interface**: [infrastructure.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/interface/protocols/infrastructure.py).
