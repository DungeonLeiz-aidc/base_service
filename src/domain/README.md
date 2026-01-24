# 📦 Domain Layer - Linh hồn của Doanh nghiệp / Core Business Logic

**Mục đích / Purpose**: Tầng Domain là nơi định nghĩa "Luật chơi". Nó chứa các khái niệm cốt lõi, quy tắc và logic nghiệp vụ mà không quan tâm đến việc dữ liệu được lưu ở đâu hay API trông như thế nào. / The Domain layer defines the "Rules of the Game". It contains core concepts, business rules, and logic, independent of data storage or API structures.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 📄 Khái niệm Cốt lõi
- **Entities**: Những đối tượng có định danh (ID) duy nhất và vòng đời dài (ví dụ: `Order` #123). Ngay cả khi thuộc tính thay đổi, nó vẫn là chính nó.
- **Value Objects**: Những đối tượng được định nghĩa bằng các giá trị thuộc tính (ví dụ: `Price`, `Address`). Nếu hai Address có cùng số nhà, chúng được coi là bằng nhau.
- **Domain Service**: Các logic nghiệp vụ không thuộc về một Entity cụ thể nào mà phối hợp nhiều Entities.
- **Exceptions**: Các lỗi nghiệp vụ thuần túy (như `Sản phẩm đã hết hàng`).

### 🏛️ Ví dụ thực tế (Example)
Trong hệ thống OMS này:
- `Order` là một Entity quan trọng quản lý trạng thái đơn hàng.
- `src/domain/exceptions.py` định nghĩa các lỗi mà hệ thống sẽ gặp phải khi logic nghiệp vụ bị vi phạm.

---

## 🇺🇸 English Version

### 📄 Core Concepts
- **Entities**: Objects with a unique identity (ID) and a long lifecycle (e.g., `Order` #123). They remain the same object even if attributes change.
- **Value Objects**: Objects defined by their attribute values (e.g., `Price`, `Address`). Two Address objects with identical values are considered equal.
- **Domain Service**: Business logic that doesn't naturally belong to a specific Entity but coordinates multiple Entities.
- **Exceptions**: Pure business errors (e.g., `Product Out of Stock`).

### 🏛️ Practical Example
In this OMS system:
- `Order` is a key Entity managing order states.
- `src/domain/exceptions.py` defines errors triggered when business invariants are violated.
