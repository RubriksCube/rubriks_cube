
# Usage

```python
from datasets import HellaswagDataset, LogicDataset, RaceDataset, WandiDataset

hellaswag = HellaswagDataset()
logic = LogicDataset()
race = RaceDataset()
wandi = WandiDataset()

# Iterate over the datasets
for example in hellaswag:
    print(example)

    # Print special fields added by the data loader
    # Special key added by the data loader 
    print(example['__instance_index']) 
    
    # The rendered string from the template
    print(example['__rendered_text']) 
```


## Customize template and data path
```python
from datasets import HellaswagDataset

hellaswag = HellaswagDataset(
    template_path='path/to/template', # Path to the jinja2 template file
    data_path='path/to/data' # Path to the jsonlines data file
)
```
