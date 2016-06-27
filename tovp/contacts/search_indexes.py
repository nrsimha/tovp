from haystack import indexes

from ananta.search_indexes import ContentSearchIndexMixin

from .models import Person


class PersonIndex(ContentSearchIndexMixin, indexes.SearchIndex,
                  indexes.Indexable):
    content_name = 'Contact'
    text = indexes.CharField(document=True, use_template=True)
    mixed_name = indexes.CharField()
    full_name = indexes.CharField(model_attr='full_name')
    initiated_name = indexes.CharField(model_attr='initiated_name')
    first_name = indexes.CharField(model_attr='first_name')
    middle_name = indexes.CharField(model_attr='last_name')
    last_name = indexes.CharField(model_attr='last_name')
    email = indexes.CharField(model_attr='email')
    phone_number = indexes.CharField(model_attr='phone_number')
    yatra = indexes.CharField(faceted=True)
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')
    state = indexes.CharField(model_attr='state')
    old_database_id = indexes.CharField(model_attr='old_database_id', null=True)
    country = indexes.CharField(model_attr='get_country_display', faceted=True)
    postcode = indexes.CharField(model_attr='postcode')
    pan_card_number = indexes.CharField(model_attr='pan_card_number', null=True)
    note = indexes.CharField(model_attr='note')
    gifts = indexes.MultiValueField(null=True, faceted=True)
    promotion_type = indexes.MultiValueField(null=True, faceted=True)

    balance_total_usd = indexes.IntegerField()
    balance_year_usd = indexes.IntegerField()
    balance_financial_year_usd = indexes.IntegerField()

    balance_total_usd = indexes.IntegerField()
    balance_year_usd = indexes.IntegerField()
    balance_financial_year_usd = indexes.IntegerField()

    balance_total_inr = indexes.IntegerField()
    balance_year_inr = indexes.IntegerField()
    balance_financial_year_inr = indexes.IntegerField()

    sources = indexes.CharField(null=True)
    promotions = indexes.CharField(null=True)

    def prepare_gifts(self, obj):
        items = []
        if obj.gifts.count():
            for gift_given in obj.gifts.all():
                items.append(gift_given.gift.name)
        return items

    def prepare_promotion_type(self, obj):
        items = []
        for promotion in obj.assigned_promotions():
            try:
                items.append(promotion._meta.verbose_name.title())
            except:
                items.append('Noname')
        return items

    def prepare_mixed_name(self, obj):
        return obj.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.yatra:
            return obj.get_yatra_display()
        else:
            return 'None'

    def prepare_sources(self, obj):
        items = []
        for pledge in obj.pledges.all():
            if (pledge.get_source_display()) and (pledge.get_source_display() not in items):
                items.append(pledge.get_source_display())
            for contribution in pledge.contributions.all():
                if (contribution.get_source_display()) and (contribution.get_source_display() not in items):
                    items.append(pledge.get_source_display())
        return ",".join(items)

    def prepare_promotions(self, obj):
        promotions = []
        for promotion in obj.assigned_promotions():
            try:
                promotions.append(promotion._meta.verbose_name.title())
            except:
                promotions.append('*Noname*')
        return ",".join(promotions)

    def prepare_balance_total_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['paid']

    def prepare_balance_total_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['paid']

    def prepare_balance_year_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['donated_year']

    def prepare_balance_year_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['donated_year']

    def prepare_balance_financial_year_usd(self, obj):
        balance = obj.get_ballance()
        return balance['USD']['donated_financial_year']

    def prepare_balance_financial_year_inr(self, obj):
        balance = obj.get_ballance()
        return balance['INR']['donated_financial_year']

    def get_model(self):
        return Person

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


class PersonSearchIndexMixin(indexes.SearchIndex):
    full_name = indexes.CharField(model_attr='person__full_name')
    mixed_name = indexes.CharField()
    initiated_name = indexes.CharField(model_attr='person__initiated_name')
    first_name = indexes.CharField(model_attr='person__first_name')
    middle_name = indexes.CharField(model_attr='person__last_name')
    last_name = indexes.CharField(model_attr='person__last_name')
    email = indexes.CharField(model_attr='person__email')
    phone_number = indexes.CharField(model_attr='person__phone_number')
    yatra = indexes.CharField(model_attr='person__get_yatra_display',
                              faceted=True)
    address = indexes.CharField(model_attr='person__address')
    city = indexes.CharField(model_attr='person__city')
    state = indexes.CharField(model_attr='person__state')
    country = indexes.CharField(model_attr='person__get_country_display', faceted=True)
    postcode = indexes.CharField(model_attr='person__postcode')
    pan_card_number = indexes.CharField(model_attr='person__pan_card_number')

    def prepare_mixed_name(self, obj):
        return obj.person.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.person.yatra:
            return obj.person.get_yatra_display()
        else:
            return 'None'


class PledgePersonSearchIndexMixin(indexes.SearchIndex):
    full_name = indexes.CharField(model_attr='pledge__person__full_name')
    mixed_name = indexes.CharField()
    initiated_name = indexes.CharField(model_attr='pledge__person__initiated_name')
    first_name = indexes.CharField(model_attr='pledge__person__first_name')
    middle_name = indexes.CharField(model_attr='pledge__person__last_name')
    last_name = indexes.CharField(model_attr='pledge__person__last_name')
    email = indexes.CharField(model_attr='pledge__person__email')
    phone_number = indexes.CharField(model_attr='pledge__person__phone_number')
    yatra = indexes.CharField(model_attr='pledge__person__get_yatra_display',
                              faceted=True)
    address = indexes.CharField(model_attr='pledge__person__address')
    city = indexes.CharField(model_attr='pledge__person__city')
    state = indexes.CharField(model_attr='pledge__person__state')
    country = indexes.CharField(model_attr='pledge__person__get_country_display', faceted=True)
    postcode = indexes.CharField(model_attr='pledge__person__postcode')
    pan_card_number = indexes.CharField(model_attr='pledge__person__pan_card_number')

    def prepare_mixed_name(self, obj):
        return obj.pledge.person.join_fields(
            ('initiated_name', 'first_name', 'middle_name', 'last_name'),
            separator=" ").replace('.', '. ').replace('-', ' ')

    def prepare_yatra(self, obj):
        if obj.pledge.person.yatra:
            return obj.pledge.person.get_yatra_display()
        else:
            return 'None'
