test = {
  'name': 'Question',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(train_X.shape) == [7474, 20]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(test_X.shape) == [2492, 20]
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
