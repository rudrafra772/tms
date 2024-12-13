from typing import List, Union, Dict, Any
from django.db.models import QuerySet, Q
from django.db import models

def search(query: Union[str, bool, int, None], data: QuerySet, search_fields: List[Union[str, Dict[str, Any]]]) -> QuerySet:
    """
    Function to search data from the provided queryset.

    Args:
        query (Union[str, bool, int, None]): The search query from the user input.
        data (QuerySet): The initial queryset of data to search within.
        search_fields (List[Union[str, Dict[str, Any]]]): A list of fields to search against, dynamically injected.
            - Can be simple field names (str) for text search.
            - Can be key-value pairs (Dict[str, Any]) for exact match.

    Returns:
        QuerySet: The filtered queryset with results matching the search query or exact match criteria.
    """
    
    if not query and not search_fields:
        return data

    q_objects = Q()

    for field in search_fields:
        # Check if the field is a dictionary for exact matches
        if isinstance(field, dict):
            for key, value in field.items():
                # Perform an exact match for the field-value pair
                q_objects |= Q(**{f"{key}__exact": value})

        # Handle simple field lookups for text search
        elif isinstance(field, str) and query:
            try:
                field_type = data.model._meta.get_field(field)
                
                # Handle different field types (Text, Integer, Boolean, etc.)
                if field_type.get_internal_type() in ['CharField', 'TextField']:
                    q_objects |= Q(**{f"{field}__icontains": query})
                elif field_type.get_internal_type() == 'BooleanField' and isinstance(query, bool):
                    q_objects |= Q(**{f"{field}__exact": query})
                elif field_type.get_internal_type() in ['IntegerField', 'BigIntegerField'] and isinstance(query, int):
                    q_objects |= Q(**{f"{field}__exact": query})
                # You can add more types like DateField, DecimalField, etc.

            except data.DoesNotExist:
                # If the field doesn't exist in the model, skip it
                continue

    # Filter the queryset if there are any valid search conditions
    if q_objects:
        return data.filter(q_objects)
    
    # Return the original data if no valid search conditions were applied
    return data

def filter_by_staff(data:QuerySet) -> QuerySet:
    """
    Function to filter data by the staff user only.

    Args:
        data (QuerySet): The initial queryset of data.
    
    Returns:
        QuerySet: The filtered queryset with results matching the query or exact match criteria.
    """
    return data.filter(is_staff = True, is_superuser = False)

def filter_by_superuser(data:QuerySet) -> QuerySet:
    """
    Function to filter data by the super user only.

    Args:
        data (QuerySet): The initial queryset of data.
    
    Returns:
        QuerySet: The filtered queryset with results matching the query or exact match criteria.
    """
    return data.filter(is_superuser = True)

def filter_by_user(data:QuerySet) -> QuerySet:
    """
    Function to filter data by the user only.

    Args:
        data (QuerySet): The initial queryset of data.
    
    Returns:
        QuerySet: The filtered queryset with results matching the query or exact match criteria.
    """
    return data.filter(is_superuser = False, is_staff = False, is_active = True)

def sort_data(data: QuerySet, sort_fields: List[Union[str, dict]]) -> QuerySet:
    """
    Function to sort data from the provided queryset.

    Args:
        data (QuerySet): The initial queryset of data to sort.
        sort_fields (List[Union[str, dict]]): A list of fields to sort by.
            - Can be simple field names (str) for ascending order.
            - Can be a dictionary with field name and order, e.g., {'field': 'asc'} or {'field': 'desc'}.

    Returns:
        QuerySet: The sorted queryset.
    """
    if not sort_fields:
        return data

    ordering = []

    for field in sort_fields:
        if isinstance(field, str):
            ordering.append(field)  # Ascending order by default
        elif isinstance(field, dict):
            for key, order in field.items():
                if order.lower() == 'desc':
                    ordering.append(f'-{key}')
                else:
                    ordering.append(key)

    return data.order_by(*ordering)