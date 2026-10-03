# Changelog

本项目遵循[语义化版本](https://semver.org/lang/zh-CN/)，版本按时间倒序排列。

## [未发布]

### 变更

- `pyproject.toml` 的 `description` 改为据实描述（占位包用途），不再使用占位文案（farfarfun/todo-list#693）。
- 开发依赖补充 `ruff`、`funbuild`，并新增 `[tool.ruff]` 配置，构建/发布统一走组织标准的 `funbuild release`（`uv run funbuild release` 封装了版本递增、构建、安装校验、发布、打标签全流程），不手写发布脚本（farfarfun/todo-list#693）。

## [0.0.2] - 2026-08-31

### 变更

- 补全 `[build-system]` 配置（hatchling），通过 `funbuild release` 发布到 PyPI 以保留 `funllmchat` 包名。

### 新增

- 占位版本的 `funllmchat` 包，尚无实际功能代码，具体功能待后续补充。

### 修复

- 无。

### 废弃

- 无。
