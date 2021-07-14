#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Change starting timecode of all clips in the current bin. Requires DaVinci Resolve Studio.
# Copyright (c) 2020 Igor Riđanović, igor ( at ) hdhead.com

import sys
from python_get_resolve import GetResolve

def _validate(x):
	# Validate and reformat timecode string

	if len(x) != 11:
		sys.exit('Invalid timecode. Try again.')

	c = ':'
	colonized = x[:2] + c + x[3:5] + c + x[6:8] + c + x[9:]
	
	if colonized.replace(':', '').isdigit():
		return colonized

	else:
		sys.exit('Invalid timecode. Try again.')
	


def reset_clip_timecode(x):

	tcValid = _validate(x)

	projectmanager = resolve.GetProjectManager()
	project        = projectmanager.GetCurrentProject()
	mediapool      = project.GetMediaPool()
	currentbin     = mediapool.GetCurrentFolder()
	clips          = currentbin.GetClips()

	for clip in clips.values():

		# Set new starting timecode to each clip
		clip.SetClipProperty('Start TC', tcValid)

		# Check back new timecodes, pre V17
		print clip.GetClipProperty('Start TC')['Start TC'],\
			  clip.GetClipProperty('Clip Name')['Clip Name']
		
# 		# Check back new timecodes, V17
# 		print clip.GetClipProperty('Start TC'),\
# 			  clip.GetClipProperty('Clip Name')


if __name__ == '__main__':
	resolve = GetResolve()

	timecode = raw_input('Set timecode for all clips in the current bin: ')
	reset_clip_timecode(timecode)
