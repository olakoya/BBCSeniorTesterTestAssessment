'''

(.venv) olakoya@MacBookPro BBCSeniorTesterTestAssessment % pytest -s -v tests/test_schedule_api_steps.py
========================================================================= test session starts =========================================================================
platform darwin -- Python 3.9.6, pytest-8.3.4, pluggy-1.5.0 -- /Users/olakoya/Desktop/automationwithpython/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.9.6', 'Platform': 'macOS-10.16-x86_64-i386-64bit', 'Packages': {'pytest': '8.3.4', 'pluggy': '1.5.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'allure-pytest': '2.13.5', 'bdd': '8.1.0', 'xdist': '3.6.1', 'requests-mock': '1.12.1'}}
rootdir: /Users/olakoya/Desktop/BBCSeniorTesterTestAssessment
plugins: html-4.1.1, metadata-3.1.1, allure-pytest-2.13.5, bdd-8.1.0, xdist-3.6.1, requests-mock-1.12.1
collected 7 items

tests/test_schedule_api_steps.py::test_verify_status_code_and_response_time PASSED
tests/test_schedule_api_steps.py::test_verify_every_item_has_a_nonempty_id_and_type_is_always_episode FAILED
tests/test_schedule_api_steps.py::test_verify_every_episode_title_is_never_null_or_empty FAILED
tests/test_schedule_api_steps.py::test_verify_only_one_episode_is_live FAILED
tests/test_schedule_api_steps.py::test_verify_start_date_is_before_end_date FAILED
tests/test_schedule_api_steps.py::test_verify_date_in_response_headers PASSED
tests/test_schedule_api_steps.py::test_verify_404_and_error_object_for_invalid_date FAILED

============================================================================== FAILURES ===============================================================================
_________________________________________________ test_verify_every_item_has_a_nonempty_id_and_type_is_always_episode _________________________________________________

fixturefunc = <function check_ids at 0x7fb030f08670>, request = <FixtureRequest for <Function test_verify_every_item_has_a_nonempty_id_and_type_is_always_episode>>
kwargs = {}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/_pytest/fixtures.py:898:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    @then("each item should have a non-empty id")
    def check_ids():
        data = response.json()
        for item in data.get("schedule", []):
>           assert item.get("id")
E           AttributeError: 'str' object has no attribute 'get'

tests/test_schedule_api_steps.py:39: AttributeError
_______________________________________________________ test_verify_every_episode_title_is_never_null_or_empty ________________________________________________________

fixturefunc = <function check_titles at 0x7fb030f089d0>, request = <FixtureRequest for <Function test_verify_every_episode_title_is_never_null_or_empty>>, kwargs = {}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/_pytest/fixtures.py:898:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    @then("each episode should have a non-empty title")
    def check_titles():
        data = response.json()
        for item in data.get("schedule", []):
>           title = item.get("episode", {}).get("title")
E           AttributeError: 'str' object has no attribute 'get'

tests/test_schedule_api_steps.py:53: AttributeError
________________________________________________________________ test_verify_only_one_episode_is_live _________________________________________________________________

fixturefunc = <function check_only_one_live at 0x7fb030f08b80>, request = <FixtureRequest for <Function test_verify_only_one_episode_is_live>>, kwargs = {}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/_pytest/fixtures.py:898:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
tests/test_schedule_api_steps.py:60: in check_only_one_live
    lives = [item.get("episode", {}).get("live") for item in data.get("schedule", [])]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

.0 = <dict_keyiterator object at 0x7fb031012b30>

>   lives = [item.get("episode", {}).get("live") for item in data.get("schedule", [])]
E   AttributeError: 'str' object has no attribute 'get'

tests/test_schedule_api_steps.py:60: AttributeError
______________________________________________________________ test_verify_start_date_is_before_end_date ______________________________________________________________

fixturefunc = <function check_transmission_dates at 0x7fb030f08d30>, request = <FixtureRequest for <Function test_verify_start_date_is_before_end_date>>, kwargs = {}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/_pytest/fixtures.py:898:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    @then("transmission_start must be before transmission_end")
    def check_transmission_dates():
        data = response.json()
        for item in data.get("schedule", []):
>           start = item.get("transmission_start")
E           AttributeError: 'str' object has no attribute 'get'

tests/test_schedule_api_steps.py:68: AttributeError
__________________________________________________________ test_verify_404_and_error_object_for_invalid_date __________________________________________________________

self = <Response [404]>, kwargs = {}

    def json(self, **kwargs):
        r"""Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        """

        if not self.encoding and self.content and len(self.content) > 3:
            # No encoding set. JSON RFC 4627 section 3 states we should expect
            # UTF-8, -16 or -32. Detect which one to use; If the detection or
            # decoding fails, fall back to `self.text` (using charset_normalizer to make
            # a best guess).
            encoding = guess_json_utf(self.content)
            if encoding is not None:
                try:
                    return complexjson.loads(self.content.decode(encoding), **kwargs)
                except UnicodeDecodeError:
                    # Wrong UTF codec detected; usually because it's not UTF-8
                    # but some other 8-bit codec.  This is an RFC violation,
                    # and the server didn't bother to tell us what codec *was*
                    # used.
                    pass
                except JSONDecodeError as e:
                    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

        try:
>           return complexjson.loads(self.text, **kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/requests/models.py:974:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/json/__init__.py:346: in loads
    return _default_decoder.decode(s)
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/json/decoder.py:337: in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <json.decoder.JSONDecoder object at 0x7fb02e6e56d0>, s = 'Endpoint not found', idx = 0

    def raw_decode(self, s, idx=0):
        """Decode a JSON document from ``s`` (a ``str`` beginning with
        a JSON document) and return a 2-tuple of the Python
        representation and the index in ``s`` where the document ended.

        This can be used to decode a JSON document from a string that may
        have extraneous data at the end.

        """
        try:
            obj, end = self.scan_once(s, idx)
        except StopIteration as err:
>           raise JSONDecodeError("Expecting value", s, err.value) from None
E           json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/json/decoder.py:355: JSONDecodeError

During handling of the above exception, another exception occurred:

fixturefunc = <function check_error_object at 0x7fb030f0d280>, request = <FixtureRequest for <Function test_verify_404_and_error_object_for_invalid_date>>, kwargs = {}

    def call_fixture_func(
        fixturefunc: _FixtureFunc[FixtureValue], request: FixtureRequest, kwargs
    ) -> FixtureValue:
        if is_generator(fixturefunc):
            fixturefunc = cast(
                Callable[..., Generator[FixtureValue, None, None]], fixturefunc
            )
            generator = fixturefunc(**kwargs)
            try:
                fixture_result = next(generator)
            except StopIteration:
                raise ValueError(f"{request.fixturename} did not yield a value") from None
            finalizer = functools.partial(_teardown_yield_fixture, fixturefunc, generator)
            request.addfinalizer(finalizer)
        else:
            fixturefunc = cast(Callable[..., FixtureValue], fixturefunc)
>           fixture_result = fixturefunc(**kwargs)

../automationwithpython/.venv/lib/python3.9/site-packages/_pytest/fixtures.py:898:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
tests/test_schedule_api_steps.py:85: in check_error_object
    data = response.json()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <Response [404]>, kwargs = {}

    def json(self, **kwargs):
        r"""Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        """

        if not self.encoding and self.content and len(self.content) > 3:
            # No encoding set. JSON RFC 4627 section 3 states we should expect
            # UTF-8, -16 or -32. Detect which one to use; If the detection or
            # decoding fails, fall back to `self.text` (using charset_normalizer to make
            # a best guess).
            encoding = guess_json_utf(self.content)
            if encoding is not None:
                try:
                    return complexjson.loads(self.content.decode(encoding), **kwargs)
                except UnicodeDecodeError:
                    # Wrong UTF codec detected; usually because it's not UTF-8
                    # but some other 8-bit codec.  This is an RFC violation,
                    # and the server didn't bother to tell us what codec *was*
                    # used.
                    pass
                except JSONDecodeError as e:
                    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

        try:
            return complexjson.loads(self.text, **kwargs)
        except JSONDecodeError as e:
            # Catch JSON-related errors and raise as requests.JSONDecodeError
            # This aliases json.JSONDecodeError and simplejson.JSONDecodeError
>           raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
E           requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

../automationwithpython/.venv/lib/python3.9/site-packages/requests/models.py:978: JSONDecodeError
======================================================================= short test summary info =======================================================================
FAILED tests/test_schedule_api_steps.py::test_verify_every_item_has_a_nonempty_id_and_type_is_always_episode - AttributeError: 'str' object has no attribute 'get'
FAILED tests/test_schedule_api_steps.py::test_verify_every_episode_title_is_never_null_or_empty - AttributeError: 'str' object has no attribute 'get'
FAILED tests/test_schedule_api_steps.py::test_verify_only_one_episode_is_live - AttributeError: 'str' object has no attribute 'get'
FAILED tests/test_schedule_api_steps.py::test_verify_start_date_is_before_end_date - AttributeError: 'str' object has no attribute 'get'
FAILED tests/test_schedule_api_steps.py::test_verify_404_and_error_object_for_invalid_date - requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
===================================================================== 5 failed, 2 passed in 3.15s =====================================================================
(.venv) olakoya@MacBookPro BBCSeniorTesterTestAssessment %
'''
