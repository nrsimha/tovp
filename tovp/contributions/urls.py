# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from . import views


follow_up = [
    url(
        regex=r'^(?P<pledge_id>\d+)/(?P<pk>\d+)/$',
        view=views.FollowUpDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<pledge_id>\d+)/create/$',
        view=views.FollowUpCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<pledge_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.FollowUpUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.FollowUpDeleteView.as_view(),
        name="delete",
    ),
]

pledges = [
    url(
        regex=r'^$',
        view=views.PledgeListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.PledgeDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.PledgeCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.PledgeUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.PledgeDeleteView.as_view(),
        name="delete",
    ),
    url(
        regex=r'^assign-to-follow/(?P<pk>\d+)/$',
        view=views.PledgeAssignToFollow.as_view(),
        name="assign_to_follow",
    ),
]

contributions = [
    url(
        regex=r'^$',
        view=views.ContributionListView.as_view(),
        name='index'
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.ContributionDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.ContributionCreateView.as_view(),
        name='create',
    ),
    # create new contribution with auto filled pledge
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pledge_id>\d+)/create/$',
        view=views.ContributionCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit/$',
        view=views.ContributionUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/confirm-move/$',
        view=views.ContributionConfirmMoveView.as_view(),
        name='confirm_move',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/move/$',
        view=views.ContributionMoveView.as_view(),
        name='move',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/move/$',
        view=views.ContributionUpdateView.as_view(),
        name='move',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/donor$',
        view=views.ContributionDonorLetterDetailView.as_view(),
        name='donor_letter',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/receipt$',
        view=views.DonorInvoiceDetailView.as_view(),
        name='donor_receipt',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/receipt-digital-signature$',
        view=views.DonorInvoiceDetailView.as_view(print_signature=True),
        name='donor_receipt_with_signature',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.ContributionDeleteView.as_view(),
        name="delete",
    ),
    url(
        regex=r'^status_changer/(?P<pk>\d+)/$',
        view=views.ContributionDepositStatusChangeView.as_view(),
        name="deposit_status_changer",
    ),
]

bulk_payments = [
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/$',
        view=views.BulkPaymentDetailView.as_view(),
        name='detail',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/create/$',
        view=views.BulkPaymentCreateView.as_view(),
        name='create',
    ),
    url(
        regex=r'^(?P<person_id>\d+)/(?P<pk>\d+)/edit$',
        view=views.BulkPaymentUpdateView.as_view(),
        name='update',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/donor$',
        view=views.BulkPaymentDonorLetterDetailView.as_view(),
        name='donor_letter',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/receipt/(?P<signature>0|1)/$',
        view=views.BulkPaymentReceiptDetailView.as_view(),
        name='print_receipt',
    ),
    url(
        regex=r'^print/(?P<pk>\d+)/acknowledgement/(?P<signature>0|1)/$',
        view=views.BulkPaymentReceiptDetailView.as_view(
            template_name='contributions/print_acknowledgement.html',
        ),
        name='print_acknowledgement',
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=views.BulkPaymentDeleteView.as_view(),
        name="delete",
    ),
    url(
        regex=r'^ajax/$',
        view=views.bulk_payment_ajax_search,
        name='ajax'
    ),
]


urlpatterns = [
    url(r'^pledge/', include(pledges, namespace="pledge")),
    url(r'^follow-up/', include(follow_up, namespace="follow_up")),
    url(r'^contribution/', include(contributions, namespace="contribution")),
    url(r'^bulk_payment/', include(bulk_payments, namespace="bulk_payment")),
]
