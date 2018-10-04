import behave

pm = __import__('sampletoload')

@given(u'I have started using Behave')
def step_impl(context):
    print(u'STEP: Given I have started using Behave')
    assert pm.test_load_function() > 1


@when(u'I create a feature file')
def step_impl(context):
    print(u'STEP: When I create a feature file')



@then(u'I should be able to run the created file')
def step_impl(context):
    print(u'STEP: Then I should be able to run the created file')
    pm.test_second_function()