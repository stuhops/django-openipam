from django.urls import re_path

from openipam.api import views


# class OPENIPAMAPIRouter(SimpleRouter):
#     """
#     A router to match existing url patterns
#     """

#     # TODO: What do we do with these routes? Do we need to make their names singular as well?


#     routes = [
#         Route(
#             url="{prefix}/",
#             mapping={"get": "list"},
#             name="api_{basename}_list",
#             detail=False,
#             initkwargs={"suffix": "List"},
#         ),
#         Route(
#             url="{prefix}/add/",
#             mapping={"post": "create"},
#             name="api_{basename}_create",
#             detail=False,
#             initkwargs={"suffix": "Create"},
#         ),
#         Route(
#             url="{prefix}/{lookup}/",
#             mapping={"get": "retrieve"},
#             name="api_{basename}_detail",
#             detail=True,
#             initkwargs={"suffix": "Detail"},
#         ),
#         Route(
#             url="{prefix}/{lookup}/update/",
#             mapping={"get": "retrieve", "post": "update", "put": "update"},
#             name="api_{basename}_update",
#             detail=True,
#             initkwargs={"suffix": "Update"},
#         ),
#         Route(
#             url="{prefix}/{lookup}/delete/",
#             mapping={"get": "retrieve", "delete": "destroy", "post": "destroy"},
#             name="api_{basename}_delete",
#             detail=True,
#             initkwargs={"suffix": "Delete"},
#         ),
#     ]


# router = OPENIPAMAPIRouter()
# router.register(r"dhcpgroups?", views.network.DhcpGroupViewSet)
# router.register(r"dhcpoptions?", views.network.DhcpOptionViewSet)
# router.register(r"dhcpoptiontodhcpgroups?", views.network.DhcpOptionToDhcpGroupViewSet)
# router.register(r"sharednetworks?", views.network.SharedNetworkViewSet)
# router.register(r"networkranges?", views.network.NetworkRangeViewSet)
# router.register(r"networks?tovlans?", views.network.NetworkToVlanViewSet)
# router.register(r"pools?", views.network.PoolViewSet)
# router.register(r"defaultpools?", views.network.DefaultPoolViewSet)
# router.register(r"vlans?", views.network.VlanViewSet)
# router.register(r"buildings?", views.network.BuildingViewSet)
# router.register(r"buildings?tovlans?", views.network.BuildingToVlanViewSet)
# %s/(name=.*)(")

urlpatterns = [
    # path("", include(router.urls)),
    # Users
    re_path(r"^user/$", views.users.UserList.as_view(), name="api_users_list_singular"),
    # Groups
    re_path(
        r"^group/$", views.users.GroupList.as_view(), name="api_groups_list_singular"
    ),
    re_path(
        r"^group/options/$",
        views.users.GroupOptionsList.as_view(),
        name="api_groupsoptions_list_singular",
    ),
    # Attributes
    re_path(
        r"^attribute/$",
        views.hosts.AttributeList.as_view(),
        name="api_attributes_singular",
    ),
    re_path(
        r"^attribute/structured/values/$",
        views.hosts.StructuredAttributeValueList.as_view(),
        name="api_attributes_structured_values_singular",
    ),
    # Hosts
    re_path(
        r"^host/mac/next/$",
        views.hosts.HostNextMac.as_view(),
        name="api_host_mac_next_singular",
    ),
    re_path(
        r"^host/mac/$", views.hosts.HostMac.as_view(), name="api_host_mac_singular"
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/attributes/add/$",
        views.hosts.HostAddAttribute.as_view(),
        name="api_host_attribute_add_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/attributes/delete/$",
        views.hosts.HostDeleteAttribute.as_view(),
        name="api_host_attribute_delete_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/attributes/$",
        views.hosts.HostAttributeList.as_view(),
        name="api_host_attribute_list_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/owners/add/$",
        views.hosts.HostOwnerAdd.as_view(),
        name="api_host_owners_delete_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/owners/delete/$",
        views.hosts.HostOwnerDelete.as_view(),
        name="api_host_owners_add_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/owners/$",
        views.hosts.HostOwnerList.as_view(),
        name="api_host_owners_list_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/renew/$",
        views.hosts.HostRenew.as_view(),
        name="api_host_renew_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/update/$",
        views.hosts.HostUpdate.as_view(),
        name="api_host_update_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/delete/$",
        views.hosts.HostDelete.as_view(),
        name="api_host_delete_singular",
    ),
    re_path(
        r"^host/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/$",
        views.hosts.HostDetail.as_view(),
        name="api_host_view_singular",
    ),
    re_path(
        r"^host/add/$", views.hosts.HostCreate.as_view(), name="api_host_add_singular"
    ),
    re_path(
        r"^host/disabled/(?P<pk>([0-9a-fA-F]{2}[:-]?){5}[0-9a-fA-F]{2})/delete/$",
        views.hosts.DisabledHostDelete.as_view(),
        name="api_disabled_hosts_delete_singular",
    ),
    re_path(
        r"^host/disabled/add/$",
        views.hosts.DisabledHostCreate.as_view(),
        name="api_disabled_hosts_add_singular",
    ),
    re_path(
        r"^host/disabled/$",
        views.hosts.DisabledHostList.as_view(),
        name="api_disabled_hosts_list_singular",
    ),
    re_path(r"^host/$", views.hosts.HostList.as_view(), name="api_host_list_singular"),
    re_path(
        r"^guest/register/$",
        views.guests.GuestRegister.as_view(),
        name="api_guest_register_singular",
    ),
    re_path(
        r"^guest/tickets/add/$",
        views.guests.GuestTicketCreate.as_view(),
        name="api_guest_create_singular",
    ),
    re_path(
        r"^guest/tickets/$",
        views.guests.GuestTicketList.as_view(),
        name="api_guest_list_singular",
    ),
    re_path(
        r"^guest/tickets/(?P<ticket>\w+)/$",
        views.guests.GuestTicketDelete.as_view(),
        name="api_guest_delete_singular",
    ),
    re_path(
        r"^domain/$", views.dns.DomainList.as_view(), name="api_domain_list_singular"
    ),
    re_path(
        r"^domain/name/$",
        views.dns.DomainNameList.as_view(),
        name="api_domain_name_list_singular",
    ),
    re_path(
        r"^network/$",
        views.network.NetworkList.as_view(),
        name="api_network_list_singular",
    ),
    re_path(
        r"^network/(?P<pk>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}\/\d{0,2}))/$",
        views.network.NetworkDetail.as_view(),
        name="api_network_detail_singular",
    ),
    re_path(
        r"^network/add/$",
        views.network.NetworkCreate.as_view(),
        name="api_network_create_singular",
    ),
    re_path(
        r"^network/(?P<pk>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}\/\d{0,3}))/update/$",
        views.network.NetworkUpdate.as_view(),
        name="api_network_update_singular",
    ),
    re_path(
        r"^network/(?P<pk>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}\/\d{0,3}))/delete/$",
        views.network.NetworkDelete.as_view(),
        name="api_network_delete_singular",
    ),
    re_path(
        r"^address/(?P<pk>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}))/$",
        views.network.AddressDetail.as_view(),
        name="api_address_view_singular",
    ),
    re_path(
        r"^address/(?P<pk>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}))/update/$",
        views.network.AddressUpdate.as_view(),
        name="api_address_update_singular",
    ),
    re_path(
        r"^address/$",
        views.network.AddressList.as_view(),
        name="api_address_list_singular",
    ),
]
