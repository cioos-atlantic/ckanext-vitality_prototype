DATASET_FIELDS = [
        "author",
        "author_email",
        "bbox-east-long",
        "bbox-north-lat",
        "bbox-south-lat",
        "bbox-west-long",
        "cited-responsible-party",
        "creator_user_id",
        "dataset-reference-date",
        "eov",
        "extras",
        "frequency-of-update",
        "groups",
        "id",
        "isopen",
        "keywords/en",
        "keywords/fr",
        "license_id",
        "license_title",
        "license_url",
        "maintainer",
        "maintainer_email",
        "metadata_created",
        "metadata_modified",
        "metadata-language",
        "metadata-point-of-contact",
        # "metadata-point-of-contact/contact-info_email",
        # "metadata-point-of-contact/contact-info_online-resource_application-profile",
        # "metadata-point-of-contact/contact-info_online-resource_description",
        # "metadata-point-of-contact/contact-info_online-resource_function",
        # "metadata-point-of-contact/contact-info_online-resource_name",
        # "metadata-point-of-contact/contact-info_online-resource_protocol",
        # "metadata-point-of-contact/contact-info_online-resource_protocol-request",
        # "metadata-point-of-contact/contact-info_online-resource_url",
        # "metadata-point-of-contact/individual-name",
        # "metadata-point-of-contact/organisation-name",
        # "metadata-point-of-contact/position-name",
        # "metadata-point-of-contact/role",
        "metadata-reference-date",
        "name",
        "notes/en",
        "notes/fr",
        "notes_translated/en",
        "notes_translated/fr",
        "num_resources",
        "num_tags",
        "organization/approval_status",
        "organization/created",
        "organization/description",
        "organization/description_translated/en",
        "organization/description_translated/fr",
        "organization/id",
        "organization/image_url",
        "organization/image_url_translated/en",
        "organization/image_url_translated/fr",
        "organization/is_organization",
        "organization/revision_id",
        "organization/state",
        "organization/title",
        "organization/title_translated/en",
        "organization/title_translated/fr",
        "organization/type",
        "owner_org",
        "private",
        "progress",
        "relationships_as_object",
        "relationships_as_subject",
        "resources",
        "resource-type",
        "revision_id",
        "spatial/coordinates",
        "spatial/type",
        "state",
        "tags",
        "temporal-extent/begin",
        "temporal-extent/end",
        "title",
        "title_translated/en",
        "title_translated/fr",
        "tracking_summary/recent",
        "tracking_summary/total",
        "type",
        "unique-resource-identifier-full/authority",
        "unique-resource-identifier-full/code",
        "unique-resource-identifier-full/code-space",
        "unique-resource-identifier-full/version",
        "url",
        "vertical-extent",
        "xml_location_url",
        "organization/name"
    ]

PUBLIC_FIELDS = [
    "id",
    "resources",
    "type",
    "name",
    "state",
    "organization/approval_status",
    "orgnaization/created",
    "organization/description",
    "organization/description_translated/en",
    "organization/description_translated/fr",
    "organization/id",
    "organization/image_url",
    "organization/image_url_translated/en",
    "organization/image_url_translated/fr",
    "organization/is_organization",
    "organization/revision_id",
    "organization/state",
    "organization/title",
    "organization/title_translated/en",
    "organization/title_translated/fr",
    "organization/type",
    "organization/name",
    "title_translated/en",
    "title_translated/fr",
    "cited-responsible-party",
    "eov",
    "frequency-of-update",
    "keywords/en",
    "keywords/fr",
    "metadata-point-of-contact",
    "notes_translated/en",
    "notes_translated/fr",
    "progress",
    "resource_type",
    "xml_location_url",
    "dataset-reference-date",
    "metadata-reference-date" 
]

# Template / harvest issues will occur if these fields don't exist
MINIMUM_FIELDS = [
    # Template issues
    "id",
#    "resources",
    "type",
    "name",
    "state",
    "organization/id",
    "organization/state",
    "organization/type",
    "organization/name",
    "dataset-reference-date",
    "metadata-reference-date",
    # Harvest issues
    "cited-responsible-party",
    "eov",
    "frequency-of-update",
    "keywords/en",
    "keywords/fr",
    "metadata-point-of-contact",
    "notes_translated/en",
    "notes_translated/fr",
    "progress",
    "resource_type",
    "xml_location_url"

]

STRINGIFIED_FIELDS = [
    "metadata-point-of-contact",
    "spatial",
    "temporal-extent",
    "unique-resource-identifier-full",
    "notes",
    "cited-responsible-party",
    "dataset-reference-date"
]