from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from .models import PurchaseQuotetionInfo,PurchaseQuotetionItem
@csrf_exempt
def purchase_quotetion_info(request):
    if request.method == 'POST':
        # requisition_no = request.POST.get('PurchaseQuotetionInfo')
        # order_info = PurchaseQuotetionInfo.objects.get(docNo=requisition_no)

        return JsonResponse({'fg':"requisition_no"})
        # Replace the filter conditions with the ones you need
        # try:
        #     order_info = PurchaseQuotetionInfo.objects.get(docNo=requisition_no)
        #     response_data = {
        #         'docNo': requisition_no,
        #         'customerName': order_info.customerName.id,
        #         'address': order_info.address,
        #         'totalAmount': order_info.totalAmount,
        #         'totalQty': order_info.totalQty,
        #     }
        #     return JsonResponse(response_data)
        # except PurchaseQuotetionInfo.DoesNotExist:
        #     return JsonResponse({'error': 'No data found for the given requisitionNo'}, status=404)
        # except Exception as e:
        #     return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)