from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='Users:login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_client,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def artist_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='Users:login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_artist,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator