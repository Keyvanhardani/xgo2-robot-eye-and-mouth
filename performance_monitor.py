#!/usr/bin/env python3
# Performance monitoring for XGO2 robot animations

import time
import psutil
from datetime import datetime

class PerformanceMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.frame_times = []
        
    def track_frame_time(self, frame_duration):
        """Track frame rendering performance"""
        self.frame_times.append(frame_duration)
        
        # Keep only last 100 frames
        if len(self.frame_times) > 100:
            self.frame_times.pop(0)
    
    def get_fps(self):
        """Calculate current FPS"""
        if not self.frame_times:
            return 0
        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        return 1.0 / avg_frame_time if avg_frame_time > 0 else 0
    
    def get_system_stats(self):
        """Get system resource usage"""
        return {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'timestamp': datetime.now().isoformat()
        }
    
    def log_performance(self):
        """Log current performance metrics"""
        stats = self.get_system_stats()
        fps = self.get_fps()
        
        print(f"FPS: {fps:.2f} | CPU: {stats['cpu_percent']}% | Memory: {stats['memory_percent']}%")
