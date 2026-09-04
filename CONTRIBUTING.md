# CONTRIBUTING

## Getting Started

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

## Development Setup

```bash
git clone https://github.com/Lushkah/token-ai-ecosystem.git
cd token-ai-ecosystem

make install
make docker-up
```

## Code Style

We use:
- Black for Python formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

```bash
make format
make lint
```

## Testing

All code must have tests:

```bash
make test
```

## Pull Request Process

1. Ensure tests pass
2. Update documentation
3. Follow code style guidelines
4. Add meaningful commit messages
5. Reference any related issues

## Code Review

All PRs require review before merging. Reviewers will check for:
- Code quality
- Test coverage
- Documentation
- Performance implications

## Bug Reports

Include:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details
- Error logs

## Feature Requests

Include:
- Clear description of feature
- Use cases and benefits
- Proposed implementation
- Potential impact

## Community

- Discord: [Join Community](https://discord.gg/token-ai)
- GitHub Discussions: [Discussions](https://github.com/Lushkah/token-ai-ecosystem/discussions)
- Twitter: [@TokenAIEco](https://twitter.com/tokenaieco)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
