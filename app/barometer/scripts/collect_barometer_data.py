from django.db.models import QuerySet

from app.barometer.models import Barometer
from app.core.core_scripts.utils import Utility


class CollectBarometerData:

    @staticmethod
    @Utility.time_it('list_data()')
    def list_data(queryset: QuerySet[Barometer]) -> dict:
        out_data = {
            'temperature_c': [],
            'humidity': [],
            'pressure_hpa': [],
            'device': [],
            'time_created': [],
            'xaxis_range': [],
        }

        if not queryset:
            return out_data

        x_axis_limit = 144  # 6 point in hour * 24 hours = ideally 1 day
        query_list = list(queryset)
        last_obj = query_list[-1]

        if len(query_list) >= x_axis_limit:
            last_x_obj = query_list[-x_axis_limit]
        else:
            last_x_obj = query_list[0]

        out_data.get('xaxis_range').extend([
            Utility.get_local_datetime_as_str(last_x_obj.time_created),
            Utility.get_local_datetime_as_str(last_obj.time_created),
        ])

        for data_obj in query_list:
            out_data.get('temperature_c').append(float(data_obj.temperature_c))
            out_data.get('humidity').append(float(data_obj.humidity))
            out_data.get('time_created').append(Utility.get_local_datetime_as_str(data_obj.time_created))
            out_data.get('pressure_hpa').append(float(data_obj.pressure_hpa))

        return out_data
