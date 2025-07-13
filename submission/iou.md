# 🚀 Onchain LifeHackathon Project Demo Submission

<!--
Please fill out the information below. This information will be automatically processed.
Do not remove the --- markers or change the field names.
-->

---
## 📋 Project Information (required)

```yaml
project_name: "IOU DApp - 链上借条存证" # Your project name
description: "一个基于区块链的数字借条应用，支持创建、还款、转让和销毁借条功能，实现去中心化的借贷记录管理" # Brief description of your project
```

## 👥 Team Information (required)

```yaml
team_members: ["Keylen"] # List of team members' usernames, e.g. ["alice", "bob"]
```

## 🔍 Additional Information (optional)

```yaml
presentation_link: "" # Link to your presentation slides or video
notes: "项目实现了完整的借条生命周期管理，包括利息计算，销毁，转让等功能" # Any additional information about your project
```
---

<!-- Do not edit below this line. This section will be automatically generated when your demo submission is processed. -->

## 📖 Project Overview

IOU App 是一个基于区块链的数字借条应用，将传统的借条数字化并上链存储。用户可以创建、管理、转让和销毁借条，所有操作都通过智能合约执行，确保透明度和不可篡改性。

应用支持多种代币类型（ETH及ERC20代币），具有实时利息计算、权限控制、余额监控等功能，为用户提供安全可靠的去中心化借贷服务。

## ✨ Features

- **借条创建**：支持ETH和ERC20代币的借条创建，可设置自定义利率和还款期限
- **智能还款**：全额还款功能，支持实时利息计算和授权溢价防止交易失败
- **借条转让**：债权人可以将借条转让给其他用户，实现债权流通
- **借条销毁**：当前债权人可以销毁借条，支持确认对话框防止误操作
- **余额监控**：实时监控用户、测试地址、部署地址的代币余额
- **权限控制**：严格的权限管理，确保只有相关用户可以执行对应操作
- **用户友好界面**：现代化的UI设计，响应式布局，支持中文本地化

## 🛠️ Technologies Used

- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **Web3**: Wagmi, Viem, RainbowKit
- **UI Components**: HeroUI, Sonner (Toast通知)
- **Smart Contract**: Solidity, ERC721 (NFT标准)
- **State Management**: Zustand
- **Styling**: SCSS, PostCSS

## 🚀 Installation

```bash
# 克隆项目
git clone https://github.com/BiscuitCoder/iou-dapp

# 进入项目目录
cd iou_app/interface

# 安装依赖
pnpm install

# 配置环境变量
cp .env.example .env.local
# 编辑 .env.local 文件，添加必要的配置

```

## 🏃‍♂️ Running the Project

```bash
# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 启动生产服务器
npm start

# 类型检查
npm run type-check
```

## 📷 Screenshots

<!-- Add screenshots of your project here -->

## 🔮 Future Plans

- **移动端优化**：开发移动端App版本
- **多链支持**：支持更多区块链网络
- **信用评分**：基于还款记录的信用评分系统
- **借条模板**：提供多种借条模板选择
- **批量操作**：支持批量创建和管理借条
- **通知系统**：到期提醒和还款通知功能

## 📝 License

MIT License
