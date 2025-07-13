# 🚀 Onchain LifeHackathon Project Demo Submission

<!--
Please fill out the information below. This information will be automatically processed.
Do not remove the --- markers or change the field names.
-->

---

## 📋 Project Information (required)

```yaml
project_name: 'UniSplit' # Your project name
description: 'A decentralized bill splitting application that allows groups to split expenses using cryptocurrency payments on Base network' # Brief description of your project
```

## 👥 Team Information (required)

```yaml
team_members: ['BruceXu'] # List of team members' usernames, e.g. ["alice", "bob"]
```

## 🔍 Additional Information (optional)

```yaml
presentation_link: 'https://uni-split.vercel.app/' # Link to your presentation slides or video
notes: 'Built with React, TypeScript, Solidity, and deployed on Base network. Features real-time currency conversion, QR code sharing, and comprehensive smart contract testing.' # Any additional information about your project
```

---

<!-- Do not edit below this line. This section will be automatically generated when your demo submission is processed. -->

## 📖 Project Overview

UniSplit is a 100% on-chain, backend-less cryptocurrency bill splitting application that revolutionizes how groups handle shared expenses. Built on the Base network, it provides a seamless way to create shared bills, generate shareable QR codes, and enable guests to pay their shares using USDT with minimal gas fees.

The application addresses the common problem of clumsy bill-splitting in group dining scenarios by leveraging blockchain technology to provide transparency, real-time tracking, and automated settlement. Users can create bills in minutes, share them via QR codes or links, and track payments in real-time without any centralized backend infrastructure.

## ✨ Features

- 💰 **Smart Bill Creation** - Set total amount, number of shares, and currency with real-time conversion
- 🔗 **QR Code & Link Sharing** - Generate shareable QR codes and URLs for easy distribution
- 💳 **Multi-Token Support** - Pay with USDC, USDT, and other ERC20 tokens on Base network
- 📱 **Mobile Responsive Design** - Professional UI that works seamlessly on all devices
- 🔐 **Web3 Wallet Integration** - Connect with MetaMask, WalletConnect, and other popular wallets
- ⚡ **Real-time Currency Conversion** - Live exchange rates for accurate share calculations
- 🛡️ **Smart Contract Security** - Audited smart contract with comprehensive test coverage (43 passing tests)
- 👥 **Flexible Payment Options** - Support for proxy payments (paying for multiple shares)
- 🎯 **Creator Share Management** - Bill creators can set their initial paid shares
- 📊 **Live Payment Tracking** - Real-time updates on payment status and remaining shares

## 🛠️ Technologies Used

- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS
- **Web3 Stack**: wagmi, viem, RainbowKit
- **Blockchain**: Base Network (Ethereum L2)
- **Smart Contracts**: Solidity, Hardhat, OpenZeppelin
- **UI Components**: Radix UI, shadcn/ui, Lucide React
- **Testing**: Hardhat Test Suite (43 comprehensive tests)
- **Styling**: Tailwind CSS with custom animations
- **State Management**: React Query, React Hook Form
- **Utilities**: QR Code generation, Zod validation

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/brucexu-eth/UniSplit

# Navigate to the project directory
cd UniSplit

# Install dependencies
npm install

# Copy environment configuration
cp .env.testnet .env

# Compile smart contracts
npm run compile

# Run smart contract tests
npm run test:contracts
```

## 🏃‍♂️ Running the Project

```bash
# Start the development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Deploy smart contracts to Base Sepolia testnet
npm run deploy:testnet

# Deploy to Base mainnet
npm run deploy:mainnet
```

## 📷 Screenshots

<!-- Add screenshots of your project here -->

## 🔮 Future Plans

- **Real-time WebSocket Integration** - Live payment notifications and status updates
- **Enhanced Organizer Dashboard** - Comprehensive bill management interface
- **On-ramp Integration** - Direct USDT purchase within the application
- **Farcaster Frame Integration** - Social sharing with embedded payment actions
- **Gas Sponsorship** - ERC-4337 Paymaster for gasless transactions
- **Multi-chain Support** - Expand to other EVM-compatible networks
- **Receipt OCR** - Automatic bill parsing from restaurant receipts
- **ENS Integration** - Display ENS names instead of wallet addresses
- **Advanced Analytics** - Detailed spending insights and group statistics

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
