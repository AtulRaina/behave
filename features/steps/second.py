import behave
import importlib
importlib.__import__('helper')

@given(u'I have created a second file')
def step_impl(context):
    print(u'STEP: Given I have created a second file')