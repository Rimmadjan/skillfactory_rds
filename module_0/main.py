def guess_number(low, high, target):
    attempts = 0

    while low <= high:
        attempts += 1
        mid = (low + high) // 2  # Calculate the middle of the range
        print(f"Attempt {attempts}: guessed number is {mid}")

        if mid == target:
            print(f"Number {target} guessed in {attempts} attempts!")
            return attempts
        elif mid < target:
            print(f"Number {mid} is less than the target.")
            low = mid + 1  # Narrow the range upwards
        else:
            print(f"Number {mid} is greater than the target.")
            high = mid - 1  # Narrow the range downwards