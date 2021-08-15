from rest_framework import serializers


def contain_numbers(string):
    if any(map(str.isdigit, string)):
        raise serializers.ValidationError('The field \'Name\' must not contain numbers!')