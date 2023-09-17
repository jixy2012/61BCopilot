# 61BCopilot
An agent backed by openai's gpt to answer student questions on ed.


## Agent Workflow

---

**EdPilot for 61B - Agent Workflow**

---

**1. User Input Reception:**
- The system starts by receiving a student's question.

---

**2. Initial Categorization by the Agent:**
- The agent classifies the student's question into categories such as logistics, course material, specific problems, etc.

---

**3. Preliminary Answer Generation:**
- The agent formulates an initial answer based on the categorized question.

---

**4. Assessment of External Information Needs:**
- The agent evaluates which external information, if any, is essential to substantiate or enhance its initial answer.

---

**5. Iterative Database Query Loop:**
- The agent enters an iterative process where:
  - It queries the Qdrant vector database based on current information needs.
  - Extracts relevant vectors or data points to refine the answer.
  - Re-evaluates if more external information is required.
  - Continues with another iteration if further data is needed or exits the loop if sufficient information has been gathered.

---

**6. Enhanced Answer Generation by the Agent:**
- Using the compiled data from Qdrant, the agent crafts a detailed and refined answer.

---

**7. Confidence Assessment:**
- The agent gauges its confidence in the crafted response based on:
  - Number of iterations in the database query loop.
  - Amount of external data incorporated vs. base knowledge.
  - (Optionally, any internal mechanisms that could be integrated later for direct confidence assessment).

---

**8. Answer Finalization:**
- If the agent determines it can't provide a sufficient answer even after exhaustive data gathering, it will indicate its inability and specify the reasons.
- Otherwise, it prepares the response, incorporating citations for its answers.

---

**9. Staff Review:**
- Every answer, irrespective of confidence, is directed to staff for review. Staff can see the agent's confidence rating along with the answer, allowing them to approve, amend, or reject the response.

---

**10. Return Response:**
- Upon staff approval, the answer is dispatched to the student. The student remains unaware of the confidence metric.

---

**11. Feedback Collection:**
- Students are prompted to rate or provide commentary on the received answer.

---

**12. Continuous Monitoring:**
- Metrics, user feedback, and other relevant KPIs are persistently tracked to ensure optimal agent functionality.

---

This representation should offer a clearer depiction of the agent's workflow while emphasizing its capabilities and processes.