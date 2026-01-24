# 🚚 Infrastructure Migrations - Tiến hóa Dữ liệu / Application Schema Wiring

**Mục đích / Purpose**: Thư mục này chứa cấu hình và logic để kết nối các Models tại mã nguồn với công cụ Alembic, đảm bảo database tiến hóa cùng với code. / Houses the configuration and logic to wire source Models to Alembic, ensuring database evolution mirrors code changes.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Đồng bộ hóa Metadata**: Kết nối Models với engine của Alembic qua đối tượng Metadata.
2. **Kiểm soát Phiên bản trong Code**: Quản lý sự thay đổi schema ngay trong luồng mã nguồn.
3. **Bảo đảm An toàn Triển khai**: Cấu hình env.py để thực thi migration an toàn.
4. **Ánh xạ Logic Chuyển đổi**: Chứa các script Python thực hiện nâng cấp hoặc khôi phục dữ liệu.
5. **Kiểm tra Tính Nhất quán**: Đảm bảo trạng thái code khớp 100% với trạng thái Database vật lý.

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Mã nguồn (Code) và Cơ sở dữ liệu (DB) là hai thực thể khác nhau nhưng cần được giữ đồng bộ. Thư mục này là "keo dính" giữa chúng.
- **Why env.py?**: Đây là nơi chúng ta cấu hình cách ứng dụng "nói chuyện" với DB trong quá trình migration, bao gồm cả việc xử lý các kết nối Bất đồng bộ (Async).

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Import Models**: Phải đảm bảo mọi file trong thư mục `models/` đều được import vào `env.py` để metadata có thể nhìn thấy chúng.
- **Async Safety**: Vì dự án dùng Async, file `env.py` phải sử dụng engine bất đồng bộ của SQLAlchemy.
- **Metadata Bridge**: Tuyệt đối không được nạp metadata sai lệch so với DB engine đang chạy.

### 🏛️ Ví dụ thực tế (Examples)
- **Bridge**: File [env.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/alembic/env.py) sử dụng `Base.metadata` để sinh các bản revision tại `versions/`.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Metadata Synchronization**: Bridges source Models with the Alembic engine via Metadata objects.
2. **In-Code Version Control**: Governs schema progression within the main source control stream.
3. **Deployment Integrity**: Configures `env.py` for safe structural execution.
4. **Logic Mapping**: Designated home for the Python scripts performing upgrades/downgrades.
5. **Consistency Verification**: Guarantees Python definitions align with physical database state.

### 💡 Context & Why
- **Context**: Code and Databases are separate entities requiring 100% synchronization; this directory acts as their vital "connector".
- **Why env.py?**: Provides absolute control over DB communication during migrations, including support for Asynchronous engines.

### ⚠️ Process & Constraints (CCE Template)
- **Explicit Imports**: Every model file must be imported into `env.py` to ensure visibility to the metadata scanner.
- **Async Awareness**: Migration logic must employ SQLAlchemy's asynchronous engines to match the project's stack.
- **Metadata Integrity**: Never load metadata that conflicts with the intended target database engine.

### 🏛️ Practical Examples
- **The Bridge**: [env.py](file:///home/korosaki-ryukai/Workspace/Service/base_service/alembic/env.py) utilizing `Base.metadata` to drive schema revisions in the `versions/` folder.
