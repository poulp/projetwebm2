#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

def home(request):
  return render_to_response('general/home.html',{})
