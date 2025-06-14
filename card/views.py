from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django_ratelimit.decorators import ratelimit

from .models import MifareClassicCard, MifareClassicCardSector


@ratelimit(key="ip", rate="30/m", method="GET", block=True)
@require_http_methods(["GET"])
def get_card(request, uid):
    card = get_object_or_404(MifareClassicCard, uid__iexact=uid)
    card_sectors = MifareClassicCardSector.objects.filter(card=card).values(
        "index", "key_a", "key_b"
    )

    return JsonResponse(
        {
            "uid": card.uid,
            "type": card.type,
            "number": card.number,
            "nickname": card.nickname,
            "is_kuokuang_card": card.is_kuokuang_card,
            # TODO: Deprecated fields, remove in future versions
            # ==================================================================
            "name": card.number,
            "comment": card.nickname,
            "tags": ["KuoKuangCard"] if card.is_kuokuang_card else [],
            # ==================================================================
            "sectors": [
                {
                    "index": sector["index"],
                    "keyA": sector["key_a"],
                    "keyB": sector["key_b"],
                }
                for sector in card_sectors
            ],
        }
    )
