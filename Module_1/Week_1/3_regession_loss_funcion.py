import random
import math


def calculate_loss(num_samples, loss_name):
    # Check if num_samples is a valid integer number
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    num_samples = int(num_samples)

    # Validate the loss name
    if loss_name not in ['MAE', 'MSE', 'RMSE']:
        print(f"{loss_name} is not supported")
        return

    samples = []
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        samples.append((predict, target))

    if loss_name == 'MAE':
        loss = sum(abs(p - t) for p, t in samples) / num_samples
    elif loss_name == 'MSE':
        loss = sum((p - t) ** 2 for p, t in samples) / num_samples
    elif loss_name == 'RMSE':
        mse = sum((p - t) ** 2 for p, t in samples) / num_samples
        loss = math.sqrt(mse)

    # Print the results
    for i, (predict, target) in enumerate(samples):
        print(
            f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {abs(predict - target)}")

    print(f"final {loss_name}: {loss}")


# Example usage
calculate_loss("5", "RMSE")
calculate_loss("aa", "RMSE")
