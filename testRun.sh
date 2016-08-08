#!/bin/bash
grep "TotalEvents" $1
grep "Timing-tstoragefile-write-totalMegabytes" $1
grep "PeakValueRss" $1
grep "AvgEventTime" $1
grep "AvgEventCPU" $1
grep "TotalJobCPU" $1
