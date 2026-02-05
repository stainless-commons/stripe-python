# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.address import Address

__all__ = [
    "IssuingCard",
    "SpendingControls",
    "SpendingControlsSpendingLimit",
    "LatestFraudWarning",
    "PersonalizationDesign",
    "PersonalizationDesignIssuingPersonalizationDesign",
    "PersonalizationDesignIssuingPersonalizationDesignPhysicalBundle",
    "PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundle",
    "PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundleFeatures",
    "PersonalizationDesignIssuingPersonalizationDesignPreferences",
    "PersonalizationDesignIssuingPersonalizationDesignRejectionReasons",
    "PersonalizationDesignIssuingPersonalizationDesignCardLogo",
    "PersonalizationDesignIssuingPersonalizationDesignCarrierText",
    "ReplacedBy",
    "ReplacementFor",
    "Shipping",
    "ShippingAddressValidation",
    "ShippingCustoms",
    "Wallets",
    "WalletsApplePay",
    "WalletsGooglePay",
]


class SpendingControlsSpendingLimit(BaseModel):
    amount: int
    """Maximum amount allowed to spend per interval.

    This amount is in the card's currency and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    interval: Literal["all_time", "daily", "monthly", "per_authorization", "weekly", "yearly"]
    """Interval (or event) to which the amount applies."""

    categories: Optional[
        List[
            Literal[
                "ac_refrigeration_repair",
                "accounting_bookkeeping_services",
                "advertising_services",
                "agricultural_cooperative",
                "airlines_air_carriers",
                "airports_flying_fields",
                "ambulance_services",
                "amusement_parks_carnivals",
                "antique_reproductions",
                "antique_shops",
                "aquariums",
                "architectural_surveying_services",
                "art_dealers_and_galleries",
                "artists_supply_and_craft_shops",
                "auto_and_home_supply_stores",
                "auto_body_repair_shops",
                "auto_paint_shops",
                "auto_service_shops",
                "automated_cash_disburse",
                "automated_fuel_dispensers",
                "automobile_associations",
                "automotive_parts_and_accessories_stores",
                "automotive_tire_stores",
                "bail_and_bond_payments",
                "bakeries",
                "bands_orchestras",
                "barber_and_beauty_shops",
                "betting_casino_gambling",
                "bicycle_shops",
                "billiard_pool_establishments",
                "boat_dealers",
                "boat_rentals_and_leases",
                "book_stores",
                "books_periodicals_and_newspapers",
                "bowling_alleys",
                "bus_lines",
                "business_secretarial_schools",
                "buying_shopping_services",
                "cable_satellite_and_other_pay_television_and_radio",
                "camera_and_photographic_supply_stores",
                "candy_nut_and_confectionery_stores",
                "car_and_truck_dealers_new_used",
                "car_and_truck_dealers_used_only",
                "car_rental_agencies",
                "car_washes",
                "carpentry_services",
                "carpet_upholstery_cleaning",
                "caterers",
                "charitable_and_social_service_organizations_fundraising",
                "chemicals_and_allied_products",
                "child_care_services",
                "childrens_and_infants_wear_stores",
                "chiropodists_podiatrists",
                "chiropractors",
                "cigar_stores_and_stands",
                "civic_social_fraternal_associations",
                "cleaning_and_maintenance",
                "clothing_rental",
                "colleges_universities",
                "commercial_equipment",
                "commercial_footwear",
                "commercial_photography_art_and_graphics",
                "commuter_transport_and_ferries",
                "computer_network_services",
                "computer_programming",
                "computer_repair",
                "computer_software_stores",
                "computers_peripherals_and_software",
                "concrete_work_services",
                "construction_materials",
                "consulting_public_relations",
                "correspondence_schools",
                "cosmetic_stores",
                "counseling_services",
                "country_clubs",
                "courier_services",
                "court_costs",
                "credit_reporting_agencies",
                "cruise_lines",
                "dairy_products_stores",
                "dance_hall_studios_schools",
                "dating_escort_services",
                "dentists_orthodontists",
                "department_stores",
                "detective_agencies",
                "digital_goods_applications",
                "digital_goods_games",
                "digital_goods_large_volume",
                "digital_goods_media",
                "direct_marketing_catalog_merchant",
                "direct_marketing_combination_catalog_and_retail_merchant",
                "direct_marketing_inbound_telemarketing",
                "direct_marketing_insurance_services",
                "direct_marketing_other",
                "direct_marketing_outbound_telemarketing",
                "direct_marketing_subscription",
                "direct_marketing_travel",
                "discount_stores",
                "doctors",
                "door_to_door_sales",
                "drapery_window_covering_and_upholstery_stores",
                "drinking_places",
                "drug_stores_and_pharmacies",
                "drugs_drug_proprietaries_and_druggist_sundries",
                "dry_cleaners",
                "durable_goods",
                "duty_free_stores",
                "eating_places_restaurants",
                "educational_services",
                "electric_razor_stores",
                "electric_vehicle_charging",
                "electrical_parts_and_equipment",
                "electrical_services",
                "electronics_repair_shops",
                "electronics_stores",
                "elementary_secondary_schools",
                "emergency_services_gcas_visa_use_only",
                "employment_temp_agencies",
                "equipment_rental",
                "exterminating_services",
                "family_clothing_stores",
                "fast_food_restaurants",
                "financial_institutions",
                "fines_government_administrative_entities",
                "fireplace_fireplace_screens_and_accessories_stores",
                "floor_covering_stores",
                "florists",
                "florists_supplies_nursery_stock_and_flowers",
                "freezer_and_locker_meat_provisioners",
                "fuel_dealers_non_automotive",
                "funeral_services_crematories",
                "furniture_home_furnishings_and_equipment_stores_except_appliances",
                "furniture_repair_refinishing",
                "furriers_and_fur_shops",
                "general_services",
                "gift_card_novelty_and_souvenir_shops",
                "glass_paint_and_wallpaper_stores",
                "glassware_crystal_stores",
                "golf_courses_public",
                "government_licensed_horse_dog_racing_us_region_only",
                "government_licensed_online_casions_online_gambling_us_region_only",
                "government_owned_lotteries_non_us_region",
                "government_owned_lotteries_us_region_only",
                "government_services",
                "grocery_stores_supermarkets",
                "hardware_equipment_and_supplies",
                "hardware_stores",
                "health_and_beauty_spas",
                "hearing_aids_sales_and_supplies",
                "heating_plumbing_a_c",
                "hobby_toy_and_game_shops",
                "home_supply_warehouse_stores",
                "hospitals",
                "hotels_motels_and_resorts",
                "household_appliance_stores",
                "industrial_supplies",
                "information_retrieval_services",
                "insurance_default",
                "insurance_underwriting_premiums",
                "intra_company_purchases",
                "jewelry_stores_watches_clocks_and_silverware_stores",
                "landscaping_services",
                "laundries",
                "laundry_cleaning_services",
                "legal_services_attorneys",
                "luggage_and_leather_goods_stores",
                "lumber_building_materials_stores",
                "manual_cash_disburse",
                "marinas_service_and_supplies",
                "marketplaces",
                "masonry_stonework_and_plaster",
                "massage_parlors",
                "medical_and_dental_labs",
                "medical_dental_ophthalmic_and_hospital_equipment_and_supplies",
                "medical_services",
                "membership_organizations",
                "mens_and_boys_clothing_and_accessories_stores",
                "mens_womens_clothing_stores",
                "metal_service_centers",
                "miscellaneous",
                "miscellaneous_apparel_and_accessory_shops",
                "miscellaneous_auto_dealers",
                "miscellaneous_business_services",
                "miscellaneous_food_stores",
                "miscellaneous_general_merchandise",
                "miscellaneous_general_services",
                "miscellaneous_home_furnishing_specialty_stores",
                "miscellaneous_publishing_and_printing",
                "miscellaneous_recreation_services",
                "miscellaneous_repair_shops",
                "miscellaneous_specialty_retail",
                "mobile_home_dealers",
                "motion_picture_theaters",
                "motor_freight_carriers_and_trucking",
                "motor_homes_dealers",
                "motor_vehicle_supplies_and_new_parts",
                "motorcycle_shops_and_dealers",
                "motorcycle_shops_dealers",
                "music_stores_musical_instruments_pianos_and_sheet_music",
                "news_dealers_and_newsstands",
                "non_fi_money_orders",
                "non_fi_stored_value_card_purchase_load",
                "nondurable_goods",
                "nurseries_lawn_and_garden_supply_stores",
                "nursing_personal_care",
                "office_and_commercial_furniture",
                "opticians_eyeglasses",
                "optometrists_ophthalmologist",
                "orthopedic_goods_prosthetic_devices",
                "osteopaths",
                "package_stores_beer_wine_and_liquor",
                "paints_varnishes_and_supplies",
                "parking_lots_garages",
                "passenger_railways",
                "pawn_shops",
                "pet_shops_pet_food_and_supplies",
                "petroleum_and_petroleum_products",
                "photo_developing",
                "photographic_photocopy_microfilm_equipment_and_supplies",
                "photographic_studios",
                "picture_video_production",
                "piece_goods_notions_and_other_dry_goods",
                "plumbing_heating_equipment_and_supplies",
                "political_organizations",
                "postal_services_government_only",
                "precious_stones_and_metals_watches_and_jewelry",
                "professional_services",
                "public_warehousing_and_storage",
                "quick_copy_repro_and_blueprint",
                "railroads",
                "real_estate_agents_and_managers_rentals",
                "record_stores",
                "recreational_vehicle_rentals",
                "religious_goods_stores",
                "religious_organizations",
                "roofing_siding_sheet_metal",
                "secretarial_support_services",
                "security_brokers_dealers",
                "service_stations",
                "sewing_needlework_fabric_and_piece_goods_stores",
                "shoe_repair_hat_cleaning",
                "shoe_stores",
                "small_appliance_repair",
                "snowmobile_dealers",
                "special_trade_services",
                "specialty_cleaning",
                "sporting_goods_stores",
                "sporting_recreation_camps",
                "sports_and_riding_apparel_stores",
                "sports_clubs_fields",
                "stamp_and_coin_stores",
                "stationary_office_supplies_printing_and_writing_paper",
                "stationery_stores_office_and_school_supply_stores",
                "swimming_pools_sales",
                "t_ui_travel_germany",
                "tailors_alterations",
                "tax_payments_government_agencies",
                "tax_preparation_services",
                "taxicabs_limousines",
                "telecommunication_equipment_and_telephone_sales",
                "telecommunication_services",
                "telegraph_services",
                "tent_and_awning_shops",
                "testing_laboratories",
                "theatrical_ticket_agencies",
                "timeshares",
                "tire_retreading_and_repair",
                "tolls_bridge_fees",
                "tourist_attractions_and_exhibits",
                "towing_services",
                "trailer_parks_campgrounds",
                "transportation_services",
                "travel_agencies_tour_operators",
                "truck_stop_iteration",
                "truck_utility_trailer_rentals",
                "typesetting_plate_making_and_related_services",
                "typewriter_stores",
                "u_s_federal_government_agencies_or_departments",
                "uniforms_commercial_clothing",
                "used_merchandise_and_secondhand_stores",
                "utilities",
                "variety_stores",
                "veterinary_services",
                "video_amusement_game_supplies",
                "video_game_arcades",
                "video_tape_rental_stores",
                "vocational_trade_schools",
                "watch_jewelry_repair",
                "welding_repair",
                "wholesale_clubs",
                "wig_and_toupee_stores",
                "wires_money_orders",
                "womens_accessory_and_specialty_shops",
                "womens_ready_to_wear_stores",
                "wrecking_and_salvage_yards",
            ]
        ]
    ] = None
    """
    Array of strings containing
    [categories](https://docs.stripe.com/api#issuing_authorization_object-merchant_data-category)
    this limit applies to. Omitting this field will apply the limit to all
    categories.
    """


class SpendingControls(BaseModel):
    allowed_categories: Optional[
        List[
            Literal[
                "ac_refrigeration_repair",
                "accounting_bookkeeping_services",
                "advertising_services",
                "agricultural_cooperative",
                "airlines_air_carriers",
                "airports_flying_fields",
                "ambulance_services",
                "amusement_parks_carnivals",
                "antique_reproductions",
                "antique_shops",
                "aquariums",
                "architectural_surveying_services",
                "art_dealers_and_galleries",
                "artists_supply_and_craft_shops",
                "auto_and_home_supply_stores",
                "auto_body_repair_shops",
                "auto_paint_shops",
                "auto_service_shops",
                "automated_cash_disburse",
                "automated_fuel_dispensers",
                "automobile_associations",
                "automotive_parts_and_accessories_stores",
                "automotive_tire_stores",
                "bail_and_bond_payments",
                "bakeries",
                "bands_orchestras",
                "barber_and_beauty_shops",
                "betting_casino_gambling",
                "bicycle_shops",
                "billiard_pool_establishments",
                "boat_dealers",
                "boat_rentals_and_leases",
                "book_stores",
                "books_periodicals_and_newspapers",
                "bowling_alleys",
                "bus_lines",
                "business_secretarial_schools",
                "buying_shopping_services",
                "cable_satellite_and_other_pay_television_and_radio",
                "camera_and_photographic_supply_stores",
                "candy_nut_and_confectionery_stores",
                "car_and_truck_dealers_new_used",
                "car_and_truck_dealers_used_only",
                "car_rental_agencies",
                "car_washes",
                "carpentry_services",
                "carpet_upholstery_cleaning",
                "caterers",
                "charitable_and_social_service_organizations_fundraising",
                "chemicals_and_allied_products",
                "child_care_services",
                "childrens_and_infants_wear_stores",
                "chiropodists_podiatrists",
                "chiropractors",
                "cigar_stores_and_stands",
                "civic_social_fraternal_associations",
                "cleaning_and_maintenance",
                "clothing_rental",
                "colleges_universities",
                "commercial_equipment",
                "commercial_footwear",
                "commercial_photography_art_and_graphics",
                "commuter_transport_and_ferries",
                "computer_network_services",
                "computer_programming",
                "computer_repair",
                "computer_software_stores",
                "computers_peripherals_and_software",
                "concrete_work_services",
                "construction_materials",
                "consulting_public_relations",
                "correspondence_schools",
                "cosmetic_stores",
                "counseling_services",
                "country_clubs",
                "courier_services",
                "court_costs",
                "credit_reporting_agencies",
                "cruise_lines",
                "dairy_products_stores",
                "dance_hall_studios_schools",
                "dating_escort_services",
                "dentists_orthodontists",
                "department_stores",
                "detective_agencies",
                "digital_goods_applications",
                "digital_goods_games",
                "digital_goods_large_volume",
                "digital_goods_media",
                "direct_marketing_catalog_merchant",
                "direct_marketing_combination_catalog_and_retail_merchant",
                "direct_marketing_inbound_telemarketing",
                "direct_marketing_insurance_services",
                "direct_marketing_other",
                "direct_marketing_outbound_telemarketing",
                "direct_marketing_subscription",
                "direct_marketing_travel",
                "discount_stores",
                "doctors",
                "door_to_door_sales",
                "drapery_window_covering_and_upholstery_stores",
                "drinking_places",
                "drug_stores_and_pharmacies",
                "drugs_drug_proprietaries_and_druggist_sundries",
                "dry_cleaners",
                "durable_goods",
                "duty_free_stores",
                "eating_places_restaurants",
                "educational_services",
                "electric_razor_stores",
                "electric_vehicle_charging",
                "electrical_parts_and_equipment",
                "electrical_services",
                "electronics_repair_shops",
                "electronics_stores",
                "elementary_secondary_schools",
                "emergency_services_gcas_visa_use_only",
                "employment_temp_agencies",
                "equipment_rental",
                "exterminating_services",
                "family_clothing_stores",
                "fast_food_restaurants",
                "financial_institutions",
                "fines_government_administrative_entities",
                "fireplace_fireplace_screens_and_accessories_stores",
                "floor_covering_stores",
                "florists",
                "florists_supplies_nursery_stock_and_flowers",
                "freezer_and_locker_meat_provisioners",
                "fuel_dealers_non_automotive",
                "funeral_services_crematories",
                "furniture_home_furnishings_and_equipment_stores_except_appliances",
                "furniture_repair_refinishing",
                "furriers_and_fur_shops",
                "general_services",
                "gift_card_novelty_and_souvenir_shops",
                "glass_paint_and_wallpaper_stores",
                "glassware_crystal_stores",
                "golf_courses_public",
                "government_licensed_horse_dog_racing_us_region_only",
                "government_licensed_online_casions_online_gambling_us_region_only",
                "government_owned_lotteries_non_us_region",
                "government_owned_lotteries_us_region_only",
                "government_services",
                "grocery_stores_supermarkets",
                "hardware_equipment_and_supplies",
                "hardware_stores",
                "health_and_beauty_spas",
                "hearing_aids_sales_and_supplies",
                "heating_plumbing_a_c",
                "hobby_toy_and_game_shops",
                "home_supply_warehouse_stores",
                "hospitals",
                "hotels_motels_and_resorts",
                "household_appliance_stores",
                "industrial_supplies",
                "information_retrieval_services",
                "insurance_default",
                "insurance_underwriting_premiums",
                "intra_company_purchases",
                "jewelry_stores_watches_clocks_and_silverware_stores",
                "landscaping_services",
                "laundries",
                "laundry_cleaning_services",
                "legal_services_attorneys",
                "luggage_and_leather_goods_stores",
                "lumber_building_materials_stores",
                "manual_cash_disburse",
                "marinas_service_and_supplies",
                "marketplaces",
                "masonry_stonework_and_plaster",
                "massage_parlors",
                "medical_and_dental_labs",
                "medical_dental_ophthalmic_and_hospital_equipment_and_supplies",
                "medical_services",
                "membership_organizations",
                "mens_and_boys_clothing_and_accessories_stores",
                "mens_womens_clothing_stores",
                "metal_service_centers",
                "miscellaneous",
                "miscellaneous_apparel_and_accessory_shops",
                "miscellaneous_auto_dealers",
                "miscellaneous_business_services",
                "miscellaneous_food_stores",
                "miscellaneous_general_merchandise",
                "miscellaneous_general_services",
                "miscellaneous_home_furnishing_specialty_stores",
                "miscellaneous_publishing_and_printing",
                "miscellaneous_recreation_services",
                "miscellaneous_repair_shops",
                "miscellaneous_specialty_retail",
                "mobile_home_dealers",
                "motion_picture_theaters",
                "motor_freight_carriers_and_trucking",
                "motor_homes_dealers",
                "motor_vehicle_supplies_and_new_parts",
                "motorcycle_shops_and_dealers",
                "motorcycle_shops_dealers",
                "music_stores_musical_instruments_pianos_and_sheet_music",
                "news_dealers_and_newsstands",
                "non_fi_money_orders",
                "non_fi_stored_value_card_purchase_load",
                "nondurable_goods",
                "nurseries_lawn_and_garden_supply_stores",
                "nursing_personal_care",
                "office_and_commercial_furniture",
                "opticians_eyeglasses",
                "optometrists_ophthalmologist",
                "orthopedic_goods_prosthetic_devices",
                "osteopaths",
                "package_stores_beer_wine_and_liquor",
                "paints_varnishes_and_supplies",
                "parking_lots_garages",
                "passenger_railways",
                "pawn_shops",
                "pet_shops_pet_food_and_supplies",
                "petroleum_and_petroleum_products",
                "photo_developing",
                "photographic_photocopy_microfilm_equipment_and_supplies",
                "photographic_studios",
                "picture_video_production",
                "piece_goods_notions_and_other_dry_goods",
                "plumbing_heating_equipment_and_supplies",
                "political_organizations",
                "postal_services_government_only",
                "precious_stones_and_metals_watches_and_jewelry",
                "professional_services",
                "public_warehousing_and_storage",
                "quick_copy_repro_and_blueprint",
                "railroads",
                "real_estate_agents_and_managers_rentals",
                "record_stores",
                "recreational_vehicle_rentals",
                "religious_goods_stores",
                "religious_organizations",
                "roofing_siding_sheet_metal",
                "secretarial_support_services",
                "security_brokers_dealers",
                "service_stations",
                "sewing_needlework_fabric_and_piece_goods_stores",
                "shoe_repair_hat_cleaning",
                "shoe_stores",
                "small_appliance_repair",
                "snowmobile_dealers",
                "special_trade_services",
                "specialty_cleaning",
                "sporting_goods_stores",
                "sporting_recreation_camps",
                "sports_and_riding_apparel_stores",
                "sports_clubs_fields",
                "stamp_and_coin_stores",
                "stationary_office_supplies_printing_and_writing_paper",
                "stationery_stores_office_and_school_supply_stores",
                "swimming_pools_sales",
                "t_ui_travel_germany",
                "tailors_alterations",
                "tax_payments_government_agencies",
                "tax_preparation_services",
                "taxicabs_limousines",
                "telecommunication_equipment_and_telephone_sales",
                "telecommunication_services",
                "telegraph_services",
                "tent_and_awning_shops",
                "testing_laboratories",
                "theatrical_ticket_agencies",
                "timeshares",
                "tire_retreading_and_repair",
                "tolls_bridge_fees",
                "tourist_attractions_and_exhibits",
                "towing_services",
                "trailer_parks_campgrounds",
                "transportation_services",
                "travel_agencies_tour_operators",
                "truck_stop_iteration",
                "truck_utility_trailer_rentals",
                "typesetting_plate_making_and_related_services",
                "typewriter_stores",
                "u_s_federal_government_agencies_or_departments",
                "uniforms_commercial_clothing",
                "used_merchandise_and_secondhand_stores",
                "utilities",
                "variety_stores",
                "veterinary_services",
                "video_amusement_game_supplies",
                "video_game_arcades",
                "video_tape_rental_stores",
                "vocational_trade_schools",
                "watch_jewelry_repair",
                "welding_repair",
                "wholesale_clubs",
                "wig_and_toupee_stores",
                "wires_money_orders",
                "womens_accessory_and_specialty_shops",
                "womens_ready_to_wear_stores",
                "wrecking_and_salvage_yards",
            ]
        ]
    ] = None
    """
    Array of strings containing
    [categories](https://docs.stripe.com/api#issuing_authorization_object-merchant_data-category)
    of authorizations to allow. All other categories will be blocked. Cannot be set
    with `blocked_categories`.
    """

    allowed_merchant_countries: Optional[List[str]] = None
    """
    Array of strings containing representing countries from which authorizations
    will be allowed. Authorizations from merchants in all other countries will be
    declined. Country codes should be ISO 3166 alpha-2 country codes (e.g. `US`).
    Cannot be set with `blocked_merchant_countries`. Provide an empty value to unset
    this control.
    """

    blocked_categories: Optional[
        List[
            Literal[
                "ac_refrigeration_repair",
                "accounting_bookkeeping_services",
                "advertising_services",
                "agricultural_cooperative",
                "airlines_air_carriers",
                "airports_flying_fields",
                "ambulance_services",
                "amusement_parks_carnivals",
                "antique_reproductions",
                "antique_shops",
                "aquariums",
                "architectural_surveying_services",
                "art_dealers_and_galleries",
                "artists_supply_and_craft_shops",
                "auto_and_home_supply_stores",
                "auto_body_repair_shops",
                "auto_paint_shops",
                "auto_service_shops",
                "automated_cash_disburse",
                "automated_fuel_dispensers",
                "automobile_associations",
                "automotive_parts_and_accessories_stores",
                "automotive_tire_stores",
                "bail_and_bond_payments",
                "bakeries",
                "bands_orchestras",
                "barber_and_beauty_shops",
                "betting_casino_gambling",
                "bicycle_shops",
                "billiard_pool_establishments",
                "boat_dealers",
                "boat_rentals_and_leases",
                "book_stores",
                "books_periodicals_and_newspapers",
                "bowling_alleys",
                "bus_lines",
                "business_secretarial_schools",
                "buying_shopping_services",
                "cable_satellite_and_other_pay_television_and_radio",
                "camera_and_photographic_supply_stores",
                "candy_nut_and_confectionery_stores",
                "car_and_truck_dealers_new_used",
                "car_and_truck_dealers_used_only",
                "car_rental_agencies",
                "car_washes",
                "carpentry_services",
                "carpet_upholstery_cleaning",
                "caterers",
                "charitable_and_social_service_organizations_fundraising",
                "chemicals_and_allied_products",
                "child_care_services",
                "childrens_and_infants_wear_stores",
                "chiropodists_podiatrists",
                "chiropractors",
                "cigar_stores_and_stands",
                "civic_social_fraternal_associations",
                "cleaning_and_maintenance",
                "clothing_rental",
                "colleges_universities",
                "commercial_equipment",
                "commercial_footwear",
                "commercial_photography_art_and_graphics",
                "commuter_transport_and_ferries",
                "computer_network_services",
                "computer_programming",
                "computer_repair",
                "computer_software_stores",
                "computers_peripherals_and_software",
                "concrete_work_services",
                "construction_materials",
                "consulting_public_relations",
                "correspondence_schools",
                "cosmetic_stores",
                "counseling_services",
                "country_clubs",
                "courier_services",
                "court_costs",
                "credit_reporting_agencies",
                "cruise_lines",
                "dairy_products_stores",
                "dance_hall_studios_schools",
                "dating_escort_services",
                "dentists_orthodontists",
                "department_stores",
                "detective_agencies",
                "digital_goods_applications",
                "digital_goods_games",
                "digital_goods_large_volume",
                "digital_goods_media",
                "direct_marketing_catalog_merchant",
                "direct_marketing_combination_catalog_and_retail_merchant",
                "direct_marketing_inbound_telemarketing",
                "direct_marketing_insurance_services",
                "direct_marketing_other",
                "direct_marketing_outbound_telemarketing",
                "direct_marketing_subscription",
                "direct_marketing_travel",
                "discount_stores",
                "doctors",
                "door_to_door_sales",
                "drapery_window_covering_and_upholstery_stores",
                "drinking_places",
                "drug_stores_and_pharmacies",
                "drugs_drug_proprietaries_and_druggist_sundries",
                "dry_cleaners",
                "durable_goods",
                "duty_free_stores",
                "eating_places_restaurants",
                "educational_services",
                "electric_razor_stores",
                "electric_vehicle_charging",
                "electrical_parts_and_equipment",
                "electrical_services",
                "electronics_repair_shops",
                "electronics_stores",
                "elementary_secondary_schools",
                "emergency_services_gcas_visa_use_only",
                "employment_temp_agencies",
                "equipment_rental",
                "exterminating_services",
                "family_clothing_stores",
                "fast_food_restaurants",
                "financial_institutions",
                "fines_government_administrative_entities",
                "fireplace_fireplace_screens_and_accessories_stores",
                "floor_covering_stores",
                "florists",
                "florists_supplies_nursery_stock_and_flowers",
                "freezer_and_locker_meat_provisioners",
                "fuel_dealers_non_automotive",
                "funeral_services_crematories",
                "furniture_home_furnishings_and_equipment_stores_except_appliances",
                "furniture_repair_refinishing",
                "furriers_and_fur_shops",
                "general_services",
                "gift_card_novelty_and_souvenir_shops",
                "glass_paint_and_wallpaper_stores",
                "glassware_crystal_stores",
                "golf_courses_public",
                "government_licensed_horse_dog_racing_us_region_only",
                "government_licensed_online_casions_online_gambling_us_region_only",
                "government_owned_lotteries_non_us_region",
                "government_owned_lotteries_us_region_only",
                "government_services",
                "grocery_stores_supermarkets",
                "hardware_equipment_and_supplies",
                "hardware_stores",
                "health_and_beauty_spas",
                "hearing_aids_sales_and_supplies",
                "heating_plumbing_a_c",
                "hobby_toy_and_game_shops",
                "home_supply_warehouse_stores",
                "hospitals",
                "hotels_motels_and_resorts",
                "household_appliance_stores",
                "industrial_supplies",
                "information_retrieval_services",
                "insurance_default",
                "insurance_underwriting_premiums",
                "intra_company_purchases",
                "jewelry_stores_watches_clocks_and_silverware_stores",
                "landscaping_services",
                "laundries",
                "laundry_cleaning_services",
                "legal_services_attorneys",
                "luggage_and_leather_goods_stores",
                "lumber_building_materials_stores",
                "manual_cash_disburse",
                "marinas_service_and_supplies",
                "marketplaces",
                "masonry_stonework_and_plaster",
                "massage_parlors",
                "medical_and_dental_labs",
                "medical_dental_ophthalmic_and_hospital_equipment_and_supplies",
                "medical_services",
                "membership_organizations",
                "mens_and_boys_clothing_and_accessories_stores",
                "mens_womens_clothing_stores",
                "metal_service_centers",
                "miscellaneous",
                "miscellaneous_apparel_and_accessory_shops",
                "miscellaneous_auto_dealers",
                "miscellaneous_business_services",
                "miscellaneous_food_stores",
                "miscellaneous_general_merchandise",
                "miscellaneous_general_services",
                "miscellaneous_home_furnishing_specialty_stores",
                "miscellaneous_publishing_and_printing",
                "miscellaneous_recreation_services",
                "miscellaneous_repair_shops",
                "miscellaneous_specialty_retail",
                "mobile_home_dealers",
                "motion_picture_theaters",
                "motor_freight_carriers_and_trucking",
                "motor_homes_dealers",
                "motor_vehicle_supplies_and_new_parts",
                "motorcycle_shops_and_dealers",
                "motorcycle_shops_dealers",
                "music_stores_musical_instruments_pianos_and_sheet_music",
                "news_dealers_and_newsstands",
                "non_fi_money_orders",
                "non_fi_stored_value_card_purchase_load",
                "nondurable_goods",
                "nurseries_lawn_and_garden_supply_stores",
                "nursing_personal_care",
                "office_and_commercial_furniture",
                "opticians_eyeglasses",
                "optometrists_ophthalmologist",
                "orthopedic_goods_prosthetic_devices",
                "osteopaths",
                "package_stores_beer_wine_and_liquor",
                "paints_varnishes_and_supplies",
                "parking_lots_garages",
                "passenger_railways",
                "pawn_shops",
                "pet_shops_pet_food_and_supplies",
                "petroleum_and_petroleum_products",
                "photo_developing",
                "photographic_photocopy_microfilm_equipment_and_supplies",
                "photographic_studios",
                "picture_video_production",
                "piece_goods_notions_and_other_dry_goods",
                "plumbing_heating_equipment_and_supplies",
                "political_organizations",
                "postal_services_government_only",
                "precious_stones_and_metals_watches_and_jewelry",
                "professional_services",
                "public_warehousing_and_storage",
                "quick_copy_repro_and_blueprint",
                "railroads",
                "real_estate_agents_and_managers_rentals",
                "record_stores",
                "recreational_vehicle_rentals",
                "religious_goods_stores",
                "religious_organizations",
                "roofing_siding_sheet_metal",
                "secretarial_support_services",
                "security_brokers_dealers",
                "service_stations",
                "sewing_needlework_fabric_and_piece_goods_stores",
                "shoe_repair_hat_cleaning",
                "shoe_stores",
                "small_appliance_repair",
                "snowmobile_dealers",
                "special_trade_services",
                "specialty_cleaning",
                "sporting_goods_stores",
                "sporting_recreation_camps",
                "sports_and_riding_apparel_stores",
                "sports_clubs_fields",
                "stamp_and_coin_stores",
                "stationary_office_supplies_printing_and_writing_paper",
                "stationery_stores_office_and_school_supply_stores",
                "swimming_pools_sales",
                "t_ui_travel_germany",
                "tailors_alterations",
                "tax_payments_government_agencies",
                "tax_preparation_services",
                "taxicabs_limousines",
                "telecommunication_equipment_and_telephone_sales",
                "telecommunication_services",
                "telegraph_services",
                "tent_and_awning_shops",
                "testing_laboratories",
                "theatrical_ticket_agencies",
                "timeshares",
                "tire_retreading_and_repair",
                "tolls_bridge_fees",
                "tourist_attractions_and_exhibits",
                "towing_services",
                "trailer_parks_campgrounds",
                "transportation_services",
                "travel_agencies_tour_operators",
                "truck_stop_iteration",
                "truck_utility_trailer_rentals",
                "typesetting_plate_making_and_related_services",
                "typewriter_stores",
                "u_s_federal_government_agencies_or_departments",
                "uniforms_commercial_clothing",
                "used_merchandise_and_secondhand_stores",
                "utilities",
                "variety_stores",
                "veterinary_services",
                "video_amusement_game_supplies",
                "video_game_arcades",
                "video_tape_rental_stores",
                "vocational_trade_schools",
                "watch_jewelry_repair",
                "welding_repair",
                "wholesale_clubs",
                "wig_and_toupee_stores",
                "wires_money_orders",
                "womens_accessory_and_specialty_shops",
                "womens_ready_to_wear_stores",
                "wrecking_and_salvage_yards",
            ]
        ]
    ] = None
    """
    Array of strings containing
    [categories](https://docs.stripe.com/api#issuing_authorization_object-merchant_data-category)
    of authorizations to decline. All other categories will be allowed. Cannot be
    set with `allowed_categories`.
    """

    blocked_merchant_countries: Optional[List[str]] = None
    """
    Array of strings containing representing countries from which authorizations
    will be declined. Country codes should be ISO 3166 alpha-2 country codes (e.g.
    `US`). Cannot be set with `allowed_merchant_countries`. Provide an empty value
    to unset this control.
    """

    spending_limits: Optional[List[SpendingControlsSpendingLimit]] = None
    """
    Limit spending with amount-based rules that apply across any cards this card
    replaced (i.e., its `replacement_for` card and _that_ card's `replacement_for`
    card, up the chain).
    """

    spending_limits_currency: Optional[str] = None
    """Currency of the amounts within `spending_limits`.

    Always the same as the currency of the card.
    """


class LatestFraudWarning(BaseModel):
    started_at: Optional[int] = None
    """Timestamp of the most recent fraud warning."""

    type: Optional[
        Literal["card_testing_exposure", "fraud_dispute_filed", "third_party_reported", "user_indicated_fraud"]
    ] = None
    """The type of fraud warning that most recently took place on this card.

    This field updates with every new fraud warning, so the value changes over time.
    If populated, cancel and reissue the card.
    """


class PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundleFeatures(BaseModel):
    card_logo: Literal["optional", "required", "unsupported"]
    """
    The policy for how to use card logo images in a card design with this physical
    bundle.
    """

    carrier_text: Literal["optional", "required", "unsupported"]
    """
    The policy for how to use carrier letter text in a card design with this
    physical bundle.
    """

    second_line: Literal["optional", "required", "unsupported"]
    """The policy for how to use a second line on a card with this physical bundle."""


class PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundle(BaseModel):
    """
    A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.
    """

    id: str
    """Unique identifier for the object."""

    features: PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundleFeatures

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    name: str
    """Friendly display name."""

    object: Literal["issuing.physical_bundle"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal["active", "inactive", "review"]
    """Whether this physical bundle can be used to create cards."""

    type: Literal["custom", "standard"]
    """
    Whether this physical bundle is a standard Stripe offering or custom-made for
    you.
    """


PersonalizationDesignIssuingPersonalizationDesignPhysicalBundle: TypeAlias = Union[
    str, PersonalizationDesignIssuingPersonalizationDesignPhysicalBundleIssuingPhysicalBundle
]


class PersonalizationDesignIssuingPersonalizationDesignPreferences(BaseModel):
    is_default: bool
    """
    Whether we use this personalization design to create cards when one isn't
    specified. A connected account uses the Connect platform's default design if no
    personalization design is set as the default design.
    """

    is_platform_default: Optional[bool] = None
    """
    Whether this personalization design is used to create cards when one is not
    specified and a default for this connected account does not exist.
    """


class PersonalizationDesignIssuingPersonalizationDesignRejectionReasons(BaseModel):
    card_logo: Optional[
        List[
            Literal[
                "geographic_location",
                "inappropriate",
                "network_name",
                "non_binary_image",
                "non_fiat_currency",
                "other",
                "other_entity",
                "promotional_material",
            ]
        ]
    ] = None
    """The reason(s) the card logo was rejected."""

    carrier_text: Optional[
        List[
            Literal[
                "geographic_location",
                "inappropriate",
                "network_name",
                "non_fiat_currency",
                "other",
                "other_entity",
                "promotional_material",
            ]
        ]
    ] = None
    """The reason(s) the carrier text was rejected."""


PersonalizationDesignIssuingPersonalizationDesignCardLogo: TypeAlias = Union[str, "File", None]


class PersonalizationDesignIssuingPersonalizationDesignCarrierText(BaseModel):
    footer_body: Optional[str] = None
    """The footer body text of the carrier letter."""

    footer_title: Optional[str] = None
    """The footer title text of the carrier letter."""

    header_body: Optional[str] = None
    """The header body text of the carrier letter."""

    header_title: Optional[str] = None
    """The header title text of the carrier letter."""


class PersonalizationDesignIssuingPersonalizationDesign(BaseModel):
    """
    A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["issuing.personalization_design"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    physical_bundle: PersonalizationDesignIssuingPersonalizationDesignPhysicalBundle
    """The physical bundle object belonging to this personalization design."""

    preferences: PersonalizationDesignIssuingPersonalizationDesignPreferences

    rejection_reasons: PersonalizationDesignIssuingPersonalizationDesignRejectionReasons

    status: Literal["active", "inactive", "rejected", "review"]
    """Whether this personalization design can be used to create cards."""

    card_logo: Optional[PersonalizationDesignIssuingPersonalizationDesignCardLogo] = None
    """The file for the card logo to use with physical bundles that support card logos.

    Must have a `purpose` value of `issuing_logo`.
    """

    carrier_text: Optional[PersonalizationDesignIssuingPersonalizationDesignCarrierText] = None

    lookup_key: Optional[str] = None
    """
    A lookup key used to retrieve personalization designs dynamically from a static
    string. This may be up to 200 characters.
    """

    name: Optional[str] = None
    """Friendly display name."""


PersonalizationDesign: TypeAlias = Union[str, PersonalizationDesignIssuingPersonalizationDesign, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    ReplacedBy = TypeAliasType("ReplacedBy", Union[str, "IssuingCard", None])
else:
    ReplacedBy: TypeAlias = Union[str, "IssuingCard", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    ReplacementFor = TypeAliasType("ReplacementFor", Union[str, "IssuingCard", None])
else:
    ReplacementFor: TypeAlias = Union[str, "IssuingCard", None]


class ShippingAddressValidation(BaseModel):
    mode: Literal["disabled", "normalization_only", "validation_and_normalization"]
    """The address validation capabilities to use."""

    normalized_address: Optional[Address] = None

    result: Optional[Literal["indeterminate", "likely_deliverable", "likely_undeliverable"]] = None
    """The validation result for the shipping address."""


class ShippingCustoms(BaseModel):
    eori_number: Optional[str] = None
    """A registration number used for customs in Europe.

    See [https://www.gov.uk/eori](https://www.gov.uk/eori) for the UK and
    [https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en](https://ec.europa.eu/taxation_customs/business/customs-procedures-import-and-export/customs-procedures/economic-operators-registration-and-identification-number-eori_en)
    for the EU.
    """


class Shipping(BaseModel):
    address: Address

    name: str
    """Recipient name."""

    service: Literal["express", "priority", "standard"]
    """Shipment service, such as `standard` or `express`."""

    type: Literal["bulk", "individual"]
    """Packaging options."""

    address_validation: Optional[ShippingAddressValidation] = None

    carrier: Optional[Literal["dhl", "fedex", "royal_mail", "usps"]] = None
    """The delivery company that shipped a card."""

    customs: Optional[ShippingCustoms] = None

    eta: Optional[int] = None
    """
    A unix timestamp representing a best estimate of when the card will be
    delivered.
    """

    phone_number: Optional[str] = None
    """The phone number of the receiver of the shipment.

    Our courier partners will use this number to contact you in the event of card
    delivery issues. For individual shipments to the EU/UK, if this field is empty,
    we will provide them with the phone number provided when the cardholder was
    initially created.
    """

    require_signature: Optional[bool] = None
    """Whether a signature is required for card delivery.

    This feature is only supported for US users. Standard shipping service does not
    support signature on delivery. The default value for standard shipping service
    is false and for express and priority services is true.
    """

    status: Optional[Literal["canceled", "delivered", "failure", "pending", "returned", "shipped", "submitted"]] = None
    """The delivery status of the card."""

    tracking_number: Optional[str] = None
    """A tracking number for a card shipment."""

    tracking_url: Optional[str] = None
    """
    A link to the shipping carrier's site where you can view detailed information
    about a card shipment.
    """


class WalletsApplePay(BaseModel):
    eligible: bool
    """Apple Pay Eligibility"""

    ineligible_reason: Optional[Literal["missing_agreement", "missing_cardholder_contact", "unsupported_region"]] = None
    """Reason the card is ineligible for Apple Pay"""


class WalletsGooglePay(BaseModel):
    eligible: bool
    """Google Pay Eligibility"""

    ineligible_reason: Optional[Literal["missing_agreement", "missing_cardholder_contact", "unsupported_region"]] = None
    """Reason the card is ineligible for Google Pay"""


class Wallets(BaseModel):
    apple_pay: WalletsApplePay

    google_pay: WalletsGooglePay

    primary_account_identifier: Optional[str] = None
    """Unique identifier for a card used with digital wallets"""


class IssuingCard(BaseModel):
    """
    You can [create physical or virtual cards](https://docs.stripe.com/issuing) that are issued to cardholders.
    """

    id: str
    """Unique identifier for the object."""

    brand: str
    """The brand of the card."""

    cardholder: "IssuingCardholder"
    """
    An Issuing `Cardholder` object represents an individual or business entity who
    is [issued](https://docs.stripe.com/issuing) cards.

    Related guide:
    [How to create a cardholder](https://docs.stripe.com/issuing/cards/virtual/issue-cards#create-cardholder)
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp`
    in the UK.
    """

    exp_month: int
    """The expiration month of the card."""

    exp_year: int
    """The expiration year of the card."""

    last4: str
    """The last 4 digits of the card number."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["issuing.card"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    spending_controls: SpendingControls

    status: Literal["active", "canceled", "inactive"]
    """Whether authorizations can be approved on this card.

    May be blocked from activating cards depending on past-due Cardholder
    requirements. Defaults to `inactive`.
    """

    type: Literal["physical", "virtual"]
    """The type of the card."""

    cancellation_reason: Optional[Literal["design_rejected", "lost", "stolen"]] = None
    """The reason why the card was canceled."""

    cvc: Optional[str] = None
    """The card's CVC.

    For security reasons, this is only available for virtual cards, and will be
    omitted unless you explicitly request it with
    [the `expand` parameter](https://docs.stripe.com/api/expanding_objects).
    Additionally, it's only available via the
    ["Retrieve a card" endpoint](https://docs.stripe.com/api/issuing/cards/retrieve),
    not via "List all cards" or any other endpoint.
    """

    financial_account: Optional[str] = None
    """The financial account this card is attached to."""

    latest_fraud_warning: Optional[LatestFraudWarning] = None

    number: Optional[str] = None
    """The full unredacted card number.

    For security reasons, this is only available for virtual cards, and will be
    omitted unless you explicitly request it with
    [the `expand` parameter](https://docs.stripe.com/api/expanding_objects).
    Additionally, it's only available via the
    ["Retrieve a card" endpoint](https://docs.stripe.com/api/issuing/cards/retrieve),
    not via "List all cards" or any other endpoint.
    """

    personalization_design: Optional[PersonalizationDesign] = None
    """The personalization design object belonging to this card."""

    replaced_by: Optional[ReplacedBy] = None
    """The latest card that replaces this card, if any."""

    replacement_for: Optional[ReplacementFor] = None
    """The card this card replaces, if any."""

    replacement_reason: Optional[Literal["damaged", "expired", "lost", "stolen"]] = None
    """The reason why the previous card needed to be replaced."""

    second_line: Optional[str] = None
    """Text separate from cardholder name, printed on the card."""

    shipping: Optional[Shipping] = None

    wallets: Optional[Wallets] = None


from .file import File
from .issuing_cardholder import IssuingCardholder
