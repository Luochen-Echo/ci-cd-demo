# GitHub CI/CD 最简入门指南（Python）

## 前置准备
- GitHub账号
- Git已安装
- Python 3.x已安装

---

## 步骤1：创建GitHub仓库

1. 登录GitHub，点击右上角 `+` → `New repository`
2. 仓库名：`ci-cd-demo`
3. 选择 `Public` 或 `Private`
4. 勾选 `Add a README file`
5. 点击 `Create repository`

---

## 步骤2：克隆到本地

```bash
git clone https://github.com/你的用户名/ci-cd-demo.git
cd ci-cd-demo
```

---

## 步骤3：创建简单Python项目

### 创建文件 `app.py`
```python
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(add(2, 3))
    print(greet("World"))
```

### 创建文件 `test_app.py`
```python
import pytest
from app import add, greet

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
```

### 创建文件 `requirements.txt`
```
pytest
```

### 创建文件 `report.md`
```markdown
# CI/CD Demo Report

## 项目信息
- 项目名称：CI/CD Demo
- 语言：Python
- 状态：正常运行中

## 功能
1. 加法运算
2. 问候功能
```

---

## 步骤4：配置CI（持续集成）

### 创建目录和文件
```bash
mkdir -p .github/workflows
```

### 创建文件 `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: pytest test_app.py -v
```

---

## 步骤5：配置CD（持续部署到GitHub Pages）

### 修改 `.github/workflows/ci.yml`，添加部署任务

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: pytest test_app.py -v

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: .
        publish_branch: gh-pages
```

---

## 步骤6：启用GitHub Pages

1. 进入仓库页面
2. 点击 `Settings` → `Pages`
3. Source 选择：`Deploy from a branch`
4. Branch 选择：`gh-pages` → `/ (root)`
5. 点击 `Save`

---

## 步骤7：提交代码

```bash
git add .
git commit -m "Initial commit with CI/CD"
git push origin main
```

---

## 步骤8：查看CI/CD运行

1. 进入仓库页面
2. 点击 `Actions` 标签
3. 你会看到workflow正在运行
4. 测试通过后，会自动部署到GitHub Pages
5. 几分钟后，访问 `https://你的用户名.github.io/ci-cd-demo/`

---

## 工作流程图

```
代码推送到GitHub
    ↓
触发GitHub Actions
    ↓
运行测试 (pytest)
    ↓
测试通过？
    ├─ 否 → 失败，通知开发者
    └─ 是 → 自动部署到GitHub Pages
```

---

## 常见问题

**Q: Actions失败怎么办？**
A: 点击红色叉号查看详细日志，检查语法和依赖

**Q: 如何修改部署内容？**
A: 修改文件后push，CD会自动触发

**Q: GitHub Pages多久更新？**
A: 通常1-5分钟

---

## 下一步学习

- 添加代码检查（flake8、black）
- 添加单元测试覆盖率报告
- 配置环境变量和密钥
- 多环境部署（dev、staging、prod）
