# views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from Authentification.models import CustomUser

@login_required
def private_chat(request, user1_id, user2_id):
    user1 = get_object_or_404(CustomUser, id=user1_id)
    user2 = get_object_or_404(CustomUser, id=user2_id)
    room, _ = PrivateChatRoom.objects.get_or_create(user1=min(user1, user2, key=lambda x: x.id), user2=max(user1, user2, key=lambda x: x.id))

    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            message = ChatMessage.objects.create(room=room, sender=request.user, message=message_text)
            return JsonResponse({'status': 'Message sent', 'message_id': message.id}, status=201)

    messages = room.messages.all().order_by('timestamp')
    return render(request, 'chat_room.html', {
        'room': room,
        'messages': messages,
        'user1': user1,
        'user2': user2,
    })