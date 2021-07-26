import uuid

from dmoj.error import InternalError
from dmoj.executors import executors
from dmoj.graders.standard import StandardGrader
from dmoj.utils.unicode import utf8bytes

class MultipleFilesGrader(StandardGrader):
    def _generate_binary(self):
        from dmoj.config import ConfigNode

        siggraders = ('C', 'C11', 'CPP03', 'CPP11', 'CPP14', 'CPP17', 'CPP20', 'CLANG', 'CLANGX')

        if self.language in siggraders:
            aux_sources = {}
            handler_data = self.problem.config['files']
            header_names = handler_data['headers']
            source_names = handler_data['sources']

            if type(header_names) is ConfigNode and type(source_names) is ConfigNode: # multiple files
                for filename in header_names:
                    aux_sources[filename] = self.problem.problem_data[filename]
                for filename in source_names:
                    aux_sources[filename] = self.problem.problem_data[filename]         
            else:
                raise InternalError('invalid header container type %s' % type(handler_data))

            return executors[self.language].Executor(
<<<<<<< HEAD
                self.problem.id, self.source, aux_sources=aux_sources, defines=['-DMULTIPLE_FILE_GRADER'],
            )

        else:
            raise InternalError('no valid runtime for signature grading %s found' % self.language)
=======
                self.problem.id, self.sources, aux_sources=aux_sources, defines=['-DMULTIPLE_FILE_GRADER'],
            )

        else:
            raise InternalError('no valid runtime for signature grading %s found' % self.language)
>>>>>>> upstream/master
