from django.core.paginator import Paginator, Page


def get_paginated_response(data, count:int=5, page:int=1) -> Page:
    """
    Function returns the paginated object for the data

    Args:
        data (list): The list of data to paginate.
        count (int, optional): The number of items per page. Defaults to 10.
        page (int, optional): The page number to return. Defaults to 1.
        
    Returns:
        Page: The paginated object for the requested page.

    """
    paginator = Paginator(data, count)
    page_obj = paginator.get_page(page)

    return page_obj