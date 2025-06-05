# 🤖 LLM-Based Review Feedback Pipeline

This module contains the logic for running **LLM-based batch processing** of customer reviews.  
It supports **sentiment classification**, **improvement feedback generation**, and **category classification** using **Gemini Flash**.

---

## 🧠 Pipeline Overview

Input CSV (raw reviews) <br>
⬇<br>
Prompt Builder (Few-shot)<br>
⬇<br>
LLM Inference (Gemini Flash)<br>
⬇<br>
Response Cleaning & Validation<br>
⬇<br>
Retry Failed IDs (via retry_failed_reviews)<br>
⬇<br>
CSV Save / Result Merge

---

## 🧩 Key Components

### `analyze_reviews_with_id(df, batch_size, checkpoint_path, fail_log_path)`
- Main pipeline to classify sentiment and generate improvement feedback
- Uses:
  - `build_sentiment_prompt()`
  - `build_feedback_prompt()`
  - `safe_generate()`
  - `clean_json_response()`
  - `validate_llm_response()`
- Saves results batch-wise and supports retrying failed reviews

---

### `build_sentiment_prompt(df)`
- Constructs a structured prompt for sentiment classification
- Output fields:
  - `id`, `sentiment` (`positive`, `negative`, `improvement`)
  - `reason`, `confidence` (0~1)

---

### `build_feedback_prompt(df)`
- Generates improvement feedback suggestions for each review
- Output:
  ```json
  {
    "id": "123",
    "feedback": "Improve fabric quality for better durability."
  }

---

### `build_category_prompt(df)`
- Classifies feedback into one of the predefined categories:
	- "Shipping", "Quality", "Design", "Price", "Service", "Other"
- Uses Few-shot prompting with manually defined examples

---

### `categorize_feedbacks(df_feedback, batch_size)`
- Main function for batch category classification
- Automatically skips previously processed IDs using checkpoints
- Validates LLM response using `validate_llm_response()`
- Stores results in a cumulative CSV

---

### Error Handling via `retry_failed_reviews()`
- Failed responses (e.g., JSON parse errors or LLM timeout) are retried in a separate pass
- Failed IDs are stored and merged after retry
- Prevents data loss without relying on fail_log.txt

---

## 🤖 Model Summary

| Model         | Provider | Notes                  |
|---------------|----------|------------------------|
| Gemini Flash  | Google   | Fast & cost-effective  |

---

## 📁 File Summary

| File Name               | Purpose                                      |
|------------------------|----------------------------------------------|
| `analyze_reviews_with_id` | Sentiment & feedback batch pipeline         |
| `build_sentiment_prompt` | Sentiment classification prompt builder     |
| `build_feedback_prompt`  | Feedback generation prompt builder          |
| `build_category_prompt`  | Feedback-to-category prompt builder         |
| `categorize_feedbacks`   | Batch category classification logic         |
| `retry_failed_reviews`   | Retry logic for failed IDs                  |
| `clean_json_response`    | JSON cleaner for LLM responses              |
| `safe_generate`          | Retry-safe LLM request handler              |
| `validate_llm_response`          | Validates LLM response using `id`           |

---

### 👤 Author  
**Aspyn** | AI Product Review Analysis Project  
🔗 [GitHub](https://github.com/Aspyn25)  
🔗 [LinkedIn](https://www.linkedin.com/in/aspyn25)  
🔗 [Kaggle](https://www.kaggle.com/code/jeonghyunsong/ai-based-product-review-feedback-generator)