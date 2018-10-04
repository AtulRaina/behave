


def before_feature(context, feature):
    print('----------------------')
    print('Before feature called')


def after_feature(context, feature):
    print('----------------------')
    print('Before feature called')


def after_scenario(context,scenario):
    print('------------------')
    print('After scenario called')

def before_scenario(context,scenario):
    print('------------------')
    print('Before scenario called')