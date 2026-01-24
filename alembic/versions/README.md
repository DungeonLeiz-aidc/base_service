# 🕒 Migration Versions - Bản đồ Biến đổi Cấu trúc / Master Schema Evolution

**Mục đích / Purpose**: Danh mục này không chỉ lưu trữ file, nó là "Cuốn nhật ký" ghi lại toàn bộ sự phát triển của hệ thống dữ liệu dưới dạng một Danh sách liên kết (Linked List). / This directory is more than a storage space; it is the "Journal" of the data system's evolution, structured as a Linked List.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🏛️ Lý thuyết Cốt lõi (Core Theory - Linked List)
Mỗi file migration là một mắt xích trong chuỗi:
- **Revision ID**: Định danh duy nhất của mắt xích hiện tại.
- **Down Revision**: ID của mắt xích trước đó. 
- **Tại sao?**: Cấu trúc này đảm bảo database không bao giờ bị nhảy cóc phiên bản, giúp việc đồng bộ giữa các môi trường (Dev/Prod) luôn chính xác tuyệt đối.

### 🔄 Quy trình làm việc Chuyên nghiệp (Professional Workflow)
1. **Sửa Model**: Cập nhật các class tại `src/infrastructure/models/`.
2. **Tạo Revision**: Chạy lệnh autogenerate để Alembic tự so sánh Model với DB thực tế.
3. **Kiểm tra Code**: Luôn mở file vừa tạo để kiểm tra logic `upgrade()` và `downgrade()`.
4. **Áp dụng**: Nâng cấp DB lên phiên bản mới nhất.

### 💻 Lệnh thực thi hỗ trợ (Mastering CLI)
```bash
# Tạo bản migration tự động (Dựa trên thay đổi của Model)
uv run alembic revision --autogenerate -m "thêm_cột_xyz"

# Nâng cấp lên phiên bản mới nhất
uv run alembic upgrade head

# Quay lại phiên bản trước đó 1 bước
uv run alembic downgrade -1

# Kiểm tra trạng thái hiện tại của DB (Biết mình đang ở đâu)
uv run alembic current

# Xem lịch sử các bản migration
uv run alembic history --verbose
```

### ⚠️ Lưu ý: Schema vs Data Migration
- **Schema Migration**: Thay đổi cấu trúc (Thêm bảng, đổi tên cột). Thường dùng `--autogenerate`.
- **Data Migration**: Thay đổi dữ liệu bên trong (Vd: Gộp tên và họ thành FullName). **Không dùng autogenerate**, phải viết code SQL/ORM thủ công trong hàm `upgrade()`.

### 🛡️ Audit & Logging
Để biết migration chạy thành công:
1. **Logs**: Kiểm tra stdout, Alembic sẽ báo `Result: OK` hoặc thông tin lỗi cụ thể.
2. **Table `alembic_version`**: Kiểm tra bảng này trong database để biết chuỗi hash hiện tại có khớp với file mới nhất không.

---

## 🇺🇸 English Version

### 🏛️ Core Theory (Linked List)
Each migration file acts as a node in a chain:
- **Revision ID**: Unique identifier for the current node.
- **Down Revision**: Previous node ID.
- **Rationale**: This structure prevents version skipping, ensuring absolute consistency across environments (Dev/Prod).

### 🔄 Professional Workflow
1. **Modify Models**: Update classes in `src/infrastructure/models/`.
2. **Generate Revision**: Run autogenerate to let Alembic diff Models vs. the actual DB.
3. **Audit Code**: Always inspect the generated file's `upgrade()` and `downgrade()` logic.
4. **Apply**: Upgrade DB to the latest head.

### 💻 Mastering the CLI
```bash
# Autogenerate migration based on Model changes
uv run alembic revision --autogenerate -m "add_column_xyz"

# Upgrade to the latest version
uv run alembic upgrade head

# Revert one step back
uv run alembic downgrade -1

# Check current DB version
uv run alembic current

# View migration history
uv run alembic history --verbose
```

### ⚠️ Schema vs. Data Migration
- **Schema Migration**: Structural changes (adding tables, renaming columns). Typically uses `--autogenerate`.
- **Data Migration**: Content changes (e.g., merging First/Last name into FullName). **Manual effort required**; write SQL/ORM code directly inside `upgrade()`.

### 🛡️ Audit & Logging
Verify success via:
1. **Logs**: Check stdout for `Result: OK` or detailed tracebacks.
2. **`alembic_version` Table**: Inspect this table in the DB to confirm the stored hash matches your latest revision file.
