import pytest
from users import models


# @pytest.skip('wip')
# def test_user_profile(self, models.UserProfile):
#   pass

# combine querysets
queryset_chain = chain(
    				monday,
				    tuesday,
				    wednesday,
				    thursday,
				    friday,
				    saturday,
				    sunday,
				)

qs = sorted(queryset_chain,
            key=lambda instance: instance.pk,
            reverse=True)


# an or lookup
or_lookup = (Q(title__icontains=query) | Q(description__icontains=query)

# an and lookup
and_lookup=(Q(title__icontains=query) & Q(description__icontains=query)
