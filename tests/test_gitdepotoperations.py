        sh.git('clone',
        # It is there
            [],
        # It is not there
        self.assertEquals(
            ['deadbeef'],
            dcvs.check_changeset_availability(
                os.path.join(self.environment_path, 'repo1'),
                ['deadbeef']))

        # Multiple changesets
        self.assertEquals(
            ['deadbeef'],
            dcvs.check_changeset_availability(
                os.path.join(self.environment_path, 'repo1'),
                ['deadbeef', '52109e71fd7f16cb366acfcbb140d6d7f2fc50c9']))

        # All changesets
        self.assertEquals(
            [],
            dcvs.check_changeset_availability(
                os.path.join(self.environment_path, 'repo1'),
                [
                    'master',
                    'e3b1fc907ea8b3482e29eb91520c0e2eee2b4cdb',
                    '52109e71fd7f16cb366acfcbb140d6d7f2fc50c9',
                ]))
