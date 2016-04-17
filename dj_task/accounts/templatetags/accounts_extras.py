from django import template
from accounts.common.access import access
from accounts.common.bizzfuzz import bizzfuzz

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.tag(name="access")
def check_access(parser, token):
    try:
        tag_name, birthday = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )

    return CheckAccessNode(birthday)


class CheckAccessNode(template.Node):
    def __init__(self, birthday):
        self.birthday = template.Variable(birthday)

    def render(self, context):
        try:
            birthday = self.birthday.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        result = access(birthday)
        return result


@register.tag(name="bizzfuzz")
def check_bizzfuzz(parser, token):
    try:
        tag_name, number = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )

    return CheckBizzFuzzNode(number)


class CheckBizzFuzzNode(template.Node):
    def __init__(self, number):
        self.number = template.Variable(number)

    def render(self, context):
        try:
            number = self.number.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        result = bizzfuzz(number)
        return result
