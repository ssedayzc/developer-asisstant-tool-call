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

LLM destekli, geliştiricilere yönelik akıllı bir araştırma ve yardımcı asistan uygulamasıdır.

Miço, kullanıcı isteğini analiz eder, gerekli araçları otomatik olarak seçer ve farklı kaynaklardan elde ettiği sonuçları birleştirerek anlaşılır bir nihai cevap üretir.

Proje, **Hugging Face Inference Providers üzerinden çalışan Qwen3 modeli**, yapılandırılmış çıktı üretimi ve çoklu araç kullanımı üzerine kurulmuştur.

## 🚀 Özellikler

- LLM tabanlı Tool Planning
- Otomatik Tool Calling
- Pydantic ile Structured Output
- PyPI paket araştırması
- GitHub repository araştırması
- Stack Overflow soru araştırması
- Çoklu araç desteği
- Planner, Executor ve Responder mimarisi
- Gradio tabanlı kullanıcı arayüzü
- Hugging Face Spaces üzerinde canlı kullanım

## 🏗️ Sistem Mimarisi

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
          ┌────────┬───────────────┬────────┐
          ▼        ▼               ▼
        PyPI     GitHub      Stack Overflow
          └────────┴───────────────┴────────┘
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

## 📂 Proje Yapısı

```text
developer-asisstant-tool-call/

├── llm/
│   ├── client.py
│   ├── planner.py
│   ├── responder.py
│   └── schemas.py
│
├── models/
│   ├── tool_models.py
│   └── trace_models.py
│
├── prompts/
│   ├── planner_prompt.txt
│   └── responder_prompt.txt
│
├── tools/
│   ├── github_tool.py
│   ├── pypi_tool.py
│   ├── stackoverflow_tool.py
│   └── registry.py
│
├── utils/
│   └── logger.py
│
├── agent.py
├── app.py
├── config.py
├── executor.py
├── requirements.txt
└── README.md
```

## 🛠️ Kullanılan Teknolojiler

- Python
- Qwen3
- Hugging Face Inference Providers
- Hugging Face Spaces
- Gradio
- Pydantic
- Requests
- Rich
- GitHub REST API
- PyPI API
- Stack Exchange API

## ⚙️ Yerel Kurulum

### 1. Repoyu klonlayın

```bash
git clone https://github.com/ssedayzc/developer-asisstant-tool-call.git
cd developer-asisstant-tool-call
```
### 2. Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

### 3. Ortam değişkenlerini ayarlayın

`.env` dosyasını aşağıdaki biçimde düzenleyin:

```env
HF_MODEL=Qwen/Qwen3-4B-Instruct-2507
HF_PROVIDER=auto
HF_TOKEN=hf_xxxxxxxxxxxxxxxxx
GITHUB_TOKEN=
```

`HF_TOKEN`, Hugging Face Inference Providers üzerinden model çağrısı yapmak için kullanılır.

`GITHUB_TOKEN` isteğe bağlıdır. Eklendiğinde GitHub API istek limitinin artırılmasına yardımcı olur.

### 4. Uygulamayı çalıştırın

```bash
python app.py
```

Hugging Face `InferenceClient`, farklı inference sağlayıcılarına ortak bir arayüz üzerinden bağlanır ve `chat_completion` çağrılarını destekler. :contentReference[oaicite:1]{index=1}

## 🌐 Hugging Face Spaces Dağıtımı

Space ayarlarında aşağıdaki secret tanımlanmalıdır:

```text
Name: HF_TOKEN
Value: hf_xxxxxxxxxxxxxxxxx
```

İsteğe bağlı olarak GitHub token da eklenebilir:

```text
Name: GITHUB_TOKEN
Value: github_token_değeri
```

Token değerleri doğrudan kaynak kod içine yazılmamalıdır.

## 💡 Örnek Kullanım

```text
FastAPI ve Flask frameworklerini karşılaştır.

- Güncel PyPI sürümlerini getir.
- Resmi GitHub repositorylerini bul.
- Stack Overflow üzerindeki ilgili soruları araştır.
- Avantaj ve dezavantajlarını özetle.
```

Bu sorgu sırasında Planner gerekli araç çağrılarını oluşturur, Executor araçları çalıştırır ve Responder sonuçları tek bir cevapta birleştirir.

## 📸 Ekran Görüntüleri

### Uygulama Arayüzü

![Uygulama arayüzü](images/app.png)

### Planner Analizi

![Planner analizi](images/planner.png)

### Tool Planı ve Tool Sonuçları

![Tool sonuçları](images/tools.png)

### Nihai Cevap

![Nihai cevap](images/final_answer.png)

## 🔍 Desteklenen Araçlar

### 📦 PyPI

- Güncel paket sürümü
- Paket açıklaması
- Lisans bilgisi
- Python sürüm gereksinimi
- Proje bağlantıları

### ⭐ GitHub

- Repository arama
- Repository açıklaması
- Yıldız ve fork sayısı
- Lisans bilgisi
- Dil ve proje bağlantıları

### 💬 Stack Overflow

- İlgili teknik sorular
- Oy sayısı
- Kabul edilmiş cevap durumu
- Soru etiketleri
- Soru bağlantıları
