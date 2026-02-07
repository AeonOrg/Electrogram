# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from .get_payment_form import GetPaymentForm
from .get_payment_receipt import GetPaymentReceipt
from .validate_requested_info import ValidateRequestedInfo
from .send_payment_form import SendPaymentForm
from .get_saved_info import GetSavedInfo
from .clear_saved_info import ClearSavedInfo
from .get_bank_card_data import GetBankCardData
from .export_invoice import ExportInvoice
from .assign_app_store_transaction import AssignAppStoreTransaction
from .assign_play_market_transaction import AssignPlayMarketTransaction
from .get_premium_gift_code_options import GetPremiumGiftCodeOptions
from .check_gift_code import CheckGiftCode
from .apply_gift_code import ApplyGiftCode
from .get_giveaway_info import GetGiveawayInfo
from .launch_prepaid_giveaway import LaunchPrepaidGiveaway
from .get_stars_topup_options import GetStarsTopupOptions
from .get_stars_status import GetStarsStatus
from .get_stars_transactions import GetStarsTransactions
from .send_stars_form import SendStarsForm
from .refund_stars_charge import RefundStarsCharge
from .get_stars_revenue_stats import GetStarsRevenueStats
from .get_stars_revenue_withdrawal_url import GetStarsRevenueWithdrawalUrl
from .get_stars_revenue_ads_account_url import GetStarsRevenueAdsAccountUrl
from .get_stars_transactions_by_id import GetStarsTransactionsByID
from .get_stars_gift_options import GetStarsGiftOptions
from .get_stars_subscriptions import GetStarsSubscriptions
from .change_stars_subscription import ChangeStarsSubscription
from .fulfill_stars_subscription import FulfillStarsSubscription
from .get_stars_giveaway_options import GetStarsGiveawayOptions
from .get_star_gifts import GetStarGifts
from .save_star_gift import SaveStarGift
from .convert_star_gift import ConvertStarGift
from .bot_cancel_stars_subscription import BotCancelStarsSubscription
from .get_connected_star_ref_bots import GetConnectedStarRefBots
from .get_connected_star_ref_bot import GetConnectedStarRefBot
from .get_suggested_star_ref_bots import GetSuggestedStarRefBots
from .connect_star_ref_bot import ConnectStarRefBot
from .edit_connected_star_ref_bot import EditConnectedStarRefBot
from .get_star_gift_upgrade_preview import GetStarGiftUpgradePreview
from .upgrade_star_gift import UpgradeStarGift
from .transfer_star_gift import TransferStarGift
from .get_unique_star_gift import GetUniqueStarGift
from .get_saved_star_gifts import GetSavedStarGifts
from .get_saved_star_gift import GetSavedStarGift
from .get_star_gift_withdrawal_url import GetStarGiftWithdrawalUrl
from .toggle_chat_star_gift_notifications import ToggleChatStarGiftNotifications
from .toggle_star_gifts_pinned_to_top import ToggleStarGiftsPinnedToTop
from .can_purchase_store import CanPurchaseStore
from .get_resale_star_gifts import GetResaleStarGifts
from .update_star_gift_price import UpdateStarGiftPrice
from .create_star_gift_collection import CreateStarGiftCollection
from .update_star_gift_collection import UpdateStarGiftCollection
from .reorder_star_gift_collections import ReorderStarGiftCollections
from .delete_star_gift_collection import DeleteStarGiftCollection
from .get_star_gift_collections import GetStarGiftCollections
from .get_unique_star_gift_value_info import GetUniqueStarGiftValueInfo
from .check_can_send_gift import CheckCanSendGift
from .get_star_gift_auction_state import GetStarGiftAuctionState
from .get_star_gift_auction_acquired_gifts import GetStarGiftAuctionAcquiredGifts
from .get_star_gift_active_auctions import GetStarGiftActiveAuctions
from .resolve_star_gift_offer import ResolveStarGiftOffer
from .send_star_gift_offer import SendStarGiftOffer
from .get_star_gift_upgrade_attributes import GetStarGiftUpgradeAttributes
from .request_recurring_payment import RequestRecurringPayment


__all__ = [
    "GetPaymentForm",
    "GetPaymentReceipt",
    "ValidateRequestedInfo",
    "SendPaymentForm",
    "GetSavedInfo",
    "ClearSavedInfo",
    "GetBankCardData",
    "ExportInvoice",
    "AssignAppStoreTransaction",
    "AssignPlayMarketTransaction",
    "GetPremiumGiftCodeOptions",
    "CheckGiftCode",
    "ApplyGiftCode",
    "GetGiveawayInfo",
    "LaunchPrepaidGiveaway",
    "GetStarsTopupOptions",
    "GetStarsStatus",
    "GetStarsTransactions",
    "SendStarsForm",
    "RefundStarsCharge",
    "GetStarsRevenueStats",
    "GetStarsRevenueWithdrawalUrl",
    "GetStarsRevenueAdsAccountUrl",
    "GetStarsTransactionsByID",
    "GetStarsGiftOptions",
    "GetStarsSubscriptions",
    "ChangeStarsSubscription",
    "FulfillStarsSubscription",
    "GetStarsGiveawayOptions",
    "GetStarGifts",
    "SaveStarGift",
    "ConvertStarGift",
    "BotCancelStarsSubscription",
    "GetConnectedStarRefBots",
    "GetConnectedStarRefBot",
    "GetSuggestedStarRefBots",
    "ConnectStarRefBot",
    "EditConnectedStarRefBot",
    "GetStarGiftUpgradePreview",
    "UpgradeStarGift",
    "TransferStarGift",
    "GetUniqueStarGift",
    "GetSavedStarGifts",
    "GetSavedStarGift",
    "GetStarGiftWithdrawalUrl",
    "ToggleChatStarGiftNotifications",
    "ToggleStarGiftsPinnedToTop",
    "CanPurchaseStore",
    "GetResaleStarGifts",
    "UpdateStarGiftPrice",
    "CreateStarGiftCollection",
    "UpdateStarGiftCollection",
    "ReorderStarGiftCollections",
    "DeleteStarGiftCollection",
    "GetStarGiftCollections",
    "GetUniqueStarGiftValueInfo",
    "CheckCanSendGift",
    "GetStarGiftAuctionState",
    "GetStarGiftAuctionAcquiredGifts",
    "GetStarGiftActiveAuctions",
    "ResolveStarGiftOffer",
    "SendStarGiftOffer",
    "GetStarGiftUpgradeAttributes",
    "RequestRecurringPayment",
    "contest",
    "auth",
    "account",
    "users",
    "contacts",
    "messages",
    "updates",
    "photos",
    "upload",
    "help",
    "channels",
    "bots",
    "payments",
    "stickers",
    "phone",
    "langpack",
    "folders",
    "stats",
    "chatlists",
    "stories",
    "premium",
    "smsjobs",
    "fragment",
]
