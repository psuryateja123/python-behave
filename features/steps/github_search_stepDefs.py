from behave import given, then

from pages.github_search_pageObjects import github_search_objects, github_search_pageObjects

author = 'surya pulakhandam'


@given(u'I navigate to github')
def step_impl(context):
    github_page = github_search_pageObjects(context.browser)
    github_page.navigate()

@then(u'I type python+behave')
def step_impl(context):
    github_page = github_search_pageObjects(context.browser)
    github_page.fill_text_search()

@then(u'I hit enter')
def step_impl(context):
    github_page = github_search_pageObjects(context.browser)
    github_page.hit_enter()


@then(u'I see the results')
def step_impl(context):
    github_page = github_search_pageObjects(context.browser)
    github_page.checking_for_repo()


@then(u'I select python+behave')
def step_impl(context):
    github_page = github_search_pageObjects(context.browser)
    github_page.selecting_the_repo()
