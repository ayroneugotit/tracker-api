# Changelog

All notable changes in this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows [Semantic Versioning](https://semver.org/).

## [v0.1.0] - 2025-09-26

### Added

- Initial FastAPI project structure
- Project metadata (`pyproject.toml`)
- Dependencies (`requirements.txt`)
- README with installation instructions

## [v0.2.0] - 2025-09-26

### Added

- Configuration management
- Core architecture modules
- Structured logging system
- MongoDB integration

## [v0.3.0] - 2025-09-28

### Added

- User domain entities
- Password hashing using Argon2
- Authentication endpoints (signup/signin)
- Result pattern for robust error handling
- Custom middleware for exception handling

### Changed

- Restructured codebase following hexagonal architecture
- Transitioned from simple API to a layered domain-driven model
- Enhanced MongoDB integration and data handling