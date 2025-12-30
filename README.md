# 🎓 Personalized Learning Recommendation System  
**Repository:** `ai-student-behavior-agent`  
**Type:** Internship Project (Documentation-Only)

> 🔒 **Confidentiality Notice**  
> This project was developed during my internship at **Carthaplay** and is based on **real internal user data** and **proprietary business rules**.  
> For confidentiality and intellectual property reasons, the **source code, datasets, and detailed configurations are not shared** in this repository.  
>  
> This repo serves as a **high-level technical and functional overview** for **portfolio and learning purposes** only.

---

## 🧠 Project Overview

The **Personalized Learning Recommendation System** is a **rule-based AI agent** that analyzes learner behavior and generates **personalized recommendations** inside an existing learning platform.

The system was integrated and used in a **real production environment**, helping:

- Learners to:
  - Stay engaged over time  
  - Progress more efficiently  
  - Receive content adapted to their **behavior**, **pace**, and **interaction patterns**

- Instructors & platform managers to:
  - Understand learner engagement profiles  
  - Identify at-risk learners  
  - Take targeted pedagogical actions  

---

## 🎯 Objectives

The main goals of the project were to:

1. **Detect and model user learning behaviors**
2. **Classify users** based on engagement and progress patterns
3. **Generate actionable, personalized recommendations**
4. **Support instructors and platform managers** with clear behavioral insights

The focus was on building a **practical, interpretable, and business-aligned system** rather than a black-box ML recommender.

---

## ⚙️ System Approach

Unlike purely ML-based recommendation engines, this solution is built around a **rule-based intelligence layer**, which makes it:

- ✅ **Interpretable** – Rules can be read, discussed, and adjusted by non-technical stakeholders  
- ✅ **Controllable** – Business teams can update strategies without retraining a model  
- ✅ **Robust with limited data** – Works well even when there isn’t a long history of user interactions  

### Core Components

#### 1. Behavior Detection Engine

Extracts behavioral signals from user activity logs, such as:

- **Session frequency** (how often users connect)
- **Content completion rate** (finished vs. started content)
- **Time spent per activity** (deep vs. shallow engagement)
- **Repetition and drop-off patterns** (where people give up or repeat)

#### 2. Rule-Based Decision System

Encodes pedagogical and business logic into **rules**, for example:

- **Engagement rules**  
  - High, medium, low engagement segments  
  - Reactivation triggers for dormant users  

- **Progression rules**  
  - Fast vs. slow progress  
  - Mastery and consolidation needs  

- **Risk detection rules**  
  - Potential **dropout**, **stagnation**, or **overload**  
  - Early-warning signals for instructors  

#### 3. Recommendation Generator

Turns interpreted behavior into **personalized outputs**:

- Tailored **content suggestions**
- Adjusted **learning paths**
- **Alerts and nudges** for inactive or at-risk users
- Insights for instructors (e.g., “This student is likely to stall in Module 3”)

---

## 🏗️ High-Level Architecture

```text
User Activity Logs
        ↓
Behavior Analysis Engine
        ↓
Rule-Based Logic Layer
        ↓
Personalized Recommendations
```

### Data Flow (Conceptual)

1. **User Activity Logs**  
   - Clicks, sessions, completions, time-on-task, etc. from the learning platform

2. **Behavior Analysis Engine**  
   - Cleans and aggregates signals  
   - Detects patterns such as “sporadic usage”, “binge learning”, “consistent progression”

3. **Rule-Based Logic Layer**  
   - Applies business and pedagogical rules  
   - Classifies user behavior and risk levels

4. **Personalized Recommendations**  
   - Suggests content, reminders, or interventions  
   - Delivered via platform APIs to the learner’s UI and instructor dashboards

---

## 🛠️ Technologies Used

- **Python**
  - Data processing and behavioral feature extraction
  - Rule engine and decision logic

- **Data Analysis Pipelines**
  - Preprocessing of logs and activity traces
  - Aggregations and metrics for behavior modeling

- **Rule-Based Logic System**
  - Encodes engagement and progression rules in a transparent manner

- **Backend Integration**
  - APIs to plug the recommendation logic into the existing learning platform

- **Monitoring & Evaluation Dashboards** (internal)
  - Track effectiveness of recommendations
  - Observe adoption and impact on user engagement

---

## 🚀 Key Learnings

Working on this project taught me to:

- **Translate educational theory into operational rules**  
  Turn abstract pedagogy and engagement models into concrete, testable logic.

- **Design interpretable AI systems**  
  Build AI that **stakeholders trust**, because they can see and understand how recommendations are made.

- **Handle real-world, noisy behavioral data**  
  Deal with missing logs, inconsistent patterns, and platform constraints.

- **Deploy under business and technical constraints**  
  Align AI logic with existing infrastructure, performance limits, and rollout strategies.

---

## 📂 About This Repository

This repository **does not contain**:

- Production source code  
- Real data  
- Sensitive configuration files or business rules

Instead, it provides:

- A **conceptual and architectural description** of the system  
- A summary of the **technical approach and design choices**  
- A reference for my **experience with real-world AI integration** in education technology

---

## 📌 Note & Contact

This is a **documentation-only** project created for **portfolio and discussion**.

If you’d like to **discuss the design, rule logic, or challenges** in more technical depth (within confidentiality limits), feel free to reach out:

- **Email:** [aya.mekni@esprim.tn](mailto:aya.mekni@esprim.tn)  
- **LinkedIn:** [aya-mekni](https://www.linkedin.com/in/aya-mekni)  
- **GitHub:** [@ayamekni](https://github.com/ayamekni)  


I’m happy to walk through:

- How rules were structured and prioritized  
- How behaviors were defined and validated  
- How this system could evolve into a **hybrid rule + ML recommender** in the future.
