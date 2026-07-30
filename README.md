---
title: AI Developer Assistant - Miço
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: mit
python_version: "3.11"
---
LLM destekli, geliştiricilere yönelik akıllı bir yardımcı uygulamasıdır.

Bu proje, **Ollama üzerinde çalışan Qwen3 modeli** ile kullanıcı isteğini analiz eder, gerekli araçları (Tool Calling) otomatik olarak seçer ve elde edilen sonuçları birleştirerek kullanıcıya anlamlı ve kapsamlı bir cevap üretir.

Projede tamamen yerel (local) çalışan bir ajan mimarisi kullanılmıştır.

---

# 🚀 Özellikler

- 🧠 LLM tabanlı Tool Planning
- 🔧 Tool Calling
- 📦 Structured Output (Pydantic)
- 📚 PyPI paket araştırması
- ⭐ GitHub repository araştırması
- 💬 Stack Overflow soru araştırması
- 🔄 Çoklu araç (Multi Tool) desteği
- 🎨 Gradio tabanlı kullanıcı arayüzü
- 🖥️ Tamamen lokal çalışabilme (Ollama)

---

# 🏗️ Sistem Mimarisi

```text
                    Kullanıcı
                        │
                        ▼
               Planner (Qwen3)
                        │
                        ▼
            Structured Tool Plan
                        │
                        ▼
                 Tool Executor
         ┌────────┬────────┬────────┐
         ▼        ▼        ▼
      PyPI     GitHub   StackOverflow
         └────────┴────────┴────────┘
                        │
                        ▼
              Tool Sonuçları
                        │
                        ▼
              Responder (Qwen3)
                        │
                        ▼
                  Nihai Cevap
```

---

# 📂 Proje Yapısı

```text
developer-assistant-tool-call/

├── llm/
│   ├── client.py
│   ├── planner.py
│   ├── responder.py
│   └── schemas.py
│
├── tools/
│   ├── github_tool.py
│   ├── pypi_tool.py
│   ├── stackoverflow_tool.py
│   └── registry.py
│
├── models/
│   ├── tool_models.py
│   └── trace_models.py
│
├── prompts/
│   ├── planner_prompt.txt
│   └── responder_prompt.txt
│
├── utils/
│   └── logger.py
│
├── executor.py
├── agent.py
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 🛠️ Kullanılan Teknolojiler

- Python
- Ollama
- Qwen3:4B
- Gradio
- Pydantic
- Requests
- Rich
- GitHub REST API
- PyPI API
- Stack Exchange API

---

# ⚙️ Kurulum

## 1. Repoyu klonlayın

```bash
git clone https://github.com/kullanici_adi/developer-assistant-tool-call.git

cd developer-assistant-tool-call
```

---

## 3. Gerekli paketleri yükleyin

```bash
pip install -r requirements.txt
```

---

## 4. Ollama'yı kurun

https://ollama.com/

---

## 5. Qwen3 modelini indirin

```bash
ollama pull qwen3:4b
```

---

## 6. Ollama'yı başlatın

```bash
ollama serve
```

---

## 7. Uygulamayı çalıştırın

```bash
python app.py
```

---

# 💡 Örnek Kullanım

Aşağıdaki gibi çok adımlı sorular sorabilirsiniz.

```
FastAPI ve Flask frameworklerini karşılaştır.

• Güncel PyPI sürümlerini getir.
• Resmi GitHub repositorylerini bul.
• Stack Overflow üzerindeki popüler soruları araştır.
• Avantaj ve dezavantajlarını özetle.
```

---

# 📸 Ekran Görüntüleri

## Uygulama Arayüzü

![Uygulama](images/app.png)

---

## Planner Analizi

![Planner](images/planner.png)

---

## Tool Planı ve Tool Sonuçları

![Tools](images/tools.png)

---

## Nihai Cevap

![Final Answer](images/final_answer.png)

---

# 🔍 Desteklenen Araçlar

## 📦 PyPI

- Paket bilgileri
- Güncel sürüm
- Lisans bilgisi
- Python sürüm gereksinimi
- Açıklama

---

## ⭐ GitHub

- Repository arama
- Repository bilgileri
- Açıklama
- Yıldız sayısı
- Fork sayısı
- Lisans

---

## 💬 Stack Overflow

- Benzer teknik sorular
- Oy sayısı
- Kabul edilen cevap bilgisi
- Etiketler
- Soru bağlantıları

