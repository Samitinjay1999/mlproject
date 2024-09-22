import os
import sys
import dill
from src.exception import CustomException


def save_object(file_path, obj):
    """
    Saves a Python object to a file using dill.

    Parameters:
    - file_path (str): The path where the object should be saved.
    - obj: The Python object to save.

    Raises:
    - CustomException: If an error occurs during saving.
    """
    try:
        # Create the directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Save the object to the specified file
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
