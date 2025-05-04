from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Avg, Count, Sum, Min, Max
from .filters import JobFilter
from rest_framework.pagination import PageNumberPagination


# Create your views here.
@api_view(['GET'])
def getAllJobs(request):
    filterset = JobFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    
    count = filterset.qs.count()

    resPerPage = 1
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage

    queryset = paginator.paginate_queryset(filterset.qs, request)

    serializer = JobSerializer(queryset, many=True)
    return Response(
        {
            'count': count,
            'resPerPage': resPerPage,
            'jobs': serializer.data,
        },
    )


@api_view(['GET'])
def getJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def new_job(request):
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_job(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.title = request.data('title')
    job.description = request.data('description')
    job.email = request.data('email')
    job.address = request.data('address')
    job.job_type = request.data('job_type')
    job.education = request.data('education')
    job.industry = request.data('industry')
    job.experience = request.data('experience')
    job.salary = request.data('salary')
    job.positions = request.data('positions')
    job.company = request.data('company')
    job.last_date = request.data('last_date')
    job.save()

    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)



@api_view(['DELETE'])
def delete_job(request, pk):
    job = get_object_or_404(Job, id=pk)
    job.delete()
    return Response('Job Deleted', status=202)


@api_view(['GET'])
def getTopicStats(request, topic):
    args = {'title__icontains': topic}
    jobs = Job.objects.filter(**args)

    if len(jobs) == 0:
        return Response('No jobs found for {topic}'.format(topic=topic))
    
    stats = jobs.aggregate(
        total_jobs = Count("title"),
        avg_positions = Avg("positions"),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Max('salary'),
    )

    return Response(stats)