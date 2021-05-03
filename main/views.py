from django.shortcuts import render, redirect
from .models import Work, WorkPicture, Collection
from .forms import WorkForm, WorkPictureForm, CollectionForm


def work_list(request):
    work_images = WorkPicture.objects.filter(is_main=True)

    top_collections = Collection.objects.order_by('-collection_views')[:2]

    top_works = Work.objects.order_by('-work_views')[:2]
    top_work_images = WorkPicture.objects.filter(work__in=list(top_works))
    context = {
        'work_images': work_images,
        'work_cards': top_work_images,
        'collection_cards': top_collections
    }
    return render(request, 'main/home.html', context)


def collection_list(request):
    collections = Collection.objects.all()

    top_collections = Collection.objects.order_by('-collection_views')[:2]

    top_works = Work.objects.order_by('-work_views')[:2]
    top_work_images = WorkPicture.objects.filter(work__in=list(top_works))
    context = {
        'collections': collections,
        'work_cards': top_work_images,
        'collection_cards': top_collections
    }
    return render(request, 'main/collections.html', context)


def work_add(request):
    if request.method == 'POST':
        work_form = WorkForm(request.POST)
        work_picture_form = WorkPictureForm(request.POST, request.FILES)

        if work_form.is_valid() and work_picture_form.is_valid():
            work_obj = work_form.save()

            work_pic_obj = work_picture_form.save(commit=False)
            work_pic_obj.is_main = True
            work_pic_obj.work = work_obj
            work_pic_obj.save()
            return redirect('home')

    work_form = WorkForm()
    work_picture_form = WorkPictureForm()
    context = {
        'work_form': work_form,
        'work_picture_form': work_picture_form
    }
    return render(request, 'main/add_work.html', context)


def collection_add(request):
    if request.method == 'POST':
        collection_form = CollectionForm(request.POST, request.FILES)

        if collection_form.is_valid():
            collection = collection_form.save()
            works = collection_form.cleaned_data.get('work_select')
            for work in works:
                work.collection = collection
                work.save()
            return redirect('home')

    collection_form = CollectionForm()
    context = {
        'collection_form': collection_form,
    }
    return render(request, 'main/add_collection.html', context)


def work_detail(request, pk):
    work = Work.objects.get(pk=pk)
    work.work_views += 1
    work.save()
    work_images_qs = WorkPicture.objects.filter(work=work)

    top_collections = Collection.objects.order_by('-collection_views')[:2]

    top_works = Work.objects.order_by('-work_views')[:2]
    top_work_images = WorkPicture.objects.filter(work__in=list(top_works))
    context = {
        'work': work,
        'work_images': work_images_qs,
        'work_cards': top_work_images,
        'collection_cards': top_collections
    }
    return render(request, 'main/work_detail.html', context)


def collection_detail(request, pk):
    collection = Collection.objects.get(pk=pk)

    works = Work.objects.filter(collection=collection)
    work_images_qs = WorkPicture.objects.filter(work__in=works)

    top_collections = Collection.objects.order_by('-collection_views')[:2]

    top_works = Work.objects.order_by('-work_views')[:2]
    top_work_images = WorkPicture.objects.filter(work__in=list(top_works))
    context = {
        'collection': collection,
        'work_images': work_images_qs,
        'work_cards': top_work_images,
        'collection_cards': top_collections
    }
    return render(request, 'main/collection_detail.html', context)


def work_delete(request, pk):
    work = Work.objects.get(pk=pk)
    work.delete()
    return redirect('home')
