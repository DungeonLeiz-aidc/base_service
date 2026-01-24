# 🎓 Clean Architecture & DDD Knowledge Map (Python)

**Mục đích / Purpose**: Dự án này là một bộ giáo trình thực tế để triển khai Microservices chuyên nghiệp, tuân thủ nguyên tắc Clean Architecture và DDD. / This project is a practical textbook for building professional Microservices using Clean Architecture and DDD principles.

Tiếng Việt | [English](#-english-version)

---

## 🇻🇳 Tiếng Việt

### 🎯 Nhiệm vụ cốt lõi (Core Responsibilities)
1. **Tầm nhìn & Mục tiêu (Project Vision)**: Truyền tải tri thức về cách xây dựng hệ thống bền vững.
2. **Sơ đồ Vận hành (Operational Blueprint)**: Cấu hình sẵn Makefile và Docker để chạy dự án ngay lập tức.
3. **Bản đồ Công nghệ (Tech Stack Overview)**: Minh họa sự phối hợp giữa FastAPI, Redis, Postgres, RabbitMQ.
4. **Tiêu chuẩn Kỹ thuật (Engineering Standards)**: Thiết lập chuẩn code 10/10 cho toàn dự án.
5. **Chuyển giao Tri thức (Handover Guide)**: Giúp nhân sự mới nắm bắt kiến trúc chỉ trong vài phút.

### 📂 Cấu trúc Thư mục (Directory Layout)
```text
.
├── src/                # Mã nguồn chính (Domain, App, Infra, Interface).
├── tests/              # Hệ thống kiểm thử toàn diện (Unit, Integration).
├── alembic/            # Quản lý phiên bản Database (Migrations).
├── configs/            # Cấu hình tập trung (Service, Clients, LLM).
├── logs/               # Nhật ký vận hành và audit bảo mật.
└── scripts/            # Các công cụ hỗ trợ và dữ liệu mẫu (Seed).
```

### 💡 Bối cảnh & Tư duy (Context & Why)
- **Context**: Tech stack luôn thay đổi, nghiệp vụ thì bền vững hơn. Cần tách biệt chúng.
- **Why Clean Architecture?**: Bảo vệ logic kinh doanh khỏi sự lỗi thời của công nghệ ngoại vi.

### ⚠️ Quy trình & Ràng buộc (CCE Template)
- **Dependency Rule**: Tầng trong không phụ thuộc tầng ngoài.
- **Domain Purity**: Cấm mã kỹ thuật (IO/DB) xâm nhập vào Domain.
- **Self-Validation**: Thực thể phải tự bảo vệ tính hợp lệ.

### 🏛️ Ví dụ thực tế (Examples)
- **Vận hành**: `make run` để khởi động stack hoàn chỉnh.

---

## 🇺🇸 English Version

### 🎯 Core Responsibilities
1. **Project Vision**: Philosophy of building scalable enterprise systems.
2. **Operational Blueprint**: Pre-configured environment for instant execution.
3. **Tech Stack Overview**: Synergy between FastAPI, Redis, Postgres, and RabbitMQ.
4. **Engineering Standards**: Establishing 10/10 code quality benchmarks.
5. **Knowledge Handover**: Entry point for rapid architectural onboarding.

### 📂 Directory Layout
```text
.
├── src/                # Core logic (Domain, App, Infra, Interface).
├── tests/              # Multi-layered test suite (Unit, Integration).
├── alembic/            # Schema versioning and migration logs.
├── configs/            # Central settings (Service, Clients, LLM).
├── logs/               # Operational tracking and security audits.
└── scripts/            # Utility tools and initial seed data.
```

### 💡 Context & Why
- **Context**: Tech is volatile; business models are persistent. Hexagonal design keeps the core stable.
- **Why Clean Architecture?**: Decouples high-value rules from low-level implementation details.

### ⚠️ Process & Constraints (CCE Template)
- **Dependency Direction**: Outer layers depend on inner ones, never vice versa.
- **Logic Purity**: Zero framework/IO libraries allowed in the Domain.
- **Integrity**: Domain objects must enforce their own logical invariants.

### 🏛️ Practical Examples
- **Ops**: `make run` to spin up the entire ecosystem.
