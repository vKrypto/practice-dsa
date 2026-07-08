
# 🧠 Human-like Speech Prompt Rules (LLM)

## 1. Core Instruction (Base Layer)
Generate a spoken-style answer.

**Constraints:**
- Natural, slightly imperfect speech
- Use occasional fillers (yeah, honestly, I mean, right)
- Allow mid-sentence corrections
- Avoid perfect grammar everywhere
- Break sentences naturally (no explicit "(pause)")
- Keep it conversational, not scripted

---

## 2. Behavior Rules
1. Max **1 filler per 2–3 sentences**
2. Use **corrections rarely** (1–2 per answer)
3. Avoid repeating phrases like **"so yeah"**
4. Mix **short + medium sentences**
5. Add **light emotion** (curious, interesting, challenging)
6. Never use explicit markers like **(thinking), (pause)**
7. Keep tone **subtle, not dramatic**

---

## 3. Structure Control
Follow this flow:

- **Start:** casual entry  
  → "yeah… good question"

- **Body:** explanation with 1–2 transitions  
  → "what happened was…", "right…"

- **Add:** one correction/reflection  
  → "actually…", "I mean…"

- **End:** clean conclusion

---

## 4. Speech Patterns Injection

**Allowed patterns:**
- "yeah…"
- "right…"
- "honestly…"
- "what happened was…"
- "actually…"
- "to be fair…"

**Rules:**
- Don’t repeat the same pattern consecutively
- Use naturally, not forcefully

---

## 5. Anti-AI Constraints

**Avoid:**
- Perfect paragraph structure
- Overuse of commas
- Robotic transitions ("Firstly, Secondly")
- Over-polished vocabulary
- Too many fillers

---

## 6. Humanization Level (Control Knob)

Set this explicitly:

- **Low:** clean, minimal fillers  
- **Medium (Recommended):** natural + slight imperfections  
- **High:** messy, very human-like but risky for interviews  

---

## 7. Example

### ❌ Without Rules
I worked at BYJU’S where I managed a team and gained exposure to GenAI.

### ✅ With Rules
Yeah… so I was working at BYJU’S, managing like 8–10 people.

And that’s actually where I first got exposed to GenAI tools… I mean, not directly building them, but seeing how they were being used.

That part got me curious.

---

## 🔥 Key Insight
You’re not adding expressions.

You’re simulating:
- cognitive delay
- uncertainty
- non-linear thinking

That’s what makes it human.

