from rest_framework.response import Response
from rest_framework import status


def error_response(message="An error occurred", errors=None, status=status.HTTP_400_BAD_REQUEST):
    """
    Function to generate an error response.

    Args:
        errors (dict): The error details.
        status_code (int): The HTTP status code for the response (default: 400).
        message (str): The message to be included in the response (default: "An error occurred").

    Returns:
        Response: The custom error response object.
    """
    # Flatten serializer errors (list of error messages without field names)
    error_list = {}
    if isinstance(errors, dict):
        for field, field_errors in errors.items():
            if isinstance(field_errors, list):
                for error in field_errors:
                    if field == "non_field_errors":
                        error_list["error"] = error
                    else:
                        error = f"{error}"
                        error_list["error"] = error

    custom_response_data = {
        'success':False,
        'message': message,
        'errors': error_list if error_list else None
    }
    return Response(custom_response_data, status=status)


def response(data=None, message="Success", status_code=status.HTTP_200_OK):
    """
    Function to generate a data response.

    Args:
        data (dict): The data to be included in the response.
        status_code (int): The HTTP status code for the response (default: 200).
        message (str): The message to be included in the response (default: "Success").

    Returns:
        Response: The custom data response object.
    """
    custom_response_data = {
        'success':True,
        'message': message,
    }
    if data:
        custom_response_data['data'] = data
    return Response(custom_response_data, status=status_code)