from django.template import Library

register = Library()


@register.inclusion_tag("user_list_with_links.html")
def include_user_list_with_links(users):
    return dict(users=users)


@register.inclusion_tag("sortable_form_js.html")
def include_sortable_form_js():
    return dict()

@register.inclusion_tag("progress_bar.html")
def include_progress_bar(done, total, large=False):
    return dict(done=done, total=total, large=large)

@register.inclusion_tag("result_bar.html")
def include_result_bar(result, show_grades, questionnaire_warning=False):
    return dict(result=result, show_grades=show_grades, questionnaire_warning=questionnaire_warning)
