# 工具 - 結合 SDXL 與 Fast-3D 從而擁有三種功能

## 測試動機
> 目前在 HuggingFace 不乏許多 Text-to-3D 之 pipeline 可以使用，例如 OpenAI 的 [【shap-e】](https://huggingface.co/openai/shap-e) 以及 Microsoft 的 [【ldm3d】](https://huggingface.co/Intel/ldm3d)，但是呼叫的過程中只可輸入文字。

> 另外又有模型專門從事 Image-to-3D，比如 StablityAI 的 [【Stable-Fast-3D】](https://huggingface.co/stabilityai/stable-fast-3d)，相對指定載入圖檔。

> 因此好奇能否結合 Text-to-Image 與 Image-to-3D，模仿出 Text-to-3D 的模式。

> 相信透過這種方式，變相也能透過擴增的方式讓該工具帶有前述的三種功能。

## 使用工具
### 模型
- [【StablityAI】Stable Diffusion XL 1.0 - Turbo](https://huggingface.co/stabilityai/sdxl-turbo)
- [【StablityAI】Stable-Fast-3D](https://huggingface.co/stabilityai/stable-fast-3d)

### 端口
- [【　Groq　】Playground API](https://console.groq.com/playground)

## 測試環境
  `Windows 11` `Python 3.10.11` `CUDA 12.4` <br> `Visual Studio 2022 - 17.11.2` `【GPU】GeForce RTX3050 Ti`

## 設計邏輯
1. 選擇基底
  - 可以想像 Image-to-3D 將為主要的操作核心，本工具建立於原模型提供的 gradio_app.py 之上進行擴增

2. 新增功能
  - 文字輸入
    > 用戶能在此處輸入物件的敘述
  - 提詞優化
    > 用戶可能闡述過於簡單，且不清楚怎麼設計負面提詞，因此結合 LLM 進行設計與優化
  - 圖片生成
    > 接收優化後的題詞開始產生圖片

## 設備需求
- DISK
  - 閒置空間 -- 11 GB
- RAM
  - 整體空間 -- 16 GB
- GPU
  - 顯卡架構 -- RTX 20XX ⬆️
  - VRAM -- 8 GB

## 安裝方式
### Windows
1. 環境安裝
  - Python 3.10.11
    https://www.python.org/downloads/release/python-31011/
2. 複製專案
  - 
    ``` bat
    git clone https://github.com/babaochou2420/concept_text-to-3d.git
    ```
3. 套件安裝
  - 建立 venv 
      ``` bat
      py -3.10 -m venv .venv
      ```
      ``` bat
      .\.venv\Scripts\activate
      ```
  - 安裝套件
    ``` python
    pip install -U setuptools==69.5.1
    ```
    ``` python
    pip install wheel
    ```
    ``` python
    pip install -U -r .\requirements.txt
    ```
> [!IMPORTANT]
> PyTorch 請另外對應系統環境自行安裝

## 操作方式
> [!IMPORTANT]
> 首次執行需要 `huggingface-cli login` 並填寫兩份 StablityAI 模型的資料才可進行模型的下載

![](https://bbc-blog-storage.s3.ap-northeast-1.amazonaws.com/wp-content/uploads/2024/09/image-10.png)

### Gradio Interface
1. 進入 venv
  ``` bat
  .\.venv\Scripts\activate
  ```
2. 執行介面
  ``` python
  python ./app.py
  ```
3. 載入圖片
  - 文字生圖
  - 上傳圖檔

## $ Stable-Fast-3D 部分原稿

### CPU Support

CPU backend will automatically be used if no GPU is detected in your system.

If you have a GPU but are facing issues and want to use the CPU backend instead, set the environment variable `SF3D_USE_CPU=1` to force the CPU backend.

### Manual Inference

```sh
python run.py demo_files/examples/chair1.png --output-dir output/
```
This will save the reconstructed 3D model as a GLB file to `output/`. You can also specify more than one image path separated by spaces. The default options takes about **6GB VRAM** for a single image input.

You may also use `--texture-resolution` to specify the resolution in pixels of the output texture and `--remesh_option` to specify the remeshing operation (None, Triangle, Quad).

For detailed usage of this script, use `python run.py --help`.

## Remesher Options:

  -`none`: mesh unchanged after generation. No CPU overhead.

  -`triangle`: verticies and edges are rearranged to form a triangle topography. Implementation is from: *"[A Remeshing Approach to Multiresolution Modeling](https://github.com/sgsellan/botsch-kobbelt-remesher-libigl)" by M. Botsch and L. Kobbelt*. CPU overhead expected.

  -`quad`: verticies and edges are rearanged in quadrilateral topography with a proper quad flow. The quad mesh is split into triangles for export with GLB. Implementation is from *"[Instant Field-Aligned Meshes](https://github.com/wjakob/instant-meshes)" from Jakob et al.*. CPU overhead expected.

Additionally the target vertex count can be specified. This is not a hard constraint but a rough vertex count the method aims to create. This target is ignored if the remesher is set to `none`.

## Citation
```BibTeX
@article{sf3d2024,
  title={SF3D: Stable Fast 3D Mesh Reconstruction with UV-unwrapping and Illumination Disentanglement},
  author={Boss, Mark and Huang, Zixuan and Vasishta, Aaryaman and Jampani, Varun},
  journal={arXiv preprint},
  year={2024}
}
```
