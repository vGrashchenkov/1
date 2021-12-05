from selenium.webdriver.common.by import By


class Catalog:

    def __init__(self, catalog_path):
        self.PATH = catalog_path

    ITEMS = {'by': By.CSS_SELECTOR, 'value': '#content > div:nth-of-type(4)'}
    LEFT_MEU = {'by': By.CSS_SELECTOR, 'value': '.list-group'}
    BREADCRUMB = {'by': By.CSS_SELECTOR, 'value': '.breadcrumb'}
    DESKTOPS_DESCR = {'by': By.CSS_SELECTOR, 'value': '#content > div:nth-of-type(1)'}
    REFINE_SEARCH = {'by': By.CSS_SELECTOR, 'value': '#content ul'}
    LIST_VIEW_BUTTON = {'by': By.ID, 'value': 'list-view'}
    GRID_VIEW_BUTTON = {'by': By.ID, 'value': 'grid-view'}

