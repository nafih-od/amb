def generate_form_errors(args, formset=False):
    """

    :param args:
    :param formset:
    :return:
    """
    message = ''
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors + "|"
        for err in args.non_field_errors():
            message += str(err) + "|"

    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message += field.errors + "|"
            for err in form.non_field_errors():
                message += str(err) + "|"
    # return message[:-1]
    return message