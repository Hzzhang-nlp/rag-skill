# 本地知识库检索 Skill

一个基于 AI Agent 架构的本地知识库检索解决方案，支持 Markdown、PDF、Excel 等多格式文件的智能问答系统。

## 特性

- 多格式支持：Markdown、PDF、Excel、TXT
- 分层索引：通过 data_structure.md 实现智能目录导航
- 渐进式检索：按需局部读取，节省 token 消耗
- 先学习后处理：确保使用正确的工具和方法
- 多轮迭代：最多 5 轮智能检索，逐步缩小范围

## 快速开始

### 环境要求

```bash
# 安装依赖
pip install pandas openpyxl pdfplumber pypdf

# macOS 安装 PDF 工具
brew install poppler

# Linux 安装 PDF 工具
apt install poppler-utils
```

### 使用方式

将本项目作为 Skill 加载到支持 Agent Skill 的 AI 助手中，直接提问：

```
问：2026年AI Agent技术有哪些关键发展趋势？
问：帮我分析库存数据，哪些商品库存不足？
问：XSS攻击的防护措施有哪些？
```

## 项目结构

```
rag-skill/
├── README.md
├── .agent/
│   └── skills/
│       ├── rag-skill/              # 核心检索 Skill
│       │   ├── SKILL.md
│       │   ├── references/         # 参考文档
│       │   │   ├── pdf_reading.md
│       │   │   ├── excel_reading.md
│       │   │   └── excel_analysis.md
│       │   └── scripts/
│       │       └── convert_pdf_to_images.py
│       │
│       └── skill-creator/          # Skill 创建工具
│           ├── SKILL.md
│           └── scripts/
│               ├── init_skill.py
│               ├── package_skill.py
│               └── quick_validate.py
│
└── knowledge/                      # 示例知识库
    ├── AI Knowledge/              # AI 行业报告
    ├── Financial Report Data/      # 金融财报
    ├── E-commerce Data/            # 电商数据
    └── Safety Knowledge/           # 安全知识
```

## 核心设计

### 1. 分层索引导航

通过 `data_structure.md` 建立目录索引树，AI 先理解目录结构，再选择性检索。

### 2. 先学习再处理

处理 PDF/Excel 前必须先阅读参考文档，学习正确的处理方法。

### 3. 渐进式检索

使用 `grep` 定位关键词，多轮迭代逐步缩小范围，只读取匹配行附近的上下文。

## 知识库数据说明

| 目录 | 内容 |
|------|------|
| AI Knowledge | AI 行业报告、白皮书（14个PDF） |
| Financial Report Data | 上市公司财报数据 |
| E-commerce Data | 电商业务数据（4个Excel） |
| Safety Knowledge | 安全知识文档 |

## 自定义知识库

1. 创建目录：`mkdir knowledge/YourDomain/`
2. 创建索引：`touch knowledge/YourDomain/data_structure.md`
3. 编写索引内容说明用途和文件列表
4. 放入知识文件

## 许可证

MIT License