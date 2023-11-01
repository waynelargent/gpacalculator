# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
db.define_table('grades',
                Field('grade',type='string',notnull=True,unique=True),
                Field('points',type='decimal(2,1)',notnull=True),
                format='%(grade)s'
                )

db.define_table('classes',
                Field('classname',type='string',notnull=True),
                Field('grade','reference grades'),
                Field('typeofclass',type='string',requires=IS_IN_SET(['Regular','Honors','AP','IB'])),
                Field('credits',type='integer',notnull=True),
                Field('yeartaken',type='integer',requires=IS_IN_SET([9,10,11,12])),
                Field('student_id', 'references auth_user', default =auth.user_id)
                )
