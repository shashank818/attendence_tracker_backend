from abc import ABC, abstractmethod


class AttendanceFilterStorageInterface(ABC):
    @abstractmethod
    def get_filtered_attendance(self, user_id, status=None, start_date=None,
                                end_date=None):
        pass
