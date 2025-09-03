# Generative AI, LLMs, and Beyond: Interview Prep Notes

## Introduction
*   From 2022 till now, **Generative AI** is a major topic.
*   Large Language Models (LLMs) from OpenAI and now Claude 3 (supported by Amazon) are doing amazing work.
*   It's important to understand **Generative AI** and how it differs from other terms like AI, ML, and DL.

## Artificial Intelligence (AI)
*   **Main Aim:** To build applications that can perform tasks **without human intervention**.
*   **Key Characteristic:** Performs tasks independently.
*   **Examples:**
    *   **Netflix's recommendation system:** Recommends movies based on your browsing, without human input.
    *   **Self-driving cars:** Drive themselves, handle turns, etc., autonomously.
*   **AI Engineers:** Create **AI products** that integrate with software like web apps, Android apps, or edge devices.

## Machine Learning (ML)
*   **Relationship:** **Machine Learning is a subset of AI**.
*   **Main Aim:** Provides **stats tools** to perform various tasks.
*   **Tasks Performed:**
    *   Statistical analysis.
    *   Visualization.
    *   Prediction.
    *   Forecasting.
*   **Purpose:** These tools help in the complete lifecycle of a data science project, from data ingestion to transformation and feature engineering.
*   **Focus:** It helps to **understand about the data** so it becomes meaningful and conveys information.
*   **Core:** It's all about using **stats tools** on data.

## Deep Learning (DL)
*   **Relationship:** **Deep Learning is a subset of Machine Learning**.
*   **History:** Not new, it existed since the 1950s. Its current fame is due to **technological advancements** like GPUs, open-source libraries, etc..
*   **Main Aim:** Built to **mimic the human brain** and how human beings learn.
*   **Key Concept:** Uses **multi-layered neural networks**.
*   **Three Important Components/Models in DL:**
    *   **ANN (Artificial Neural Networks):** Can be used to train machine learning problems.
    *   **CNN (Convolutional Neural Networks) & Object Detection:** Primarily for **computer vision** purposes. Techniques include R-CNN and others.
    *   **RNN (Recurrent Neural Networks) & its variants:** Used for **text-related use cases** and **time series use cases**. Variants include LSTM, GRU, Encoder-Decoder.
*   **Advanced Concepts (Crucial for Generative AI):**
    *   **Transformers and Berts:** These are very advanced and form the **backbone** for most LLM models in Generative AI.

## Generative AI
*   **Relationship:** **Generative AI is a subset of Deep Learning**.
*   **Core Idea:** It's about **generating new content** based on the content it has been trained on.
*   **Two Types of Models in Data Science Industry:**
    *   **Discriminative Models:**
        *   Mostly for tasks like **classification, prediction, regression**.
        *   Trained on **labeled datasets**.
    *   **Generative Models (Generative AI):**
        *   **Generates new data**.
        *   Trained on **huge datasets**.
*   **Two Main Types of Generative AI Models:**
    *   **Large Language Models (LLMs):**
        *   Works with **text data**.
        *   Given text, it provides a text response.
    *   **Large Image Models (LIMs):**
        *   Works with **images and videos**.
        *   Given text, it can convert that into an image or video.
*   **Key Players in LLMs (Foundation Models):**
    *   **OpenAI:** GPT-4, GPT-4 Turbo, GPT-5 (coming).
    *   **Meta:** Llama 2 (open source), Llama 3 (in pipeline).
    *   **Google:** Gemini, Gamma (open source).
    *   **Anthropic:** Claude 3 (fierce competitor to OpenAI GPT-4).
*   **Foundation Models / Pre-trained Models:**
    *   These models are trained on **huge amounts of data**, often the **entire internet data** (including code, etc.).
    *   They can be used for **domain-specific use cases**.
    *   **Fine-tuning:** A concept used to adapt these models with custom datasets for specific use cases (techniques like Laura are used).
    *   The current competition is to create the **best foundation model**.
*   **Frameworks & Applications:**
    *   **LangChain:** A framework that works with these models to help generate applications like **retrieval augmentation query** and **amazing chatbots**.
    *   **Impact:** LLMs are becoming very famous due to the chances of **automation**, especially in chatbot responses, and have a huge scope in multiple sectors.
*   **LIMs Example:** Stability AI is a company specifically working on large image models.