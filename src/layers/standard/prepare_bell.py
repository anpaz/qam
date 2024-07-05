import numpy as np

from qstack.instruction_definition import InstructionDefinition


class PrepareBell(InstructionDefinition):
    @property
    def names(self):
        return ["|bell>", "|bell⟩", "prepare_bell"]

    # @property
    # def instruction_type(self) -> str:
    #     return InstructionType.PREPARATION

    def matrix(self):
        # prepare statements return
        sqrt1_2 = np.sqrt(1 / 2)
        return np.array(
            [
                [sqrt1_2, 0.0, sqrt1_2, 0.0],
                [0.0, sqrt1_2, 0.0, sqrt1_2],
                [0.0, sqrt1_2, 0.0, -sqrt1_2],
                [sqrt1_2, 0.0, -sqrt1_2, 0.0],
            ]
        )
