{
    output_dir: 'results/mistral',
    model_id: 'mistralai/Mistral-7B-Instruct-v0.3',
    temperature: 0.0,
    max_tokens: 2048,
    tensor_parallel_size: 1,
    gpu_memory_utilization: 0.9,
    dtype: 'auto',
    max_model_len: 8192,
    system_message: null,
    datasets: ['hellaswag', 'race', 'wandi', 'logic'],
    dataset_path: null,
    template_path: null,
}
