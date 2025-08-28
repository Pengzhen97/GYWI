
# main.py
from src.pipeline.idea_generator import IdeaGenerator
from src.config import DEFAULTS

# ========= 手动输入区 =========
PAPER_ID = "2010.13337"          # 必填：目标论文ID（与 data_rag/updated_mcq_with_id_abstract.json 对齐）
TITLE = ""                       # 可选：留空则自动按数据集匹配
ABSTRACT = ""                    # 可选：留空则自动按数据集匹配

# 生成参数（如不需要改，可沿用默认）
N_HOPS       = 2                 # 图谱N跳邻居
TOP_K        = 10                # 最终TopK（仅用于构造展示，核心选片在下面三项）
HN_TOPK      = 1                 # 硬负样本数量
MAX_SELF     = 5                 # 自身论文取片数
MAX_NEIGHBOR = 4                 # 邻居论文取片数
MAX_RANDOM   = 1                 # 随机/负样本取片数
TEMPERATURE  = 0.7               # LLM 采样温度
COMPRESS_CTX = True              # 是否用压缩提示合并 GraphRAG+RAG 上下文
# =====================================

def run_once():
    gen = IdeaGenerator()
    result = gen.generate(
        paper_id=PAPER_ID,
        title=TITLE or None,
        abstract=ABSTRACT or None,
        n_hops=N_HOPS,
        top_k=TOP_K,
        hn_topk=HN_TOPK,
        max_self=MAX_SELF,
        max_neighbor=MAX_NEIGHBOR,
        max_random=MAX_RANDOM,
        temperature=TEMPERATURE,
        compress_context=COMPRESS_CTX,
        output_dir=DEFAULTS["output_dir"],  # 如需自定义，可改成你的路径
    )

    print("\n=== Generation Done ===")
    print(f"ID: {result['id']}")
    print(f"Title: {result['title']}")
    print(f"Result saved to: {result['paths']['result']}")
    print(f"Detail saved to: {result['paths']['detail']}")

if __name__ == "__main__":
    run_once()
