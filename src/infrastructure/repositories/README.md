# 🏆 Repository Pattern - Trừu tượng hóa Dữ liệu / Data Access Abstraction

**Mục đích / Purpose**: Repository đóng vai trò như một bộ sưu tập (collection) các đối tượng trong bộ nhớ, che giấu sự phức tạp của SQL và logic truy vấn. / The Repository pattern acts as an in-memory collection of objects, hiding SQL complexity and query logic.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Đọc/Ghi dữ liệu (CRUD)**: Thực hiện các thao tác Thêm, Đọc, Cập nhật, Xóa vào nguồn dữ liệu.
2. **Trừu tượng hóa nguồn dữ liệu**: Che giấu việc dữ liệu đến từ đâu (SQL, NoSQL, API).
3. **Chuyển đổi kiểu dữ liệu (Mapping)**: Biến đổi bản ghi DB thô thành Domain Entities.
4. **Đóng gói câu truy vấn phức tạp**: Đặt tên có nghĩa cho các logic JOIN/Filter phức tạp.
5. **Quản lý bộ lọc và phân trang**: Xử lý sắp xếp, tìm kiếm và chia nhỏ dữ liệu.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Trong SQL, chúng ta thường làm việc với các bảng phẳng. Trong code, chúng ta làm việc với các Object phân cấp. Repository là "người phiên dịch" giữa hai thế giới này.
- **Why Repository Pattern?**: Giúp Unit Test dễ dàng hơn bằng cách giả lập (Mock) dữ liệu mà không cần chạy database thật. Đồng thời giữ cho Service layer không bị ngập trong mã SQL.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Chỉ Persistence**: Không được kiểm tra logic nghiệp vụ (Vd: không check stock tại đây).
- **Tuân thủ Interface**: Phải thực thi chính xác các phương thức đã định nghĩa tại Domain Interfaces.
- **Nguyên tử (Atomic)**: Một phương thức Repository nên trả về một đối tượng hoàn chỉnh, sẵn sàng sử dụng.

### 🏛️ Ví dụ thực tế (Examples)
- **OrderRepository**: [Implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) sử dụng SQLAlchemy AsyncSession.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **CRUD Operations**: Executes Create, Read, Update, and Delete actions against data sources.
2. **Data Abstraction**: Hides the underlying data source (SQL, NoSQL, or external API).
3. **Data Mapping**: Transforms raw database records into rich business Domain Entities.
4. **Query Encapsulation**: Assigns meaningful names to complex JOIN/Filter logic.
5. **Filtering & Pagination**: Manages technical sorting, searching, and batching logic.

### 💡 Context & Why
- **Context**: In SQL, we work with flat tables; in code, we work with hierarchical objects. The Repository acts as the "translator" between these two worlds.
- **Why Repository Pattern?**: Simplifies Unit Testing by enabling easy Mocking. It also prevents the Service layer from being cluttered with low-level SQL code.

### ⚠️ Process & Constraints (CCE Template)
- **Persistence Only**: No business logic decision-making allowed (e.g., skip stock checks here).
- **Interface Loyalty**: Must strictly implement methods predefined in the Domain layer.
- **Atomic Results**: Every retrieval method should return a complete, usable domain object.

### 🏛️ Practical Examples
- **OrderRepository**: [Implementation](file:///home/korosaki-ryukai/Workspace/Service/base_service/src/infrastructure/repositories/order_repository.py) leveraging SQLAlchemy AsyncSession.
