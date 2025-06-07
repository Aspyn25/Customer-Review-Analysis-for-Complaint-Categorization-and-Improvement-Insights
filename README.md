# 📌 Customer Review Analysis for Complaint Categorization and Improvement Insights



## Project Overview

This project focuses on analyzing customer reviews to identify areas for product improvement. It leverages Large Language Models (LLMs) to classify sentiments and generate actionable suggestions based on the content of each review.

The primary goal was to help businesses extract valuable insights from review data—such as what customers liked, what frustrated them, and what could be improved—and transform them into structured, useful information that supports product and service decisions.



## 📊 Dataset Description

- **Source**: `amazon_reviews.csv`
- **Size**: ~10,000 reviews
- **Key Fields**:
  - `review`: raw customer review
  - `sentiment`: positive, negative, improvement (LLM-generated)
  - `feedback`: improvement suggestion (LLM-generated)
  - `category`: manually/semi-automatically tagged feedback category



## 🎯 Project Goals

- Analyze large-scale customer review data  
- Classify sentiment and generate feedback automatically  
- Categorize improvement areas for better product strategy  
- Visualize common themes and complaints using charts and NLP tools


## 🔄 Project Workflow

1. **Raw Review Collection**: Load and review unstructured customer feedback  
2. **Preprocessing**: Clean and prepare the data (e.g., batching)  
3. **Sentiment Classification**: Use LLMs to assign sentiment labels  
4. **Feedback Generation**: Generate suggestions for negative/improvement reviews  
5. **Feedback Categorization**: Tag each feedback item by theme (quality, content, etc.)  
6. **Merging & Structuring**: Combine model outputs with original reviews  
7. **Visualization & Analysis**: Use WordClouds, n-grams, and keyword frequency analysis  
8. **Insight Generation**: Identify top issues by category and sentiment



## 📊 Key Outputs

- **Sentiment Distribution Chart**: Visual breakdown of positive, negative, and improvement reviews  
- **WordClouds by Sentiment/Category**: Visual summary of key terms in each group  
- **Top Bigrams**: Most frequent word pairs used in feedback  
- **Category-wise Complaint Analysis**: Themes like design, quality, content, etc.



## 💡 Key Insights

- **Design** and **Quality** were the most frequently criticized areas  
- Product descriptions often failed to reflect real user experience  
- Negative reviews were short and emotion-driven, while improvement reviews offered more constructive suggestions  
- Category-based analysis helped uncover specific, actionable feedback trends



## ✅ Conclusion

This project demonstrates how customer reviews—when processed with the right tools—can offer meaningful direction for product development and user satisfaction. By combining NLP techniques with visual analytics, businesses can better prioritize improvements and track recurring concerns in real time.


## 🔗 Access the Project

- **GitHub Repository**: [github.com/Aspyn25/Customer-Review-Analysis-for-Complaint-Categorization-and-Improvement-Insights](https://github.com/Aspyn25/Customer-Review-Analysis-for-Complaint-Categorization-and-Improvement-Insights)  
- **Interactive Dashboard**: [Streamlit App](https://da7xrgatbqek7awwkswkqx.streamlit.app/)  
- **LLM Pipeline Details**: See `llm/README.md` for technical implementation of the LLM-based processing
[llm/README.md](https://github.com/Aspyn25/Customer-Review-Analysis-for-Complaint-Categorization-and-Improvement-Insights/tree/main/LLM)
## Auther
**Aspyn (Jeonghyun Song)** <br>
🔗 [GitHub](https://github.com/Aspyn25)  
🔗 [LinkedIn](https://www.linkedin.com/in/aspyn25)  
🔗 [Kaggle](https://www.kaggle.com/code/jeonghyunsong/ai-based-product-review-feedback-generator)
