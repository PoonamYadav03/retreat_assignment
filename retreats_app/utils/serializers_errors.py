def serializer_error(serializer_error):
    """
    Extract all error messages from a serializer error dictionary.
    """
    error_messages = []
    for error_text in serializer_error.keys():
        error_messages.extend(serializer_error.get(error_text))
    return error_messages

