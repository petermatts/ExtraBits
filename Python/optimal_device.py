import torch
# import importlib

def vprint(msg: str, verbose: bool) -> None:
    if verbose:
        print(msg)
    

def get_optimal_device(verbose: bool = False) -> torch.device:
    """
    Usage:
        device = get_optimal_device()
        model.to(device)
        tensor.to(device)
    """
    # # Try TPU (XLA) if available
    # xla_spec = importlib.util.find_spec("torch_xla.core.xla_model")
    # if xla_spec is not None:
    #     try:
    #         import torch_xla.core.xla_model as xm
    #         device = xm.xla_device()
    #         vprint("Using TPU (XLA) device.", verbose)
    #         vprint(f"    XLA device: {device}", verbose)
    #         return device
    #     except Exception as e:
    #         vprint(f"TPU detected but failed to initialize: {e}", verbose)

    # CUDA
    if torch.cuda.is_available():
        device = torch.device("cuda")
        num_devices = torch.cuda.device_count()
        vprint(f"Using CUDA. {num_devices} device(s) detected:", verbose)
        for i in range(num_devices):
            props = torch.cuda.get_device_properties(i)
            total_mem = round(props.total_memory / (1024 ** 3), 2)
            vprint(f"  [{i}] {props.name} - {total_mem} GB VRAM", verbose)

        current_id = torch.cuda.current_device()
        used_mem = round(torch.cuda.memory_allocated(current_id) / (1024 ** 2), 2)
        reserved_mem = round(torch.cuda.memory_reserved(current_id) / (1024 ** 2), 2)
        vprint(f"\tMemory usage (Device {current_id}): Allocated {used_mem} MB / Reserved {reserved_mem} MB", verbose)
        vprint(f"\tMixed Precision Support (AMP): {'Yes' if torch.cuda.is_bf16_supported() else 'No'}", verbose)
        return device #? support returning multiple devices if more than 1 detected

    # MPS (Apple Silicon)
    elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
        device = torch.device("mps")
        vprint("Using Apple Metal Performance Shaders (MPS) backend.", verbose)
        vprint("\tNote: MPS does not yet support advanced memory queries in PyTorch.", verbose)
        return device

    # CPU fallback
    else:
        device = torch.device("cpu")
        vprint(f"No GPUs available. Using CPU. Device: {device}", verbose)
        return device

# Example usage
# if __name__ == "__main__":
#     device = get_optimal_device()