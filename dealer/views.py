from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    HomePage view
    """
    template_name: str = "dealer/homepage.html"


class DealerView(TemplateView):
    """
    Create view Dealers
    """

    template_name: str = "dealer/create_dealer.html"


class DealerListView(TemplateView):
    """
    Show list Dealers
    """

    template_name: str = "dealer/list_dealers.html"


class OfficialView(TemplateView):
    """
    Create view Official
    """

    template_name: str = "dealer/create_official.html"


class OfficialsListView(TemplateView):
    """
    Show list Officials
    """

    template_name: str = "dealer/list_officials.html"


class HighDealersView(TemplateView):
    """
    High Dealer and assign to Official to Dealer
    """

    template_name: str = "dealer/high_dealer.html"


class HighDealerView(TemplateView):
    """
    Create assign of Official with Dealer
    """

    template_name: str = "dealer/create_high_dealer.html"
