# Roleplay-Model

#For download the GGUF file 

huggingface-cli download TheBloke/WestLake-7B-v2-GGUF westlake-7b-v2.Q6_K.gguf --local-dir . --local-dir-use-symlinks False
 

#For install llama-cpp

CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir