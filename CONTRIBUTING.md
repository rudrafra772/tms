# 🤝 Contributing to TMS

Thank you for your interest in contributing to **TMS (Task Management System)**! We welcome contributions from everyone — whether it’s fixing bugs, adding features, improving documentation, or suggesting ideas.  

Please read this guide carefully before submitting your pull requests (PRs) to ensure a smooth collaboration.

---

## 📝 Repository Rules

1. **Code Review**  
   - All PRs require **review and approval from the repository owner** before merging.  
   - Make sure your code follows the existing project structure and coding style.  

2. **CI/CD and Actions**  
   - All **GitHub Actions / CI/CD pipelines must pass** before a PR can be merged.  
   - This ensures that your changes don’t break the build, tests, or deployment.  

3. **Branching**  
   - Use feature branches for your changes (e.g., `feature/add-login`, `bugfix/fix-task-filter`).  
   - Do not commit directly to `main` or `master`.  

4. **Commit Messages**  
   - Use clear and descriptive commit messages, e.g., `Fix task filtering bug` or `Add task category filter`.  

---

## 🚀 How to Contribute

1. Fork the repository and clone your fork:
   ```bash
     git clone https://github.com/YOUR_USERNAME/tms.git
   ```

2. Create a new feature or bugfix branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes, commit, and push your branch:
   ```bash
   git add .
   git commit -m "Add short description of your changes"
   git push origin feature/your-feature-name
   ```
4. Open a pull request against the `main` branch of the original repository.
5. Wait for code review approval from the repository owner and ensure all CI/CD checks pass.

## 🧹 Code Style and Best Practices

- Follow PEP 8 for Python code.
- Keep functions and modules small and focused.
- Write clear docstrings for any new functions or classes.
- Keep UI templates and static files organized.

## 💡 Reporting Issues

- Please submit any bugs or feature requests as GitHub Issues.
- Provide clear reproduction steps, screenshots if applicable, and your environment details.

## 🙏 Thank You

Your contributions help make TMS better for everyone. We appreciate your time and effort!
