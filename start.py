import os
os.system('pwd;ls')
# 定义要执行的所有命令
commands = """
bash;
conda create --name personal_assistant --clone=/root/share/conda_envs/internlm-base;
conda activate personal_assistant;
cd ~;
mkdir /root/personal_assistant && cd /root/personal_assistant;
mkdir /root/personal_assistant/xtuner019 && cd /root/personal_assistant/xtuner019;
git clone -b v0.1.9  https://github.com/InternLM/xtuner;
cd xtuner;
pip install -e '.[all]';
cd /home/xlab-app-center/xtuner019/xtuner;
pip install -e '.[all]';
xtuner train /home/xlab-app-center/config/internlm_chat_7b_qlora_oasst1_e3_copy.py;
mkdir code;cd code;
git clone https://gitee.com/internlm/InternLM.git;
cd InternLM;
git checkout 3028f07cb79e5b1d7342f4ad8d11efad3fd13d17;
mkdir /home/xlab-app-center/config/work_dirs/hf;
export MKL_SERVICE_FORCE_INTEL=1;
export CONFIG_NAME_OR_PATH=./config/internlm_chat_7b_qlora_oasst1_e3_copy.py;
export PTH=./config/work_dirs/internlm_chat_7b_qlora_oasst1_e3_copy/epoch_3.pth;
export SAVE_PATH=./config/work_dirs/hf;
xtuner convert pth_to_hf $CONFIG_NAME_OR_PATH $PTH $SAVE_PATH;
export MKL_SERVICE_FORCE_INTEL=1;
export MKL_THREADING_LAYER='GNU';
export NAME_OR_PATH_TO_LLM=Shanghai_AI_Laboratory/internlm-chat-7b;
export NAME_OR_PATH_TO_ADAPTER=./config/work_dirs/hf;
mkdir /home/xlab-app-center/config/work_dirs/hf_merge;
export SAVE_PATH=./config/work_dirs/hf_merge;
xtuner convert merge $NAME_OR_PATH_TO_LLM $NAME_OR_PATH_TO_ADAPTER $SAVE_PATH --max-shard-size 2GB;
pip install streamlit==1.24.0
"""

# 通过os.system()执行所有命令
os.system(commands)

os.system('streamlit run /home/xlab-app-center/code/InternLM/web_demo.py --server.address 127.0.0.1 --server.port 6006')