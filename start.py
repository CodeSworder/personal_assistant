import os

os.system('xtuner train config/internlm_chat_7b_qlora_oasst1_e3_copy.py')
os.system('
# 创建用于存放Hugging Face格式参数的hf文件夹
mkdir config/work_dirs/hf;

export MKL_SERVICE_FORCE_INTEL=1;

# 配置文件存放的位置
export CONFIG_NAME_OR_PATH=config/internlm_chat_7b_qlora_oasst1_e3_copy.py;

# 模型训练后得到的pth格式参数存放的位置
export PTH=config/work_dirs/internlm_chat_7b_qlora_oasst1_e3_copy/epoch_3.pth;

# pth文件转换为Hugging Face格式后参数存放的位置
export SAVE_PATH=config/work_dirs/hf;

# 执行参数转换
xtuner convert pth_to_hf $CONFIG_NAME_OR_PATH $PTH $SAVE_PATH;
export MKL_SERVICE_FORCE_INTEL=1;
export MKL_THREADING_LAYER='GNU';

# 原始模型参数存放的位置
export NAME_OR_PATH_TO_LLM=Shanghai_AI_Laboratory/internlm-chat-7b;

# Hugging Face格式参数存放的位置
export NAME_OR_PATH_TO_ADAPTER=config/work_dirs/hf;

# 最终Merge后的参数存放的位置
mkdir config/work_dirs/hf_merge;
export SAVE_PATH=config/work_dirs/hf_merge;

# 执行参数Merge
xtuner convert merge \
    $NAME_OR_PATH_TO_LLM \
    $NAME_OR_PATH_TO_ADAPTER \
    $SAVE_PATH \
    --max-shard-size 2GB;
pip install streamlit==1.24.0
')
os.system('streamlit run code/InternLM/web_demo.py --server.address 127.0.0.1 --server.port 6006')