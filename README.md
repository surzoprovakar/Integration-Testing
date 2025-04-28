# 🧪 ER-π: Exhaustive Integration Testing for Replicated Data Libraries Integration

This project introduces a comprehensive integration testing framework designed to **improve the reliability and correctness of replicated data libraries** by exploring **optimized interleaving** of interactions between application logic and library behavior.

## Overview

Distributed systems often rely on replicated data libraries to maintain availability and performance under network partitions. However, **ensuring correctness across all possible operation interleavings** is notoriously difficult.

This project addresses that challenge by:
- Applying **domain-specific constraints** to intelligently **prune the interleaving space**.
- Replaying **critical interactions** between the application and libraries to reveal inconsistencies or violations.
- Supporting **multi-language libraries** (Go, Java, JavaScript) for broader applicability.
- Using **Datalog-based specifications** to define and enforce system-wide invariants.

## Key Features

- ⚡ **Optimized Interleaving Replay**: Reduces the number of test executions needed by focusing only on meaningful interleavings.
- 🌐 **Multi-language Support**: Integration testing for libraries written in Go, Java, and JavaScript.
- 🛠️ **Domain-Specific Constraint System**: Customize the exploration space based on application-specific knowledge.
- 📈 **Improved Test Coverage**: Boosts integration test coverage by **32%** over traditional random or exhaustive approaches.
- 🔎 **Invariant Checking with Datalog**: Expresses complex correctness properties in a concise, declarative manner.

## Technologies Used

- **Go**, **Java**, **JavaScript** — client libraries under test.
- **Datalog** — to model and enforce consistency constraints.
- **Custom Test Harness** — for orchestrating test runs and interleaving control.

## Motivation

Integration testing across replicated systems can miss critical bugs if interleavings are not exhaustively explored.

This project strikes a balance by leveraging **domain-specific knowledge** to **optimize** the exploration of behaviors that are most likely to uncover real-world bugs.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/surzoprovakar/Integration-Testing.git
   cd Integration-Testing

2. Run:
   ```bash
   Command *redis-server* from a CLI.
   Navigate from another CLI to the library directory where the Makefile is located.
   command *make all*.
   Example_Go: open two CLIs inside **Library** directory and command *./r1.sh* and *./r2.sh*.
   Example_Java: *gradle test*.
   Example_JS: *npm test*.
   *make clean*.
