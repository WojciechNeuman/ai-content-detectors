from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def update_model_metrics(df, model_name, y_true, y_pred):
    """
    Calculate metrics for the given model and update the DataFrame with those metrics.

    Parameters:
    - df: DataFrame to update
    - model_name: Name of the model (e.g., 'BiLSTM (RNN)')
    - y_true: True labels
    - y_pred: Predicted labels

    Returns:
    - Updated DataFrame
    """

    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    # Round all metrics to 3 decimal places
    accuracy = round(accuracy, 3)
    f1 = round(f1, 3)
    precision = round(precision, 3)
    recall = round(recall, 3)

    # Update the row corresponding to the model_name
    df.loc[df['model'] == model_name, 'accuracy'] = accuracy
    df.loc[df['model'] == model_name, 'precision'] = precision
    df.loc[df['model'] == model_name, 'recall'] = recall
    df.loc[df['model'] == model_name, 'f1_score'] = f1

    return df
