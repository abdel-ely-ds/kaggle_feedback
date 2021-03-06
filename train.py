from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification

BS = 4
GRAD_ACC = 8
LR = 5e-5
WD = 0.01
WARMUP = 0.1
N_EPOCHS = 5


def create_training_args(
        model_name,
        load_best_model_at_end: bool = True,
        learning_rate: float = LR,
        per_device_train_batch_size: int = BS,
        per_device_eval_batch_size: int = BS,
        n_epochs: int = N_EPOCHS,
        weight_decay: float = WD,
        gradient_accumulation_steps: int = GRAD_ACC,
        warmup_ratio: float = WARMUP
):
    return TrainingArguments(
        output_dir=model_name,
        run_name=model_name,
        evaluation_strategy="epoch",
        logging_strategy="epoch",
        save_strategy="epoch",
        learning_rate=learning_rate,
        per_device_train_batch_size=per_device_train_batch_size,
        per_device_eval_batch_size=per_device_eval_batch_size,
        num_train_epochs=n_epochs,
        weight_decay=weight_decay,
        report_to="wandb",
        gradient_accumulation_steps=gradient_accumulation_steps,
        warmup_ratio=warmup_ratio,
        load_best_model_at_end=load_best_model_at_end,
    )


def create_data_collator(tokenizer):
    return DataCollatorForTokenClassification(tokenizer)


def create_trainer(model,
                   args=None,
                   train_dataset=None,
                   eval_dataset=None,
                   data_collator=None,
                   tokenizer=None,
                   compute_metrics=None,
                   ):
    trainer = Trainer(
        model,
        args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=data_collator,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics
    )
    return trainer
